from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views import defaults as default_views
from django.views.generic import TemplateView


urlpatterns = [
    # Django Admin, use {% url 'admin:index' %}
    path(settings.ADMIN_URL, admin.site.urls),

    # User management
    path("users/", include("metrica.users.urls", namespace="users_details")),
    path("accounts/", include("allauth.urls")),

    # Dashboard
    path("", include("metrica.dashboard.urls", namespace="dashboard")),

    # Apps, Pages, UI Kit, and Authentication
    path("apps/", include("apps.urls", namespace="apps")),
    path("pages/", include("pages.urls", namespace="pages")),
    path("uikit/", include("uikit.urls", namespace="uikit")),
    path("authentication/", include("authentication.urls", namespace="authentication")),

    # Browser Reload (Optional for development)
    path("__reload__/", include("django_browser_reload.urls")),

    # Custom URLs
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
