from rest_framework import serializers

from .models import Category, Genre, Title


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        exclude = ('id',)
        model = Category


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        exclude = ('id',)
        model = Genre


class TitleSerializer(serializers.ModelSerializer):
    category = CategorySerializer(Category,  read_only=True)
    genre = GenreSerializer(Genre, many=True, read_only=True)

    class Meta:
        fields = '__all__'
        model = Title
