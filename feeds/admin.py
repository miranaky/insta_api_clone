from django.contrib import admin
from . import models


@admin.register(models.Feed)
class FeedAdmin(admin.ModelAdmin):
    "Feed Admin Config"

    pass


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    """ Photo Admin Config"""

    pass
