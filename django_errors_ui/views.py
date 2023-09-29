from urllib.parse import quote

from django.conf import settings
from django.http import (
    HttpResponseBadRequest,
    HttpResponseForbidden,
    HttpResponseNotFound,
    HttpResponseServerError,
)
from django.template import loader
from django.views.decorators.csrf import requires_csrf_token

ERROR_404_TEMPLATE_NAME = "404.html"
ERROR_403_TEMPLATE_NAME = "403.html"
ERROR_400_TEMPLATE_NAME = "400.html"
ERROR_500_TEMPLATE_NAME = "500.html"

custom_settings = getattr(settings, "DJANGO_ERRORS_UI", None)


@requires_csrf_token
def handler404(request, exception, template_name=ERROR_404_TEMPLATE_NAME):
    """
    Default 404 handler.

    Templates: :template:`404.html`
    Context:
        request_path
            The path of the requested URL (e.g., '/app/pages/bad_page/'). It's
            quoted to prevent a content injection attack.
        exception
            The message from the exception which triggered the 404 (if one was
            supplied), or the exception class name
    """
    exception_repr = exception.__class__.__name__
    # Try to get an "interesting" exception message, if any (and not the ugly
    # Resolver404 dictionary)
    try:
        message = exception.args[0]
    except (AttributeError, IndexError):
        pass
    else:
        if isinstance(message, str):
            exception_repr = message

    context = {
        "request_path": quote(request.path),
        "exception": exception_repr,
    }

    if custom_settings:
        settings_404 = custom_settings.get("404")
        if settings_404:
            title = settings_404.get("title")
            if title:
                context["title"] = title
            description = settings_404.get("description")
            if description:
                context["description"] = description
            extra_content = settings_404.get("extra_content")
            if extra_content:
                context["extra_content"] = extra_content

    template = loader.get_template(template_name)
    body = template.render(context, request)
    return HttpResponseNotFound(body)


@requires_csrf_token
def handler500(request, template_name=ERROR_500_TEMPLATE_NAME):
    """
    500 error handler.
    """
    template = loader.get_template(template_name)
    return HttpResponseServerError(template.render())


@requires_csrf_token
def handler400(request, exception, template_name=ERROR_400_TEMPLATE_NAME):
    """
    400 error handler.
    """
    template = loader.get_template(template_name)
    # No exception content is passed to the template, to not disclose any
    # sensitive information.
    return HttpResponseBadRequest(template.render())


@requires_csrf_token
def handler403(request, exception, template_name=ERROR_403_TEMPLATE_NAME):
    """
    Permission denied (403) handler.

    Templates: :template:`403.html`
    Context:
        exception
            The message from the exception which triggered the 403 (if one was
            supplied).
    """
    template = loader.get_template(template_name)
    return HttpResponseForbidden(
        template.render(request=request, context={"exception": str(exception)})
    )
