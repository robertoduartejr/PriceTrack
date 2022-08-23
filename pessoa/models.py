from django.db import models

# Create your models here.

class Pessoa(models.Model):
    nome_completo = models.CharField(max_length=256)
    data_nascimento = models.DateField(null=True)
    ativa = models.BooleanField(default=True)

    def __str__(self):
        return self.nome_completo

class Contato(models.Model):
    nome = models.CharField(max_length=256)
    email = models.EmailField(max_length=256)
    telefone = models.CharField(max_length=20)
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE) # se remover a pessoa, essas informaçoes sao removidas tbm

    def __str__(self):
        return self.nome

