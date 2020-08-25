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
    category = serializers.SlugRelatedField(slug_field='slug',queryset=Category.objects.all())
    # genre = serializers.SlugRelatedField(slug_field='slug',queryset=Genre.objects.all())
    # genre = GenreSerializer(source="tag",read_only=True,  many=True)

    class Meta:
        fields = '__all__'
        model = Title
        # depth = 1

    # def create(self, validated_data):

    #     # categories_data = validated_data.get('category')
    #     genries_data = validated_data.get('genre')
    #     print(validated_data)

    #     title = Title.objects.create(**validated_data)
    #     # category_data = Category.objects.get(slug=categories_data['slug'])
    #     # title.category = category_data
    #     for genre_data in genries_data:

    #         genre = Genre.objects.get(slug=genre_data['slug'])
    #         title.genre.add(genre)
    #     return title
