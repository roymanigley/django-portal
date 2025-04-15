from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from apps.authentication.models import User, Organization, UserOrganization

admin.site.register(User, UserAdmin)
admin.site.register(Organization)
admin.site.register(UserOrganization)
