import pytest
import sys
import os
from dash.testing.application_runners import import_app

# Add the parent directory of tests/ to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

@pytest.fixture
def dash_app():
    app = import_app("app")  # Refers to app.py
    return app.app

# Test 1: Header is present
def test_header_present(dash_duo, dash_app):
    dash_duo.start_server(dash_app)
    header = dash_duo.find_element("h1")
    assert "Soul Foods: Pink Morsels Sales Visualization" in header.text

# Test 2: Graph is present
def test_graph_present(dash_duo, dash_app):
    dash_duo.start_server(dash_app)
    graph = dash_duo.find_element("div.js-plotly-plot")
    assert graph is not None

# Test 3: Region picker is present
def test_region_picker_present(dash_duo, dash_app):
    dash_duo.start_server(dash_app)
    region_picker = dash_duo.find_element("#region-selector")
    assert region_picker is not None