from django.contrib import messages
from django.http import HttpResponse, request
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.urls import reverse
from django.views import View
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import UpdateView
from django.contrib.auth import logout as auth_logout
from .models import User
from django.contrib.auth.models import Group

def signup(request):
    if request.method == 'GET':
        print('nonono1')
        return render(request, 'user/signup.html')
    else:
        print('nonono2')
        username = request.POST.get('username', '')
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        print(username, password, email)
        user = User.objects.create_user(username = username, email=email, password=password)
        
        Group.objects.last().user_set.add(user)
        
        new_user = authenticate(username=username, password=password)
        if new_user is not None:
            auth_login(request, new_user)
           # return HttpResponse('Invalid login credentials')
            print('nonono')
            return HttpResponseRedirect(reverse('knowledge:index'))
        else:
            return HttpResponse('Invalid login credentials')



def logout(request):
    auth_logout(request)
    return render(request, 'user/login.html')

def login(request):
    if request.method == 'GET':
        return render(request, 'user/login.html')
    else:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        user = authenticate(username=username, password=password)
        if user is not None:
            auth_login(request, user)
           # return HttpResponse('Invalid login credentials')
            return HttpResponseRedirect(reverse('knowledge:index'))
        else:
            return HttpResponse('Invalid login credentials')


#
#class Login(View):
#
#
#    def get(self, request):
#        return render(request, 'user/login.html')
#    def post(self, request):
#        username = request.POST['username']
#        password = request.POST['password']
#        print(username,password)
#        user = authenticate( username=username, password=password)
#        if user is not None:
#            login(request, user)
#            return HttpResponseRedirect('/knowledge/')
#        else:
#            messages.error(request, 'Invalid login credentials')
#            #return HttpResponse()
#
#
#
