from django.shortcuts import render, get_object_or_404
from .models import Post, Comments
from django.utils import timezone
from .forms import CommentForm, SearchForm
from django.http import HttpResponseRedirect
from django.db.models import Q
from itertools import chain
from operator import attrgetter


def post_list(request):
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
                          {'post_list': post_list, 'sform': sform})
    else:
        sform = SearchForm()
    return render(request, 'blog/post_list.html', {'post_list': post_list,
                                                   'sform': sform})


def post_detail(request,pk):
    post=get_object_or_404(Post, pk=pk)
    comments = Comments.objects.filter(comments_post=pk)
    form = CommentForm
    return render(request, 'blog/post_detail.html', {'post':post,
                                                     'comments':comments,
                                                     'form':form})

def add_comment(request, post_pk):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.published_date = timezone.now()
            comment.comments_post = Post.objects.get(pk=post_pk)
            comment.save()
    return HttpResponseRedirect('/post/%s/' %post_pk)
