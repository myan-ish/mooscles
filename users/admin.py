from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "date_joined",
        "last_login",
        "is_superuser",
        "username",
        "first_name",
        "last_name",
        "is_active",
    )
    list_filter = (
        "date_joined",
        "last_login",
        "is_superuser",
    )
    raw_id_fields = (
        "groups",
        "user_permissions",
    )
