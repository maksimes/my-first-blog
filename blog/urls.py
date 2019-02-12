from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/(?P<post_pk>[0-9]+)/add_comment/$', views.add_comment,
        name='add_comment'),
    url(r'^post/(?P<pk>[0-9]+)/comments_ajax/$', views.comments_ajax, name='comments_ajax'),
    url(r'add_like/$', views.add_like, name='add_like'),
]
