from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^register/$', views.register, name='register'),
    url(r'^user_login/$', views.user_login, name='login'),
    url(r'^log_out/$', views.log_out, name='log_out'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^edit_profile/$', views.edit_profile, name='edit_profile'),
    url(r'^password-change/$', auth_views.password_change,
        {'template_name': 'account/password_change.html'},
        name='password_change'),
    url(r'^password-change/done/$', auth_views.password_change_done,
        {'template_name': 'account/password_change_done.html'},
        name='password_change_done'),
    url(r'^profile/(?P<u_name>[a-zA-Z0-9_]+)/$', views.other_profile,
        name='other_profile'),
]