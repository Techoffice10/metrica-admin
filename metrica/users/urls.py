from django.urls import path

from metrica.users.views import (
    user_detail_view,
    user_redirect_view,
    user_update_view,
    user_list,  # Ensure `user_list` is imported
)

app_name = "users_details"

urlpatterns = [
    # Redirect, Update, and Detail
    path("~redirect/", view=user_redirect_view, name="redirect"),
    path("~update/", view=user_update_view, name="update"),
    path("<str:username>/", view=user_detail_view, name="detail"),

    # Mapping the user_list view to a URL (users.html)
    path("users/", user_list, name="user_list"),
]
