from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('vagas/', views.lista_vagas, name='lista_vagas'),
    path('vagas/<int:pk>/', views.detalhe_vaga, name='detalhe_vaga'),
    path('gestao/', views.painel_gestao, name='painel_gestao'),
    path('gestao/criar/', views.criar_vaga, name='criar_vaga'),
    path('gestao/editar/<int:pk>/', views.editar_vaga, name='editar_vaga'),
    path('gestao/eliminar/<int:pk>/', views.eliminar_vaga, name='eliminar_vaga'),
    path('perfil/', views.perfil, name='perfil'),
        
]