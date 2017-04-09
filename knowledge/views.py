from django.contrib.auth.models import Group
from django.http import HttpResponse
from django.http import request
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

# Create your views here.
from django.template import RequestContext
from django.utils import timezone
from django.views.generic import DetailView
from django.views.generic import ListView

from knowledge.models import *
from user.models import *
from knowledge.variable import parameter

from templated_docs import fill_template
from templated_docs.http import FileResponse


class UserInterfaceDocumentListView(ListView):

    model = Document

    def get_template_names(self):
        return "knowledge/index.html"

    def get_context_data(self, **kwargs):
        context = super(UserInterfaceDocumentListView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        categorys = []
        for j in range(2):
           category = Category()
           category.name = '人文'
           category.length = 500
           categorys.append(category)
        #context['object_list'] =  Document.objects.all()
        context['categorys'] = categorys
        context.update(parameter)
        return context




class UserInterfaceDocumentDetailView(DetailView):
    model = Document


    def get_template_names(self):
        return "knowledge/post.html"


    def get_context_data(self, **kwargs):
        context = super(UserInterfaceDocumentDetailView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        document_id = context['object'].id
        context['comments'] = Comment.objects.filter(document = document_id)
        context.update(parameter)
        return context
@login_required
def filter_category(request):
    return render(request, 'knowledge/filter_category.html', parameter)
@login_required
def filter_date(request):
    return render(request, 'knowledge/filter_date.html', parameter)
@login_required
def subscribe(request):
    form = SubscribeModelForm()
    return render(request, 'knowledge/subscribe.html', dict(parameter, **{'form': form}))
'''
    #document = Document()
    #document.name = '标题'
    #document.date = '2017/01/07'
    #document.category = '分类'
    #document.description = '描述'
    #document.con##tent = 'content'
    #document.tag = ['django','Python','系统','Web','信息管理','信息技术','人工智能']

    ##comments = []
    ##for i in range(4):
    ##    comment = Comment()
    ##    comment.username = 'username'
    ##    comment.date = 'date'
    ##    comment.content = 'content'
##
    ##    comments.append(comment)

    #post = {'post': document}
    #comments = {'comments':comments}
    #parameter.update(post)
    #parameter.update(comments)
#
#
    #return render(request, 'knowledge/post.html', parameter)
'''


class DocumentDetailView(DetailView):

    model = Document

    def get_template_names(self):
        return "knowledge/document_detail.html"

    def get_context_data(self, **kwargs):
        context = super(DocumentDetailView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class DocumentListView(ListView):

    model = Document

    #def get_queryset(self):
    #    return Document.objects.all()

    def get_template_names(self):
        return "knowledge/document_list.html"

    def get_context_data(self, **kwargs):
        context = super(DocumentListView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        #context['object_list'] =  Document.objects.all()
        return context

@login_required
def upload_page(request):
    if request.method=="POST":
        form = DocumentModelForm(request.POST, request.FILES)
        if form.is_valid(): #所有验证都通过
            document = form.save(commit = False)
            document.uploader = request.user
            document.save()
            #do something处理业务
            return HttpResponseRedirect('/knowledge')
    else:
        form = DocumentModelForm()

        return render(request, 'knowledge/document_upload_page.html',  dict(parameter, **{'form': form}))

@login_required
def pdf_fullscreen_preview(request):
    if request.method == "GET":
        file_path = request.GET.get('file_path', '')

        return render(request, 'knowledge/pdf_fullscreen_preview.html', {'file_path': file_path})
@login_required
def comment(request):
    if request.method == "POST":
        content = request.POST.get('content', '')
        document_id = request.POST.get('documentid', '')

        comment = Comment()
        comment.document = Document.objects.get(id=document_id)
        comment.author = request.user
        comment.content = content
        comment.date = timezone.now()
        comment.level = Group.objects.get(id = 4)
        comment.save()
        return HttpResponse('评论成功')
    else:
        return HttpResponse('error')
@login_required
def test(request):
    form = DocumentModelForm()
    return render(request, 'knowledge/collapse_button.html')

#http://localhost:8000/knowledge/get_document
def get_document(request):

    models_li = [
    'Category',
    'DocumentStatus',
    'Document',
    'DocumentAssess',
    'Comment',
    'Subscribe',
    'ReadTrace',
    'User',
    'Permission',
    'PermissionControl',
    ]
    def retrive_data(x):
        return eval(x + '._meta')

    context = {'models':map(retrive_data, models_li)}
    return render(request, 'knowledge/model_structure.html', context)


