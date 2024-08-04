from django.db import models
from django.core import validators
from model_utils.managers import InheritanceManager


class Page(models.Model):
    org_id = models.IntegerField()
    position = models.IntegerField()


class Box(models.Model):
    name = models.CharField(max_length=255)
    position = models.PositiveIntegerField()
    width = models.IntegerField(
        validators=[validators.MinValueValidator(1),
                    validators.MaxValueValidator(12)]
    )
    height = models.IntegerField(
        validators=[validators.MinValueValidator(1),
                    validators.MaxValueValidator(12)]
    )

    page = models.ForeignKey(
        'Page', on_delete=models.CASCADE, related_name='boxes'
    )

    objects = InheritanceManager()

    class Meta:
        ordering = ('position', )


class ImageBox(Box):
    image = models.FileField(upload_to='image-box')


class LinkBox(ImageBox):
    link = models.CharField(max_length=1024)


class HtmlBox(Box):
    html = models.TextField()
