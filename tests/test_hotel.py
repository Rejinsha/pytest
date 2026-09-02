import pytest

HOTEL_URL = "/in/cheap-hotels/"

@pytest.mark.smoke
def test_hotel_url(page, app_config):
    page.goto(app_config.base_url + HOTEL_URL, wait_until="domcontentloaded")
    page_title = page.title()
    assert page_title == "Cheap Flights ; Domestic ; International Flight Offers in India"