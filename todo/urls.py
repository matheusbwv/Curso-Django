from django.urls import path
from . import views

urlpatterns = [
    path('createUser/', views.createUser),
    path('login/', views.loginUser),
    path('checkLogin/', views.checkLogin),
    path('logout/', views.userLogout),
    path('createTask/', views.criarTarefa),
    path('verTarefas/', views.verTarefas),
    path('verUmaTarefa/', views.verUmaTarefa),
    path('deletarTarefa/', views.deletarTarefa),
    path('updateTarefa/', views.editarTarefa),
    path('concluirTarefa/', views.concluirTarefa)
]