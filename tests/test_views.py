import pytest


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
    assert f'src="/static/django_custom_error_views/visual-{page}.jpg"' in res.content.decode()


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
    settings.DJANGO_ERRORS_UI = {
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
    assert settings.DJANGO_ERRORS_UI[page]["title"] in content
    assert settings.DJANGO_ERRORS_UI[page]["description"] in content
    assert settings.DJANGO_ERRORS_UI[page]["extra_content"] in content
    if settings.DJANGO_ERRORS_UI[page].get("render_exception"):
        assert settings.DJANGO_ERRORS_UI[page]["exception"] in content
