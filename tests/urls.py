"""
URL Configuration for django_custom_error_views
"""

from django.contrib import admin
from django.urls import include, path

from django_custom_error_views.views import handler400 as ui_handler400
from django_custom_error_views.views import handler403 as ui_handler403
from django_custom_error_views.views import handler404 as ui_handler404
from django_custom_error_views.views import handler500 as ui_handler500

handler400 = (
    "django_custom_error_views.views.handler400"  # pylint: disable=invalid-name
)
handler403 = (
    "django_custom_error_views.views.handler403"  # pylint: disable=invalid-name
)
handler404 = (
    "django_custom_error_views.views.handler404"  # pylint: disable=invalid-name
)
handler500 = (
    "django_custom_error_views.views.handler500"  # pylint: disable=invalid-name
)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),
    path("__debug__/", include("debug_toolbar.urls")),
    path(
        "400/",
        ui_handler400,
        kwargs={"exception": Exception("Bad Request!")},
    ),
    path(
        "403/",
        ui_handler403,
        kwargs={"exception": Exception("Permission Denied")},
    ),
    path(
        "404/",
        ui_handler404,
        kwargs={"exception": Exception("Page not Found")},
    ),
    path("500/", ui_handler500),
]
