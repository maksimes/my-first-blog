from django.shortcuts import render, get_object_or_404
from .models import Post, Comments
from django.utils import timezone
from .forms import CommentForm, SearchForm, FeedbackForm
from django.http import HttpResponse
from django.db.models import Q
from itertools import chain
from operator import attrgetter
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
try:
    from django.utils import simplejson as json
except ImportError:
    import json
from django.core.mail import send_mail


def post_list(request):
    feedback_form = FeedbackForm()
    posts = Post.objects.filter(published_date__lte=timezone.now())
    post_list = posts.order_by('-published_date')
    comments = Comments.objects.all()
    q = request.GET.get('search_field')
    if q is not None:
        sform = SearchForm(request.GET)
        if sform.is_valid():
            cd = sform.cleaned_data
            postsf = posts.filter(Q(title__icontains=cd['search_field'])|
                                  Q(text__icontains=cd['search_field']))
            commentsf = comments.filter(text__icontains=cd['search_field'])
            post_list = sorted(chain(postsf, commentsf),
                               reverse = not(cd['sort_field']),
                               key = attrgetter('published_date'))
            return render(request, 'blog/post_list.html',
                          {'post_list': post_list, 'sform': sform,
                           'feedback_form':feedback_form})
    else:
        sform = SearchForm()
    return render(request, 'blog/post_list.html',
                  {'post_list': post_list, 'sform': sform,
                   'feedback_form':feedback_form})
#создание списка постов, поиск по постам


@require_POST
def feedback(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            if request.user.is_authenticated():
                feedback.author = request.user
            feedback.save()
            send_mail('Feedback maksblog', '%s | %s | %s | %s '
                      %(feedback.author, feedback.name, feedback.email,
                        feedback.text),
                      'maksblog.server@gmail.com', ['maksimes@mail.ru'],
                      fail_silently=False)
            message="Спасибо! Я с Вами свяжусь."
        return HttpResponse(message)
#форма обратной связи. Отправляет текст ОС на email


def post_detail(request,pk):
    post=get_object_or_404(Post, pk=pk)
    comments = Comments.objects.filter(comments_post=pk)
    form = CommentForm
    return render(request, 'blog/post_detail.html', {'post':post,
                                                     'comments':comments,
                                                     'form':form})
#отображает детальную информацию по постам, комментарии, форму их добавления


def comments_ajax(request, pk):
    comments = Comments.objects.filter(comments_post=pk)
    return render(request, 'blog/comments_ajax.html', {'comments':comments})
#подгружает комментарии в блок


@login_required
@require_POST
def add_comment(request, post_pk):
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.author = request.user
        comment.published_date = timezone.now()
        comment.comments_post = Post.objects.get(pk=post_pk)
        comment.save()
        message="ok"
    return HttpResponse(message)
#создание комментариев


@login_required
@require_POST
def add_like(request):
    user = request.user
    post_id = request.POST.get('postid', None)
    post = get_object_or_404(Post, id=post_id)
    if post.likes.filter(id=user.id).exists():
        post.likes.remove(user)
    else:
        post.likes.add(user)
    data = {'likes_count':post.total_likes, 'post_id':post.id}
    return HttpResponse(json.dumps(data), content_type="application/json")
#добавление и удаление лайков