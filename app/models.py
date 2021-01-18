from django.db import models

# Create your models here.

max_caracteres = 300

estados = {'Feito' : True, 'Pendente' : False}

class Tarefas(models.Model):
    
    data_de_nascimento = models.DateTimeField(auto_now_add=True)

    data_de_edit = models.DateTimeField(auto_now=True)

    nome = models.CharField(max_length = max_caracteres)
    
    info = models.TextField()
    
    status = models.BooleanField(
        choices=[(True, 'Feita'),(False, 'Pendente')]
    )

    def __str__(self):
        return self.nome


    
