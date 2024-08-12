from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, TelegramUserViewSet

router = DefaultRouter()
router.register(r'tasks', TaskViewSet)
router.register(r'telegram-users', TelegramUserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]