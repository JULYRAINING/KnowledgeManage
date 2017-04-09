from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.http import request

class AuthenticationMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        if request.path == '/login/':
            if request.method == 'POST':
                username = request.POST.get('username')
                password = request.POST.get('password')
                if username == '123' and password == '456':
                    request.session['IS_LOGIN'] = True
                    return HttpResponseRedirect('/knowledge/')
                else:
                    request.session['IS_LOGIN'] = False
                    return HttpResponseRedirect('/login/')
            else:
                pass
        elif request.path == '/logout/':
            request.session['IS_LOGIN'] = False
            return HttpResponseRedirect('/login/')

        elif request.path == '/admin/':
            return False
        else:
            try:
                is_login = request.session['IS_LOGIN']
                if is_login:
                    pass
                else:
                    return HttpResponseRedirect('/login/')
            except:
                return HttpResponseRedirect('/login/')

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response



