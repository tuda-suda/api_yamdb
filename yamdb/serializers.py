from rest_framework import serializers

from .models import Category, Genre, Title


class DynamicFieldsModelSerializer(serializers.ModelSerializer):

    def __init__(self, *args, **kwargs):
        self.extra_fields = kwargs.pop('fields', None)
        self.extra_exclude = kwargs.pop('exclude', None)

        super(DynamicFieldsModelSerializer, self).__init__(*args, **kwargs)

        if self.extra_fields is not None:
            allowed = set(self.extra_fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)

        if self.extra_exclude is not None:
            not_allowed = set(self.extra_exclude)
            for exclude_name in not_allowed:
                self.fields.pop(exclude_name)


class CategorySerializer(DynamicFieldsModelSerializer):

    class Meta:
        fields = '__all__'
        model = Category


class GenreSerializer(DynamicFieldsModelSerializer):

    class Meta:
        fields = '__all__'
        model = Genre


class TitleSerializer(serializers.ModelSerializer):
    category = CategorySerializer(Category, exclude=['id'], read_only=True)
    genre = GenreSerializer(Genre, exclude=['id'], many=True, read_only=True)

    class Meta:
        fields = '__all__'
        model = Title
