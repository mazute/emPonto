from django.contrib import admin

from .models import Empresa, Funcionario, Ponto
# Register your models here.
admin.site.register(Empresa)
admin.site.register(Funcionario)
admin.site.register(Ponto)