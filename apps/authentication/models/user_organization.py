from django.db import models


class UserOrganization(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    organization = models.ForeignKey('Organization', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user} <-> {self.organization.name}'

    class Meta:
        ordering = ['user__username', 'organization__name']
        unique_together = ('user', 'organization')
