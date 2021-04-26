from django.conf import settings
from django.db import models


# Create your models here.


class Item(models.Model):
    """"Комплекты подарков"""
    title = models.CharField("Название", max_length=50, unique=True)
    description = models.TextField("Описание")
    image = models.ImageField("Картинка", upload_to=settings.MEDIA_ITEM_IMAGE_DIR, null=True,)
    weight = models.PositiveSmallIntegerField("Вес в граммах")
    price = models.DecimalField("Цена в рублях", max_digits=8, decimal_places=2)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Комплект подарков"
        verbose_name_plural = "Комплекты подарков"
