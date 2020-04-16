from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.urls import reverse
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

class LoginView(View):
    def get(self, request):
        return render(request, 'auth/login.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('intranet:index'))
        else:
            return render(request, 'auth/login.html', { 'error_message' : 'Invalid login or password' })

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('intranet:index')) 

@login_required
def wip(request):
    return render(request, 'intranet/index.html')