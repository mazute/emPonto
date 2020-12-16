from django.urls import path

# Importa as views que a gente criou 
from .views import EmpresaCreate, FuncionarioCreate, PontoCreate
from .views import EmpresaUpdate, FuncionarioUpdate, PontoUpdate
from .views import EmpresaDelete, FuncionarioDelete, PontoDelete
from .views import EmpresaList, FuncionarioList, PontoList

# Tem que ser urlpatterns porque é padrão do Django
urlpatterns = [
    # Todo path tem endereço, sua_view.as_view() e nome
    path('cadastrar/empresa', EmpresaCreate.as_view(), name='cadastrar-empresa'),
    path('cadastrar/funcionario', FuncionarioCreate.as_view(), name='cadastrar-funcionario'),
    path('cadastrar/ponto', PontoCreate.as_view(), name='cadastrar-ponto'),

    path('editar/empresa/<int:pk>', EmpresaUpdate.as_view(), name='editar-empresa'),
    path('editar/funcionario/<int:pk>', FuncionarioUpdate.as_view(), name='editar-funcionario'),
    path('editar/ponto/<int:pk>', PontoUpdate.as_view(), name='editar-ponto'),

    path('excluir/empresa/<int:pk>', EmpresaDelete.as_view(), name='excluir-empresa'),
    path('excluir/funcionario/<int:pk>', FuncionarioDelete.as_view(), name='excluir-funcionario'),
    path('excluir/ponto/<int:pk>', PontoDelete.as_view(), name='excluir-ponto'),
    
    path('', EmpresaList.as_view(), name='listar-empresa'),
    path('listar/funcionarios', FuncionarioList.as_view(), name='listar-funcionario'),
    path('listar/pontos', PontoList.as_view(), name='listar-ponto'),

]
