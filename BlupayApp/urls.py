import BlupayApp.views

from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^(?P<t_id>.*?)/(?P<rf_id>.*?)/(?P<amt>.*?)/(?P<l_or_s_or_c>\d{1}.*?)/(?P<date_time>.*?)/$', 'BlupayApp.views.get_post_function'),
    url(r'^(?P<t_id>.*?)/(?P<uname>.*?)/(?P<pword>.*?)/$', 'BlupayApp.views.get_post_login'),
)
