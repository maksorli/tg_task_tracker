from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, TelegramUserViewSet
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

router = DefaultRouter()
router.register(r'tasks', TaskViewSet)
router.register(r'telegram-users', TelegramUserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path("schema/swagger-ui/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),   
]
