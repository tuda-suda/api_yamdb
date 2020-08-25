from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CategoryViewSet, GenreViewSet, TitleViewSet

router = DefaultRouter()

router.register(r'titles', TitleViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('categories/', CategoryViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('categories/<slug:slug>/', CategoryViewSet.as_view({'delete': 'destroy'})),
    path('genres/', GenreViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('genres/<slug:slug>/', GenreViewSet.as_view({'delete': 'destroy'})),
]
