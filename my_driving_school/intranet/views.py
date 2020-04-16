from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from django.utils.decorators import method_decorator

from .forms import AdminUserCreationForm, SecretaryUserCreationForm
from .models import User


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

def not_authorized(request):
    return render(request, 'auth/not_authorized.html')

@login_required
def wip(request):
    return render(request, 'intranet/index.html')

@login_required
def create_user(request):
    if not (request.user.is_superuser or request.user.is_secretary):
        return redirect('intranet:not_authorized')

    if request.method == 'POST':
        f = None
        if request.user.is_superuser:
            f = AdminUserCreationForm(request.POST)
        else:
            f = SecretaryUserCreationForm(request.POST)

        if f.is_valid():
            f.save()
            return redirect('intranet:index')
 
    else:
        f = None
        if request.user.is_superuser:
            f = AdminUserCreationForm(request.POST)
        else:
            f = SecretaryUserCreationForm(request.POST)
 
    return render(request, 'users/create.html', {'form': f})

@method_decorator(login_required, name='dispatch')
class SecretariesView(generic.ListView):
    template_name = 'users/index.html'
    context_object_name = 'users'

    def get_queryset(self):
        return User.objects.filter(is_secretary=True)

@method_decorator(login_required, name='dispatch')
class InspectorsView(generic.ListView):
    template_name = 'users/index.html'
    context_object_name = 'users'

    def get_queryset(self):        
        return User.objects.filter(is_inspector=True)

@method_decorator(login_required, name='dispatch')
class StudentsView(generic.ListView):
    template_name = 'users/index.html'
    context_object_name = 'users'

    def get_queryset(self):        
        return User.objects.filter(is_student=True)

