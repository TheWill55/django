from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()

class NumeroEscolhido(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    numero = models.IntegerField()