"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from blogs import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index',views.index,name='index'),
    url(r'^login/',views.loginn,name='login'),
    url(r'^logout/',views.logoutt,name='logout'),
    url(r'^register/',views.register,name='register'),
    url(r'^user/(?P<x>\d+)',views.users,name='user'),
    url(r'^article/(?P<y>\d+)',views.article,name='article'),
    url(r'^add_article/',views.add_article,name='add_art'),
    url(r'^poll/(?P<p>\d+)',views.poll,name='poll'),
    url(r'^keep/(?P<k>\d+)',views.keep,name='keep'),
    url(r'^fabu/',views.fabu,name='fabu'),
    url(r'^shoucang/',views.shoucang,name='shoucang'),
    url(r'^pinglun/',views.pinglun,name='pinglun'),
]
