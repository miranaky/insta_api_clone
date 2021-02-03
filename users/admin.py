from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):
    """Custom User Admin """

    list_display = ("username", "gender", "verified_badge", "phone_number", "email", "website")
    list_filter = ("gender", "verified_badge")

    fieldsets = (
        UserAdmin.fieldsets[0],
        UserAdmin.fieldsets[1],
        (
            "Custom Fields",
            {
                "fields": (
                    "avatar",
                    "bio",
                    "website",
                    "phone_number",
                    "gender",
                    "verified_badge",
                ),
            },
        ),
    )