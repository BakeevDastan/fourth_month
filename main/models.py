from django.db import models


class Genre(models.Model):
    class Meta:
        verbose_name = 'жанр'
        verbose_name_plural = 'жанры'
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Films(models.Model):
    class Meta:
        verbose_name = 'фильм'
        verbose_name_plural = 'фильмы'
    image = models.ImageField(null=True, upload_to='films', verbose_name='картинки')
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT, null=True, verbose_name='жанры')
    name = models.CharField(max_length=100, verbose_name='Имя')
    producer = models.CharField(max_length=100, verbose_name='Режисёр')
    rating = models.FloatField(default=0, verbose_name='Рейтинг')
    duration = models.DurationField(default=0, verbose_name='Длительность')

    def __str__(self):
        return self.name


class Review(models.Model):
    class Meta:
        verbose_name = 'отзыв'
        verbose_name_plural = 'отзывы'
    films = models.ForeignKey(Films, on_delete=models.CASCADE, null=True, verbose_name='Список фильмов')
    film = models.CharField(max_length=100, verbose_name='фильм')
    text = models.TextField(verbose_name='Текст')

    def __str__(self):
        return self.film

