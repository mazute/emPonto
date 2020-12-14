from django.db import models

# Create your models here.
class Empresa(models.Model):
    nome = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=14)
    telefone = models.CharField(max_length=11)
    latitude = models.IntegerField()
    longitude = models.IntegerField()

    def __str__(self):
        return "{}".format(self.nome)

class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14)
    telefone = models.CharField(max_length=11)
    cargo = models.CharField(max_length=50)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)

    def __str__(self):
        return "{} {} {}".format(self.nome, self.cargo, self.empresa)

class Ponto(models.Model):
    horario = models.DateField()
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    
    def __str__(self):
        return "{} {}".format(self.horario, self.funcionario)