from django.shortcuts import render
from django_filters import rest_framework as d_filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics, mixins, permissions, viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny

from users.permissions import IsAdmin

from .filters import TitleFilter
from .models import Category, Genre, Title
from .serializers import (CategorySerializer, GenreSerializer,
                          TitleDetailSerializer, TitleSerializer)


class CategoryViewSet(mixins.CreateModelMixin,
                      mixins.ListModelMixin,
                      mixins.DestroyModelMixin,
                      viewsets.GenericViewSet):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes_by_action = {
        'create': (IsAdmin,),
        'list': (AllowAny,),
        'destroy': (IsAdmin,)}
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
    lookup_field = ('slug')


class GenreViewSet(mixins.CreateModelMixin,
                   mixins.ListModelMixin,
                   mixins.DestroyModelMixin,
                   viewsets.GenericViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes_by_action = {
        'create': (IsAdmin,),
        'list': (AllowAny,),
        'destroy': (IsAdmin,)}
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
    lookup_field = ('slug')


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    permission_classes_by_action = {
        'create': (IsAdmin,),
        'list': (AllowAny,),
        'destroy': (IsAdmin,),
        'partial_update': (IsAdmin,)}
    filter_backends = (d_filters.DjangoFilterBackend,)
    filterset_class = TitleFilter

    def get_serializer_class(self):
        if self.action == 'create' or self.action == 'partial_update':
            return TitleSerializer
        else:
            return TitleDetailSerializer
