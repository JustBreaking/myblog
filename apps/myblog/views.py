#-*-coding:utf-8-*-
from django.shortcuts import render, get_object_or_404
from django.views.generic.base import View
from django.db.models import Q

from .models import Article, UserProfile, Tag, Category

from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

#博客index
class IndexView(View):
    def get(self, request):
        return render(request, 'index.html', {})

#博客首页
class HomeView(View):
    def get(self, request):
        article_list = Article.objects.filter(is_aboutme=False).order_by('-create_time')

        #文章分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(article_list, 5, request=request) #每一页5条
        articles = p.page(page)

        return render(request, 'home.html', {
            'article_list':articles,
        })

#博客归档
class ArchivesView(View):
    def get(self, request, year, month):
        archive = '%s年%s月' % (year, month)
        article_list = Article.objects.filter(create_time__year=year, create_time__month=month).order_by('-create_time')

        #文章分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(article_list, 5, request=request) #每一页5条
        articles = p.page(page)

        return render(request, 'article_list.html', {
            'article_list':articles,
            'archive':archive,
        })

#分类名称列表页
class CategoryListView(View):
    def get(self, request):
        return render(request, 'categorylist.html', {})

#博客分类
class CategoryView(View):
    def get(self, request, category_id):
        category_name = Category.objects.get(id = category_id).name
        article_list = Article.objects.filter(category__id = int(category_id)).order_by('-create_time')

        #文章分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(article_list, 5, request=request) #每一页5条
        articles = p.page(page)

        return render(request, 'article_list.html', {
            'article_list':articles,
            'category_name':category_name,
        })

#标签列表页
class TagListView(View):
    def get(self, request):
        return render(request, 'taglist.html', {})

#所属标签的文章列表
class TagsView(View):
    def get(self, request, tag_id):
        tag = Tag.objects.get(id = int(tag_id))
        article_list = tag.article_set.all().order_by('-create_time')

        #文章分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(article_list, 5, request=request) #每一页5条
        articles = p.page(page)

        return render(request, 'article_list.html', {
            'article_list':articles,
            'tag_name':tag.name,
        })

#关于我
class AboutView(View):
    def get(self, request):
        article = get_object_or_404(Article, is_aboutme = True)
        return render(request, 'about.html', {
            'article':article,
        })

#博客相册
class PhotoView(View):
    def get(self, request):
        return render(request, 'photo.html', {})

#音乐
#文章分类
class MusicView(View):
    def get(self, request):
        return render(request, 'music.html', {})

#文章详情页
class ArticleDetailView(View):
    def get(self, request, article_id):
        article_detail = Article.objects.get(id=int(article_id))

        pre_id, next_id = -1, -1
        article_pre = Article.objects.filter(id__lt=int(article_id))
        if article_pre:
            pre_id = article_pre[0].id
        article_next = Article.objects.filter(id__gt=int(article_id))
        if article_next:
            next_id = article_next[0].id

        return render(request, 'article_detail.html', {
            'article_detail':article_detail,
            'pre_id':pre_id,
            'next_id':next_id,
        })

#搜索
def search(request):
    q = request.GET.get('q')
    error_msg = ''

    if not q:
        error_msg = "请输入关键词"
        return render(request, 'article_list.html', {'error_msg': error_msg})

    article_list = Article.objects.filter(Q(title__icontains=q) | Q(content__icontains=q))

    #文章分页
    try:
        page = request.GET.get('page', 1)
    except PageNotAnInteger:
        page = 1

    p = Paginator(article_list, 5, request=request) #每一页5条
    articles = p.page(page)
    return render(request, 'article_list.html', {
        'error_msg': error_msg,
        'article_list': articles,
    })
