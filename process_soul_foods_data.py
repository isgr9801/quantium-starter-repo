import pandas as pd
import os

files = ["daily_sales_data_0.csv", "daily_sales_data_1.csv", "daily_sales_data_2.csv"]
folder = "data"
output_file = "Soul_Foods-Pink_Morsels-Consolidated.csv"

# empty dataframe
dfs = []

for file in files:
    file_path = os.path.join(folder, file)
    print(f"\nreading file {file}:")

    # Read CSV
    df = pd.read_csv(file_path)

    # Pink Morsel only data accepted
    df_filtered = df[df['product'] == 'pink morsel'].copy()

    if not df_filtered.empty:

        # Clean $ and take first numeric value
        df_filtered['price'] = df_filtered['price'].str.replace(r'\$', '', regex=True).str.split('$').str[0]
        # Convert to numeric
        df_filtered['quantity'] = pd.to_numeric(df_filtered['quantity'], errors='coerce')
        df_filtered['price'] = pd.to_numeric(df_filtered['price'], errors='coerce')

        df_filtered['Sales'] = df_filtered['quantity'] * df_filtered['price'] # sales calculation

        df_filtered = df_filtered[['Sales', 'date', 'region']].rename(
            columns={'date': 'Date', 'region': 'Region'}
        )
        dfs.append(df_filtered)
    else:
        print(f"  No result for pink morsel found")

# consolidated result
if dfs:
    fn_df = pd.concat(dfs, ignore_index=True)
    fn_df.to_csv(output_file, index=False)
    print(f"Final consolidated file '{output_file}'is generated ")
else:
    print("Error: No data to consolidate")