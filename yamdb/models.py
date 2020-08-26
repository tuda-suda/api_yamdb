from django.db import models


class Category(models.Model):
    name = models.CharField(verbose_name='Категория', max_length=50)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Категории"


class Genre(models.Model):
    name = models.CharField(verbose_name='Жанр', max_length=50)
    slug = models.SlugField(unique=True, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Жанры"


class Title(models.Model):
    name = models.CharField(verbose_name='Название', max_length=250)
    year = models.PositiveIntegerField(
        verbose_name='Год выпуска', null=True, blank=True)
    rating = models.PositiveIntegerField(
        verbose_name='Рейтинг на основе отзывов', null=True, blank=True)
    description = models.TextField(
        verbose_name='Описание', null=True, blank=True)
    genre = models.ManyToManyField(
        Genre, verbose_name='Жанр', related_name='genre_titles', null=True,
        blank=True)
    category = models.ForeignKey(
        Category, related_name='category_titles', on_delete=models.DO_NOTHING,
        null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Произведения"
        ordering = ['-id']
