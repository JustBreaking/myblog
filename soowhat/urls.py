#-*-coding:utf-8-*-
"""soowhat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.views.static import serve
# from django.contrib import admin
import xadmin
import myblog
from myblog.views import IndexView
from soowhat.settings import MEDIA_ROOT

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^$', IndexView.as_view(), name="index"),

    #富文本相关
    url(r'^ueditor/',include('DjangoUeditor.urls' )),

    #myblog下的相关配置
    url(r'^blog/', include('myblog.urls', namespace='blog')),

    #设置上传文件的访问处理
    url(r'^media/(?P<path>.*)$', serve, {"document_root":MEDIA_ROOT}),
]
