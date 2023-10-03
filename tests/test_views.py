import pytest

from django_custom_error_views.views import extract_settings


def test_extract_settings(settings):
    settings.DJANGO_CUSTOM_ERROR_VIEWS = {
        "400": {
            "title": "Custom 400 error.",
            "description": "Custom 400 description.",
        },
        "403": {"extra_content": "403 extras.", "render_exception": True},
        "404": {},
    }

    assert extract_settings("400") == {
        "title": "Custom 400 error.",
        "description": "Custom 400 description.",
    }

    assert extract_settings("403") == {
        "extra_content": "403 extras.",
        "render_exception": True,
    }

    assert not extract_settings("404")


@pytest.mark.parametrize(
    "page",
    [
        "400",
        "403",
        "404",
        "500",
    ],
)
def test_error_views(page, client):
    res = client.get(f"/{page}/")
    assert res.status_code == int(page)
    assert res.templates[0].name == f"{page}.html"
    assert (
        f'src="/static/django_custom_error_views/visual-{page}.jpg"'
        in res.content.decode()
    )


@pytest.mark.parametrize(
    "page",
    [
        "400",
        "403",
        "404",
        "500",
    ],
)
def test_error_views_settings(page, client, settings):
    settings.DJANGO_CUSTOM_ERROR_VIEWS = {
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
            "exception": "Permission Denied",
        },
        "404": {
            "title": "Custom 404 Error.",
            "description": "Custom 404 description.",
            "extra_content": "404 extras.",
            "render_exception": True,
            "exception": "Page not Found",
        },
        "500": {
            "title": "Custom 500 Error.",
            "description": "Custom 500 description.",
            "extra_content": "500 extras.",
        },
    }

    res = client.get(f"/{page}/")
    assert res.status_code == int(page)
    assert res.templates[0].name == f"{page}.html"

    content = res.content.decode()
    assert f'src="/static/django_custom_error_views/visual-{page}.jpg"' in content
    assert settings.DJANGO_CUSTOM_ERROR_VIEWS[page]["title"] in content
    assert settings.DJANGO_CUSTOM_ERROR_VIEWS[page]["description"] in content
    assert settings.DJANGO_CUSTOM_ERROR_VIEWS[page]["extra_content"] in content
    if settings.DJANGO_CUSTOM_ERROR_VIEWS[page].get("render_exception"):
        assert settings.DJANGO_CUSTOM_ERROR_VIEWS[page]["exception"] in content
