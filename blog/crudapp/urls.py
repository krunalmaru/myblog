from django.urls import path,include
from crudapp import views
urlpatterns = [
    path('', views.home , name='home')
]

