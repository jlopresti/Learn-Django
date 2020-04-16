from django.urls import path

from . import views

app_name = 'intranet'
urlpatterns = [
    path('', views.wip, name='index'),
    path('auth/login', views.LoginView.as_view(), name='login'),
    path('auth/logout', views.logout_view, name='logout'),
]