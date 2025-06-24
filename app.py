import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html

df = pd.read_csv('Soul_Foods-Pink_Morsels-Consolidated.csv')

df['Date'] = pd.to_datetime(df['Date'], errors='coerce')  # Convert Date to datetime
df = df.sort_values('Date')
df_agg = df.groupby('Date')['Sales'].sum().reset_index()  # Sum sales by date


# line chart
fig = px.line(df_agg, x='Date', y='Sales', title='Pink Morsels Sales Over Time')
fig.update_layout(xaxis_title='Date', yaxis_title='Total Sales ($)')
fig.add_vline(x=pd.to_datetime('2021-01-15').timestamp() * 1000, line_dash='dash', line_color='red',
              annotation_text='Price Increase', annotation_position='top right')

# dashapp init
app = Dash(__name__)

# Layout
app.layout = html.Div([
    html.H1('Soul_Foods with Pink_Morsel Sales Visualization'),
    dcc.Graph(figure=fig)
])

# application on local host to visualize
if __name__ == '__main__':
    app.run(debug=True)