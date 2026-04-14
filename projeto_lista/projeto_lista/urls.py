from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.api_views import TarefaViewSet, CategoriaViewSet, PrioridadeViewSet

router = DefaultRouter()
router.register(r'tarefas', TarefaViewSet)
router.register(r'categorias', CategoriaViewSet)
router.register(r'prioridades', PrioridadeViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('', include('core.urls')),
]