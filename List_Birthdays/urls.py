from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_new/', views.add_new, name='add_new'),
    path('list_all/', views.list_all, name='list_all'),
]
