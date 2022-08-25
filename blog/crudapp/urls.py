from django.urls import path,include
from crudapp import views
urlpatterns = [
    path('', views.home , name='home'),
    path('login/', views.login, name='login'),
    path('register/', views.registartion, name='register')
]

