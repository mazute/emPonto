from django.db import models

# Create your models here.
class Empresa(models.Model):
    nome = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=18, unique=True)
    telefone = models.CharField(max_length=15)

    def __str__(self):
        return "{}".format(self.nome)

class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=18)
    telefone = models.CharField(max_length=15)
    cargo = models.CharField(max_length=50)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)

    def __str__(self):
        return "{} - {}".format(self.nome, self.cargo)

class Ponto(models.Model):
    horario = models.DateTimeField()
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE, verbose_name="Funcionário")
    
    def __str__(self):
        return "{} {}".format(self.horario, self.funcionario)