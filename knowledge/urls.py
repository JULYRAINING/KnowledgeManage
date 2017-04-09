"""KnowledgeManage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.contrib.auth.decorators import login_required

from . import views
from django.contrib import admin

admin.autodiscover()
urlpatterns = [
    url(r'^$', views.UserInterfaceDocumentListView.as_view(), name='index'),
    url(r'^upload/$', views.upload_page, name='upload_document'),
    url(r'^assess/(?P<slug>.+)/$', login_required(views.DocumentDetailView.as_view()), name='document_detail'),

    url(r'^filter_category', views.filter_category, name='filter_category'),
    url(r'^filter_date', views.filter_date, name='filter_date'),
    url(r'^subscribe', views.subscribe, name='subscribe'),
    url(r'^document_list', login_required(views.DocumentListView.as_view()), name='document_list'),
    url(r'^preview', views.pdf_fullscreen_preview, name='pdf_fullscreen_preview'),
    url(r'^comment', views.comment, name='comment'),
    url(r'^test', views.test, name='test'),
    url(r'^get_document', views.get_document, name='get_document'),
    #always on bottom ,otherwise it will cover other url matchs.
    url(r'^(?P<slug>.+)/$', login_required(views.UserInterfaceDocumentDetailView.as_view()), name='post_content'),
]


