from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

class Category(models.Model):
    name = models.CharField(verbose_name='Категория', max_length=50)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Категории'


class Genre(models.Model):
    name = models.CharField(verbose_name='Жанр', max_length=50)
    slug = models.SlugField(unique=True, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Жанры'


class Title(models.Model):
    name = models.CharField(verbose_name='Название', max_length=250)
    year = models.PositiveIntegerField(
        verbose_name='Год выпуска', 
        null=True, 
        blank=True
    )
    rating = models.PositiveIntegerField(
        verbose_name='Рейтинг на основе отзывов', 
        null=True, 
        blank=True
    )
    description = models.TextField(
        verbose_name='Описание', 
        null=True, 
        blank=True
    )
    genre = models.ManyToManyField(
        Genre, 
        verbose_name='Жанр', 
        related_name='genre_titles', 
        null=True,
        blank=True
    )
    category = models.ForeignKey(
        Category, 
        related_name='category_titles', 
        on_delete=models.DO_NOTHING,
        null=True, blank=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Произведения"
        ordering = ['-id']


class Review(models.Model):
    text = models.TextField(verbose_name='Текст отзыва', null=True, blank=True)
    author = models.ForeignKey(
        User, 
        related_name='reviews', 
        null=False,
        on_delete=models.CASCADE
    )
    score = models.PositiveSmallIntegerField(verbose_name='Оценка', null=False)
    pub_date = models.DateTimeField(
        verbose_name='Дата отзыва',
        auto_now_add=True
    )
    title = models.ForeignKey(
        Title, 
        related_name='reviews', 
        null=False,
        verbose_name='Произведение',
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name_plural = "Отзывы"
        ordering = ['-score']


class Comment(models.Model):
    text = models.TextField(
        verbose_name='Текст комментария', 
        null=False,
        blank=True
    )
    author = models.ForeignKey(
        User, 
        related_name='comments', 
        null=False,
        on_delete=models.CASCADE
    )
    pub_date = models.DateTimeField(
        verbose_name='Дата комментария',
        auto_now_add=True
    )
    review = models.ForeignKey(
        Review, 
        related_name='comments', 
        null=False,
        verbose_name='Отзыв',
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name_plural = "Комментарии"
        ordering = ['-pub_date']
