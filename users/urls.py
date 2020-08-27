from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register('', views.UserViewSet)


urlpatterns = [
    path('auth/email/', views.EmailSignUpView, name='token_obtain_pair'),
    path('auth/token/', views.CodeConfirmationView, name='token'),
    path('users/me/', views.UserOwnView.as_view(), name='current_user_profile'),
    path('users/', include(router.urls))
]
