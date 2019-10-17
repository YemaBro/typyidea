from django.urls import path
from .views import post_list, post_detail

urlpatterns = [
    path(r'^$', post_list),
    path(r'^category/(?P<category_id>\d+)/$', post_list),
    path(r'^tag/(?P<tag_id>\d+)/$', post_list),
    path(r'^post/(?P<post_id>\d+).html$', post_detail),
]
