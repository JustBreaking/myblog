# -*- coding: utf-8 -*-

from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser
from future.utils import python_2_unicode_compatible

from DjangoUeditor.models import UEditorField

@python_2_unicode_compatible
#继承了AbstractUser,该类中已有user的很多信息
class UserProfile(AbstractUser):
    nickname = models.CharField(max_length=16, verbose_name=u'昵称', null=True, blank=True)
    birday = models.DateField(verbose_name=u'生日', null=True, blank=True)
    gender = models.CharField(max_length=8, choices=(('male',u'男'),('female',u'女')))
    address = models.CharField(max_length=64, null=True, blank=True)
    mobile = models.CharField(max_length=11, null=True, blank=True)
    avator = models.ImageField(upload_to="avator/%Y/%m", default = 'avator/default.png', max_length=64)
    background_image = models.ImageField(upload_to="image/%Y/%m", default = 'image/default.png', max_length=64)

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name  #复数形式，若不设置，后台显示会多一个s

    def __str__(self):
        return self.username


#文章的分类
@python_2_unicode_compatible
class Category(models.Model):
    name = models.CharField(max_length=20, verbose_name=u'类名' )

    class Meta:
        verbose_name = u"分类"
        verbose_name_plural = verbose_name  #复数形式，若不设置，后台显示会多一个s

    def __str__(self):
        return self.name

@python_2_unicode_compatible
class Tag(models.Model):
    name = models.CharField('标签名',  max_length=32)

    class Meta:
        verbose_name = u"标签"
        verbose_name_plural = verbose_name  #复数形式，若不设置，后台显示会多一个s

    def __str__(self):
        return self.name

#博客文章
@python_2_unicode_compatible
class Article(models.Model):
    title = models.CharField('标题', max_length = 64)
    image = models.ImageField(upload_to='article/%Y/%m', verbose_name=u'封面图', max_length=64, default = 'article/default.png')
    # author = models.ForeignKey(Author, verbose_name='作者', null=True, on_delete=models.SET_NULL)
    # content = models.TextField('正文')
    content = UEditorField(verbose_name=u'文章内容',width=600, height=300, toolbars="full",
            imagePath="article/ueditor/",
            filePath="article/ueditor/",
            default = ""
        )
    create_time = models.DateTimeField('创建时间', auto_now_add=True)   #文章添加时自动添加创建时间
    last_modified_time = models.DateTimeField('最近编辑时间', auto_now=True)
    status = models.CharField('文章状态', max_length=1, choices = (('d', 'Draft'),('p', 'Published'),))
    abstract = models.CharField('摘要', max_length=54, blank=True, null=True, help_text="可选，如若为空将摘取正文前54个字符")
    views = models.PositiveIntegerField('浏览量', default=0)   # PositiveIntegerField 存储非负整数
    topped = models.BooleanField('置顶', default=False)
    #on_delete=models.SET_NULL 表示删除category分类后该分类下所有的Article的外键均设为null
    category = models.ForeignKey(Category, verbose_name='分类', null=True, on_delete=models.SET_NULL)
    tags = models.ManyToManyField(Tag, verbose_name='标签集合', blank=True)
    is_aboutme = models.BooleanField('关于自己', default = False) #有一篇文章为自己的个人简介

    class Meta:
        verbose_name = u"文章"
        verbose_name_plural = verbose_name

    def __str__(self):
        #主要用于交互解释器显示表示该类的字符串
        return self.title

    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])

    # #重写save(), 自动生成abstract字段
    # def save(self, *args, **kwargs):
    #     if not self.abstract:
    #         self.abstract = self.content[:54]
    #     super(Article, self).save(*args, **kwargs)


#点赞
@python_2_unicode_compatible
class Upvote(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name='用户', null=True)
    article = models.ForeignKey(Article, verbose_name='文章', null=True)
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u'点赞时间')
