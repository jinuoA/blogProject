

from django.conf.urls import url
from blog.views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    url(r'^$', index,name='index'),
    url(r'^index/$', index,name='index'),
    url(r'^archive/$', archive,name='archive'),
    url(r'^article/$', article,name='article'),
    url(r'^login/$', do_login,name='login'),
    url(r'^logout/$', logout,name='logout'),
    url(r'^reg/$', do_reg,name='reg'),
    url(r'^category/$', category,name='category'),
    url(r'^comment_post/$', comment_post,name='comment_post'),
]+staticfiles_urlpatterns()
