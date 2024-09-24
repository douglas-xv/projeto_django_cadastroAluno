from django.db import models

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    sobrenome = models.TextField(max_length=255)
    idade = models.TextField(max_length=255)
    telefone = models.TextField(max_length=11)
    curso = models.TextField(max_length=255)

