from django.forms import ModelForm
from .models import Tarefa

class FormTarefa(ModelForm):
    class Meta:
        model = Tarefa
        exclude = ['data','completa', 'user']