from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import Empresa, Funcionario, Ponto

from django.urls import reverse_lazy

# Create your views here.

class EmpresaCreate(CreateView):
    model = Empresa
    fields = ['nome', 'cnpj', 'telefone']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-empresa')

class FuncionarioCreate(CreateView):
    model = Funcionario
    fields = ['nome', 'cpf', 'telefone', 'cargo', 'empresa']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-funcionario')

class PontoCreate(CreateView):
    model = Ponto
    fields = ['horario', 'funcionario']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-ponto')

class EmpresaUpdate(UpdateView):
    model = Empresa
    fields = ['nome', 'cnpj', 'telefone']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-empresa')

class FuncionarioUpdate(UpdateView):
    model = Funcionario
    fields = ['nome', 'cpf', 'telefone', 'cargo', 'empresa']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-funcionario')

class PontoUpdate(UpdateView):
    model = Ponto
    fields = ['horario', 'funcionario']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-ponto')

class EmpresaDelete(UpdateView):
    model = Empresa
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-empresa')

class FuncionarioDelete(UpdateView):
    model = Funcionario
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-funcionario')

class PontoDelete(UpdateView):
    model = Ponto
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy('listar-campo')

class EmpresaList(ListView):
    model = Empresa
    template_name = 'cadastros/listas/empresa.html'


class FuncionarioList(ListView):
    model = Funcionario
    template_name = 'cadastros/listas/funcionario.html'


class PontoList(ListView):
    model = Ponto
    template_name = 'cadastros/listas/ponto.html'
