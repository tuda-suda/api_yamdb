from rest_framework import serializers

from .models import Category, Genre, Title


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('name', 'slug')
        model = Category


class CategoryField(serializers.SlugRelatedField):
    def to_representation(self, value):
        serializer = CategorySerializer(value)
        return serializer.data


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('name', 'slug')
        model = Genre


class GenreField(serializers.SlugRelatedField):
    def to_representation(self, value):
        serializer = GenreSerializer(value)
        return serializer.data


class TitleSerializer(serializers.ModelSerializer):
    category = CategoryField(
        slug_field='slug', queryset=Category.objects.all())
    genre = GenreField(
        slug_field='slug', queryset=Genre.objects.all(), many=True)

    class Meta:
        fields = '__all__'
        model = Title
