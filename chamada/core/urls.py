from django.urls import path
from . import views

urlpatterns = [
  path('', views.Chamada, name='Chamada'),
  path('Listar/', views.Listar, name='Listar'),
]
