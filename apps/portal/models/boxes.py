from django.contrib.auth.models import Permission
from django.core import validators
from django.db import models
from model_utils.managers import InheritanceManager


class CustomQuerySet(models.QuerySet):
    pass


class Manager(InheritanceManager):

    def get_queryset(self):
        return CustomQuerySet(model=self.model, using=self._db)


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
    permission = models.ForeignKey(Permission, on_delete=models.DO_NOTHING, null=True, blank=True)

    objects = InheritanceManager()

    class Meta:
        ordering = ('position',)

    def __str__(self):
        return f'{self.__class__.__name__}: {self.id} {self.name}'


class ImageBox(Box):
    image = models.FileField(upload_to='image-box')


class LinkBox(ImageBox):
    link = models.CharField(max_length=1024)
    new_window = models.BooleanField(default=False)


class HtmlBox(Box):
    html = models.TextField()
    color = models.CharField(max_length=255, null=True)
