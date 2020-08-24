from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register('', views.UsersViewSet)


urlpatterns = [
    path('auth/email/', views.email_confirmation, name='token_obtain_pair'),
    path('auth/token/', views.token, name='token'),
    path('users/me/', views.UserOwnView.as_view(), name='current_user_profile'),
    path('users/', include(router.urls))
]