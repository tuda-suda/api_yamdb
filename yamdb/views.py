from django.shortcuts import render
from rest_framework import filters, generics, mixins, permissions, viewsets
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly

from .models import Category, Genre, Title
from .serializers import CategorySerializer, GenreSerializer, TitleSerializer


class CategoryViewSet(mixins.CreateModelMixin,
                      mixins.ListModelMixin,
                      mixins.DestroyModelMixin,
                      viewsets.GenericViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny, ]
    lookup_field = ('slug')


class GenreViewSet(mixins.CreateModelMixin,
                   mixins.ListModelMixin,
                   mixins.DestroyModelMixin,
                   viewsets.GenericViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [AllowAny, ]
    lookup_field = ('slug')


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer
    permission_classes = [AllowAny, ]
