from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import CharField, TextField, DateTimeField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """Custom User model for Metrica with additional fields."""
    
    # Replacing first and last name with a unified full name field
    full_name = models.CharField(max_length=255, blank=True, null=True)
    first_name = None  # type: ignore
    last_name = None  # type: ignore

    # Additional user fields
    phone_no = models.CharField(max_length=15, blank=True, null=True, verbose_name="Phone Number")
    alt_no = models.CharField(max_length=15, blank=True, null=True, verbose_name="Alternate Number")
    company = models.CharField(max_length=255, blank=True, null=True)
    service_type = models.CharField(max_length=100, blank=True, null=True, verbose_name="Service Type")
    location = models.CharField(max_length=255, blank=True, null=True)
    user_name = models.CharField(max_length=255, unique=True, null=True, blank=True, default='default_user_name')
    port_no = models.CharField(max_length=50, blank=True, null=True, verbose_name="Port Number")
    rdp_password = models.CharField(max_length=255, blank=True, null=True, verbose_name="RDP Password")
    node = models.CharField(max_length=100, blank=True, null=True)
    internal_ip = models.GenericIPAddressField(blank=True, null=True, verbose_name="Internal IP")
    email = models.EmailField(_("Email Address"), unique=True)
    email_password = models.CharField(max_length=255, blank=True, null=True, verbose_name="Email Password")
    pb_id = models.CharField(max_length=50, blank=True, null=True, verbose_name="PB ID")
    pb_password = models.CharField(max_length=255, blank=True, null=True, verbose_name="PB Password")
    branch = models.CharField(max_length=255, blank=True, null=True)
    ext_no = models.CharField(max_length=10, blank=True, null=True, verbose_name="Extension Number")
    notes = TextField(blank=True, null=True)
    user_creation_date = DateTimeField(auto_now_add=True, verbose_name="User Creation Date")
    status = models.CharField(
        max_length=50,
        choices=[("Active", "Active"), ("Deactivated", "Deactivated")],
        default="Active",
    )
    profile_picture = models.ImageField(
        upload_to="images/users/",
        default="images/users/default.jpg",
        blank=True,
        null=True,
    )

    class Meta:
        app_label = 'users'  # Explicitly set app_label to 'users'

    def get_absolute_url(self):
        """Get URL for user's detail view."""
        return reverse("users:detail", kwargs={"username": self.user_name})

    def __str__(self):
        """Return the full name if available, else the username."""
        return self.full_name or self.user_name
