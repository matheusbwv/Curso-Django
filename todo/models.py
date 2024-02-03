from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Tarefa(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    data = models.DateField(auto_now=True)
    completa = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null = True)