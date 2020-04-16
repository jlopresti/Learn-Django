from django.urls import path

from . import views

app_name = 'intranet'
urlpatterns = [
    path('', views.wip, name='index'),
    path('login/', views.LoginView.as_view(), name='login'),
]