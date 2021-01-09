from django.urls import path
from . import views

app_name = 'imageAdd'

urlpatterns = [
    path('', views.index, name='index'),
]