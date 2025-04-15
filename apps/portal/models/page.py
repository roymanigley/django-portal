from django.db import models

from apps.authentication.models import Organization


class CustomQuerySet(models.QuerySet):

    def get_by_org_id(self, *, org_id: int) -> 'CustomQuerySet':
        return self.filter(
            organization_id=org_id
        )

    def get_by_org_id_with_boxes(self, *, org_id: int) -> 'CustomQuerySet':
        return self.filter(
            organization_id=org_id
        ).prefetch_related(
            'boxes',
        )

    def get_by_id_with_boxes(self, *, id: int) -> 'CustomQuerySet':
        return self.filter(
            id=id
        ).prefetch_related(
            'boxes',
        )


class Manager(models.Manager):

    def get_queryset(self):
        return CustomQuerySet(model=self.model, using=self._db)

    def get_by_org_id(self, *, org_id: int) -> CustomQuerySet['Page']:
        return self.get_queryset().get_by_org_id(org_id=org_id)

    def get_by_org_id_with_boxes(self, *, org_id: int) -> CustomQuerySet['Page']:
        return self.get_queryset().get_by_org_id_with_boxes(org_id=org_id)

    def get_by_id_with_boxes(self, *, id: int, org_id: int) -> 'Page':
        return self.get_queryset().get_by_org_id(org_id=org_id).get_by_id_with_boxes(id=id).first()


class Page(models.Model):
    title = models.CharField(max_length=255)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    position = models.IntegerField(default=0)

    objects = Manager()

    def __str__(self):
        return f'{self.title} - {self.organization.name} - {self.position}'

    class Meta:
        ordering = ['position']
