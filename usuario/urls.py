from django.urls import path, include
from rest_framework import routers

from usuario.views import CadastroView
from usuario.api.viewsets import UsuarioViewSet, CriarUsuarioViewSet, ChangePasswordView

router = routers.DefaultRouter()
router.register('usuarios', UsuarioViewSet)
router.register('cadastro', CriarUsuarioViewSet)

urlpatterns = [
    path('api/', include(router.urls), ),
    path('novo/', CadastroView.as_view(), name='cadastro', ),
    path('mudar-senha/', ChangePasswordView.as_view(), name='change-password'),
]
