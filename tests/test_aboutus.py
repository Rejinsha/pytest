import pytest

ABOUTUS_URL = "/in/about-us"

@pytest.mark.smoke

def test_aboutus_url(page, app_config):
    page.goto(app_config.base_url + ABOUTUS_URL)
    page_title = page.title()
    assert page_title == "Akbartravels -"
