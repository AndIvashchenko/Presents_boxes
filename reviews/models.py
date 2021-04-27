from django.conf import settings
from django.db import models

# Create your models here.


class Review(models.Model):
    """Отзывы"""
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="Автор", on_delete=models.PROTECT, related_name='review',)
    text = models.TextField("Текст отзыва")
    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField(null=True, blank = True)
    STATUS_CHOICES = [
        ("new", 'на модерации'),
        ("published", 'опубликован'),
        ("hidden", 'отклонен'),
    ]
    status = models.CharField("Статус", max_length=10, choices=STATUS_CHOICES, default="new",)

    def __str__(self):
        return f'Отзыв от {self.author}'

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
