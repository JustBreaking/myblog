#-*-coding:utf-8-*-

from django import template
from django.template.defaultfilters import stringfilter
from django.db.models.aggregates import Count

from ..models import Article, UserProfile, Category, Tag

register = template.Library()

@register.filter
def is_greate(value, custom): # value为前端传递的参数
    try:
        if int(value) > int(custom):
            return True
        else:
            return False
    except:
        return False

#文章归档
@register.simple_tag
def archives():
    return Article.objects.datetimes('create_time', 'month', order='DESC')

#获取文章归档下的文章数量
@register.filter
def get_articlenums(date):
    return Article.objects.filter(create_time__year=date.year, create_time__month=date.month).count()

#获取博主信息
@register.simple_tag
def get_bloger():
    return UserProfile.objects.get(username='admin')

#文章分类
@register.simple_tag
def get_categories():
    #模板中可以获取类名和分类下的文章数num_articles
    return Category.objects.exclude(name='个人简介').annotate(num_articles=Count('article')).filter(num_articles__gt=0)  #注意此处有两个_

@register.simple_tag
def get_tags():
    return Tag.objects.annotate(num_articles=Count('article')).filter(num_articles__gt=0)
