from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjUserAdmin
from django.utils.translation import gettext_lazy as _

from main import models


@admin.register(models.User)
class UserAdmin(DjUserAdmin):
    list_display = (
        'email',
    )
    fieldsets = (
        (None, {"fields": ("password",)}),
        (_("Personal info"), {"fields": ("email",)}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    search_fields = ("email",)
    ordering = ("email",)

