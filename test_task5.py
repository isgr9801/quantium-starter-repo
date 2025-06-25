# test_task5.py
import pytest
from dash import Dash
from dash.test import DashComposite
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
import app


# Fixture to set up the Dash app with a Chrome browser
@pytest.fixture
def dash_app():
    # Configure Chrome options (e.g., headless mode)
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run browser without UI
    chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration
    chrome_options.add_argument("--no-sandbox")  # Disable sandbox for some environments

    # Initialize WebDriver
    browser = Chrome(options=chrome_options)

    # Initialize DashComposite with browser
    dash_composite = DashComposite(app.app, browser=browser)

    yield dash_composite

    # Cleanup: Close browser after tests
    browser.quit()


def test_header_present(dash_app):
    """
    Test that the H1 header is present with the correct text.
    """
    dash_app.start_server()
    dash_app.wait_for_element_by_css_selector("h1")
    header = dash_app.find_element("h1")
    assert header.text == "Soul Foods: Pink Morsels Sales Visualization", "Header text does not match expected"


def test_visualization_present(dash_app):
    """
    Test that the sales graph visualization is present.
    """
    dash_app.start_server()
    dash_app.wait_for_element_by_id("sales-graph")
    graph = dash_app.find_element("#sales-graph")
    assert graph is not None, "Sales graph component not found"


def test_region_picker_present(dash_app):
    """
    Test that the region selector RadioItems component is present with all options.
    """
    dash_app.start_server()
    dash_app.wait_for_element_by_id("region-selector")
    radio_items = dash_app.find_elements("input[name='region-selector']")
    assert len(radio_items) == 5, "Expected 5 region options (All, North, East, South, West)"
    expected_values = ['all', 'north', 'east', 'south', 'west']
    for radio in radio_items:
        assert radio.get_attribute('value') in expected_values, "Unexpected region option value"