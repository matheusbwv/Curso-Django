from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import login, logout, authenticate
from .models import Tarefa
from .forms import FormTarefa
from .serializer import TarefaSerializer

# Create your views here.


@api_view(['POST'])
def createUser(request):
    username = request.data.get('username')
    email = request.data.get('email')
    password = request.data.get('password')
    
    try:
        userExists = User.objects.get(username=username)
    except:
        userExists = None

    if username == None or password == None or email == None:
        return Response({"message":"Informações incorretas!"})
    elif userExists:
        return Response({"message":"Usuário já existe!"})   

    user = User.objects.create(username=username, email=email, password=make_password(password))

    mensagem = "Usuário " + user.username + " criado!"

    return Response({"message":mensagem})



@api_view(['POST'])
def loginUser(request):
    username = request.data.get("username")
    password = request.data.get("password")

    if username == None or password == None:
        return Response({"message":"Informações incorretas!"})

    try:
        user = User.objects.get(username=username)
    except:
        return Response({"message":"Usuário não existe!"})
    
    user = authenticate(username=username, password=password)
    if user:
        login(request, user)
        return Response({"message":"Usuário Logado!"})
    else:
        return Response({"message":"Username ou senha errado!"})
    
@api_view(['GET'])
def checkLogin(request):
    if request.user.is_authenticated:
        mensagem = request.user.username + " está logado!"
        return Response({"message":mensagem})
    else:
        return Response({"message":"Você está deslogado!"})
    
@api_view(['GET'])
def userLogout(request):
    if request.user.is_authenticated:
        logout(request)
        return Response({"message":"logout feito com sucesso! Você está deslogado!"})
    else:
        return Response({"message":"Você já está deslogado!"})
    
# Criação das Tarefas da to-do List
    
@api_view(['POST'])
def criarTarefa(request):
    if request.user.is_authenticated:
        dados = request.data
        form = FormTarefa(dados)
        if form.is_valid():
            form.save()
            return Response({"Mensagem":"ok"})

        return Response({"Mensagem":"not OK"})
    else:
        return Response({"Mensagem":"Usuário não Logado!"})

@api_view(["GET"])
def verTarefas(request):
    if request.user.is_authenticated:
        tarefas = Tarefa.objects.all()
        serializer = TarefaSerializer(tarefas, many=True)
        return Response({"Tarefas":serializer.data})
    else:
        return Response({"Mensagem":"Usuário não Logado!"})
@api_view(["PUT","POST"])
def verUmaTarefa(request):
    try:
        if request.user.is_authenticated:
            
            id = request.data.get('id')

            tarefa = Tarefa.objects.get(id = id)

            serializer = TarefaSerializer(tarefa)
            return Response({"Tarefas":serializer.data})
        else:
            return Response({"Mensagem":"Usuário não Logado!"})
    except:
        return Response({"Mensagem":"send to us an ID!"})

@api_view(["POST","PUT","DELETE"])
def deletarTarefa(request):
    try:
        if request.user.is_authenticated:
            
            id = request.data.get('id')

            tarefa = Tarefa.objects.get(id = id)

            tarefa.delete()
            
            return Response({"Tarefas":"Tarefa Deletada!"})
        else:
            return Response({"Mensagem":"Usuário não Logado!"})
    except:
        return Response({"Mensagem":"send to us an ID!"})
    
@api_view(["PUT"])
def editarTarefa(request):
    try:
        if request.user.is_authenticated:
            
            id = request.data.get('id')

            tarefa = Tarefa.objects.get(id = id)

            form = FormTarefa(instance=tarefa,data=request.data)

            if form.is_valid:
                form.save()

                tarefa = Tarefa.objects.get(id = id)
                serializer = TarefaSerializer(tarefa)
                return Response({"Tarefas": serializer.data})
        else:
            return Response({"Mensagem":"Usuário não Logado!"})
    except:
        return Response({"Mensagem":"send to us an ID!"})

@api_view(["PUT"])
def concluirTarefa(request):
    
    id = request.data.get('id')
    tarefa = Tarefa.objects.get(id = id)

    if request.user.is_authenticated:
        tarefa.completa = True
        tarefa.save()
        mensagem = "A tarefa de Titulo " + tarefa.titulo + " foi concluida"
        return Response({"Mensagem":mensagem })
# except:
#         return Response({"Mensagem":"Precisa-se de um ID valido!"})


