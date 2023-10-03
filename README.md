# Django Custom Error Views

Prebuilt and customizable error views for Django.

* [Features](#features)
* [Installation](#installation)
* [Screenshots](#screenshots)

## Features

* Responsive design suitable for device sizes from mobile to desktop

## Installation

```sh
pip install django-custom-error-views
```

```python
INSTALLED_APPS = [
    "django_custom_error_views",
]
```

Now Django will by default use the templates for 400, 403, 404 and 500 pages.

### Customizing Error Pages

To customize the error pages you need to add a custom handler that injects context into the templates. Add the below snippet to your `urls.py`

```py
from django_custom_error_views.views import handler400 as ui_handler400
from django_custom_error_views.views import handler403 as ui_handler403
from django_custom_error_views.views import handler404 as ui_handler404
from django_custom_error_views.views import handler500 as ui_handler500

handler400 = "django_custom_error_views.views.handler400"
handler403 = "django_custom_error_views.views.handler403"
handler404 = "django_custom_error_views.views.handler404"
handler500 = "django_custom_error_views.views.handler500"
```

And then you can add the following settings for each page.

```py
DJANGO_CUSTOM_ERROR_VIEWS = {
    "400": {
        "title": "Custom 400 error.",
        "description": "Custom 400 description.",
        "extra_content": "400 extras.",
    },
    "403": {
        "title": "Custom 403 Error.",
        "description": "Custom 403 description.",
        "extra_content": "403 extras.",
        "render_exception": True,
    },
    "404": {
        "title": "Custom 404 Error.",
        "description": "Custom 404 description.",
        "extra_content": "404 extras.",
        "render_exception": True,
    },
    "500": {
        "title": "Custom 500 Error.",
        "description": "Custom 500 description.",
        "extra_content": "500 extras.",
    },
}
```

Each option does the following:

- `title` - Changes the title for the page to a custom one.
- `description` - Changes the description for the error to a custom one.
- `extra_content` - Adds extra text to the page below the title and description.
- `render_exception` - Renders the exception that occurred in the page (only for 403/404 pages), by default it's hidden.


## Preview

You can preview the error pages live at:

- [400 HTTP status code](https://hodovi.cc/400)
- [403 HTTP status code](https://hodovi.cc/403)
- [404 HTTP status code](https://hodovi.cc/404)
- [500 HTTP status code](https://hodovi.cc/500)
