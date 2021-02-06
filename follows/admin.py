from django.contrib import admin
from . import models


@admin.register(models.Following)
class FollowingAdmin(admin.ModelAdmin):
    """ Following Admin Config """

    pass


@admin.register(models.Follower)
class FollowerAdmin(admin.ModelAdmin):
    """ Follower Admin Config """

    pass
