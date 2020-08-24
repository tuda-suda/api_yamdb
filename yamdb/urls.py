from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CategoryViewSet, GenreViewSet, TitleViewSet

router = DefaultRouter()

router.register(r'titles', TitleViewSet)

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/category/', CategoryViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('v1/category/<slug:slug>/', CategoryViewSet.as_view({'delete': 'destroy'})),
    path('v1/genres/', GenreViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('v1/genres/<slug:slug>/', GenreViewSet.as_view({'delete': 'destroy'})),
]
