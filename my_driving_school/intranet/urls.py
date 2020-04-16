from django.urls import path

from . import views

app_name = 'intranet'
urlpatterns = [
    path('', views.wip, name='index'),
    path('auth/login', views.LoginView.as_view(), name='login'),
    path('auth/not_authorized', views.not_authorized, name='not_authorized'),
    path('auth/logout', views.logout_view, name='logout'),
    path('users/secretaries', views.SecretariesView.as_view(), name='view_secretaries'),
    path('users/inspectors', views.InspectorsView.as_view(), name='view_inspectors'),
    path('users/students', views.StudentsView.as_view(), name='view_students'),
    path('users/create', views.create_user, name='create_user'),
]