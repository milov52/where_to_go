from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Place(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название места')
    placeId = models.SlugField()
    description_short = models.TextField(verbose_name='Краткое описание')
    description_long = models.TextField(verbose_name='Полное описание')
    coord_lng = models.FloatField(
        verbose_name='Долгота',
        validators=[MinValueValidator(-90.0), MaxValueValidator(90.0)]
    )
    coord_lat = models.FloatField(
        verbose_name='Широта',
        validators=[MinValueValidator(-90.0), MaxValueValidator(90.0)]
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Место"
        verbose_name_plural = "Места"
        ordering = ['placeId']


class Image(models.Model):
    position = models.PositiveSmallIntegerField(verbose_name='Позиция', default=0, blank=False, null=False)
    place_image = models.ImageField(upload_to='places', blank=True, verbose_name='Картинка')
    places = models.ForeignKey(Place, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.position} {self.places}"

    class Meta:
        verbose_name = "Фотография"
        verbose_name_plural = "Фотографии"
        ordering = ['position']
