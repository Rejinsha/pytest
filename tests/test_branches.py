import pytest

BRANCHES_URL = "/in/branches"

@pytest.mark.smoke

def test_branches_url(page, app_config):
    page.goto(app_config.base_url + BRANCHES_URL)
    page_title = page.title()
    assert page_title == "Akbartravels -"
