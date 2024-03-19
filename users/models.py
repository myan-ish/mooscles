from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
)
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=256, default="")
    last_name = models.CharField(max_length=256, default="")

    username = models.CharField(
        _("username"),
        max_length=250,
        unique=True,
        help_text=_(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )

    email = models.EmailField(
        _("email address"),
        help_text=_("Required. Inform a valid email address."),
        error_messages={
            "unique": _("A user with that email already exists."),
        },
        blank=True,
        null=True,
        )
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_(
            "Designates whether the user can log into this admin site."
        ),
    )

    date_joined = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "username"

    objects = UserManager()

    def __str__(self):
        return self.get_username()

    @property
    def full_name(self):
        return self.first_name + " " + self.last_name
