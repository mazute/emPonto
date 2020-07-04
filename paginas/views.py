
# Importar o TemplateView para criar páginas simples
from django.views.generic import TemplateView


# Create your views here.

# A classe PaginaInicial "extends" TemplateView
class index(TemplateView):
    # Toda classe filha do TemplateView precisa do
    # atributo abaixo para definir um template a ser renderizado
    template_name = 'paginas/index.html'

class DiagramaCasoUso(TemplateView):
    template_name = 'paginas/diagramaCasoUso.html'

class DiagramaClasse(TemplateView):
    template_name = 'paginas/diagramaClasse.html'    
