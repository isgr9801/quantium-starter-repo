import sys
import os
import pandas as pd


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import app, df


#Test region filtering
def test_region_filtering():
    print("\nRunning region filtering test...")
    test_region = 'south'
    filtered_df = df[df['Region'].str.lower() == test_region]
    agg = filtered_df.groupby('Date')['Sales'].sum().reset_index()

    assert not agg.empty, "Aggregated data for 'south' should not be empty"
    print("Region filtering and aggregation logic passed.")


# Test date parsing and sorting
def test_date_handling():
    print("\nRunning date parsing test...")
    assert pd.api.types.is_datetime64_any_dtype(df['Date']), "Date column is not in datetime format"
    assert df['Date'].is_monotonic_increasing, "Dates are not sorted"
    print("Date parsing and sorting passed.")

def test_layout_structure():
    print("\nRunning Dash layout test...")
    layout = app.layout

    assert hasattr(layout, 'children'), "Layout should have children elements"
    h1 = layout.children[0]
    assert h1.children.startswith("Soul Foods"), "H1 tag missing or incorrect"
    print("Layout structure looks good.")


# Simulating callback logic
def simulate_callback(region='north'):
    print(f"\nSimulating callback for region: {region}")
    if region == 'all':
        region_df = df.copy()
    else:
        region_df = df[df['Region'].str.lower() == region]

    df_agg = region_df.groupby('Date')['Sales'].sum().reset_index()
    assert not df_agg.empty, f"Callback simulation failed for region: {region}"


# manual test run
if __name__ == "__main__":
    test_region_filtering()
    test_date_handling()
    test_layout_structure()
    simulate_callback('north')
    simulate_callback('east')
    simulate_callback('all')
