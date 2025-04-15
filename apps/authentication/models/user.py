from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.transaction import atomic

from apps.authentication.models.organization import Organization
from apps.authentication.models.user_organization import UserOrganization
from apps.portal.models import Page


class UserManager(BaseUserManager):

    @atomic
    def create_superuser(self, username: str, password: str, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        organization, _ = Organization.objects.get_or_create(name='MASTER')
        user = self.model(username=username, current_organization=organization, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        UserOrganization.objects.create(user=user, organization=organization)

        Page.objects.get_or_create(organization=organization, position=0, defaults={'title': 'HOME'})

        return user


class User(AbstractUser):
    current_organization = models.ForeignKey(Organization, on_delete=models.DO_NOTHING)
    organizations = models.ManyToManyField('Organization', through='UserOrganization', related_name='users')
    objects = UserManager()

    class Meta:
        ordering = ['username']
