from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

# Register your models here.

# @admin~ = decorater: same as admin.site.register(models.User, CustomUserAdmin)


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    """ Custom User Admin """

    pass
