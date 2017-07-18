# -*- coding: utf-8 -*-

from django.conf.urls import url
from .views import HomeView, ArchivesView, AboutView, PhotoView, MusicView, ArticleDetailView, CategoryView, TagListView, TagsView, CategoryListView

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', ArchivesView.as_view(), name='archives'),

    url(r'^category_list/$', CategoryListView.as_view(), name='category_list'),    #分类列表页
    url(r'^category/(?P<category_id>\d+)/$', CategoryView.as_view(), name='category'),

    url(r'^tag_list/$', TagListView.as_view(), name='tag_list'),    #标签列表页
    url(r'^tag/(?P<tag_id>\d+)/$', TagsView.as_view(), name='tag'), #所属标签的文章列表

    url(r'^about/', AboutView.as_view(), name='about'),
    url(r'^photo/', PhotoView.as_view(), name='photo'),
    url(r'^music/', MusicView.as_view(), name='music'),
    url(r'^article_detail/(?P<article_id>\d+)/$', ArticleDetailView.as_view(), name='article_detail'),
]
