from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

from usuario.api.viewsets import ChangePasswordView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuario', include('usuario.urls')),
    path('login/', obtain_auth_token),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
