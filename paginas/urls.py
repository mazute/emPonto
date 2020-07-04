from django.urls import path

# Importa as views que a gente criou 
from .views import index, DiagramaCasoUso, DiagramaClasse

# Tem que ser urlpatterns porque é padrão do Django
urlpatterns = [
    # Todo path tem endereço, sua_view.as_view() e nome
    path('', index.as_view(), name='index'),
    path('diagramaCasoUso/', DiagramaCasoUso.as_view(), name='diagramaCasoUso'),
    path('diagramaClasse/', DiagramaClasse.as_view(), name='diagramaClasse'),
]
