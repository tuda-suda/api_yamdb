from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register('', views.UsersViewSet)


urlpatterns = [
    path('auth/email/', views.email_confirmation),
    path('auth/token/', views.token),
    path('users/me/', views.current_user),
    path('users/', include(router.urls))
]