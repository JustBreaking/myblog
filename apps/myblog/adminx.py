# -*- coding: utf-8 -*-

import xadmin
from .models import Article, UserProfile, Category, Tag

class ArticleAdmin(object):
    list_display = ['title', 'image', 'status', 'views', 'topped', 'category', 'tags']
    search_fields = ['title', 'image', 'status', 'views', 'topped', 'category', 'tags']
    list_filter = ['title', 'image', 'status', 'views', 'topped', 'category', 'tags']

    ordering = ['-views']

    readonly_fields = ['views']

    exclude = ['abstract']

    style_fields = {'content':'ueditor'}

    class Media:
        # 在管理后台的HTML文件中加入js文件, 每一个路径都会追加STATIC_URL/
        js = (
            'js/editor/kindeditor/kindeditor-all.js',
            'js/editor/kindeditor/lang.zh_CN.js',
            'js/editor/kindeditor/config.js',
        )

class CategoryAdmin(object):
    list_display = ['name']
    search_fields = ['name']
    list_filter = ['name']

class TagAdmin(object):
    list_display = ['name']
    search_fields = ['name']
    list_filter = ['name']


xadmin.site.register(Article, ArticleAdmin)
xadmin.site.register(Category, CategoryAdmin)
xadmin.site.register(Tag, TagAdmin)
