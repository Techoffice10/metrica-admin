from django.contrib.auth import forms as admin_forms
from django.contrib.auth import get_user_model
from django import forms
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class UserChangeForm(admin_forms.UserChangeForm):
    """Form for updating an existing user."""
    class Meta(admin_forms.UserChangeForm.Meta):
        model = User
        fields = [
            "full_name", "phone_no", "alt_no", "company", "service_type", 
            "location", "user_name", "port_no", "rdp_password", "node", 
            "internal_ip", "email", "email_password", "pb_id", "pb_password", 
            "branch", "ext_no", "notes", "status"
        ]


class UserCreationForm(admin_forms.UserCreationForm):
    """Form for creating a new user."""
    class Meta(admin_forms.UserCreationForm.Meta):
        model = User
        fields = [
            "full_name", "phone_no", "alt_no", "company", "service_type", 
            "location", "user_name", "port_no", "rdp_password", "node", 
            "internal_ip", "email", "email_password", "pb_id", "pb_password", 
            "branch", "ext_no", "notes", "status"
        ]
        error_messages = {
            "user_name": {"unique": _("This username has already been taken.")},
            "email": {"unique": _("A user with this email already exists.")},
        }


class UserForm(forms.ModelForm):
    """Form for creating or updating user records."""
    class Meta:
        model = User
        fields = [
            "full_name", "phone_no", "alt_no", "company", "service_type", 
            "location", "user_name", "port_no", "rdp_password", "node", 
            "internal_ip", "email", "email_password", "pb_id", "pb_password", 
            "branch", "ext_no", "notes", "status"
        ]
        widgets = {
            "notes": forms.Textarea(attrs={"rows": 3, "placeholder": "Enter additional notes here..."}),
            "status": forms.Select(choices=[("Active", "Active"), ("Deactivated", "Deactivated")]),
        }
