from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.views import defaults as default_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
    path("__debug__/", include("debug_toolbar.urls")),
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
