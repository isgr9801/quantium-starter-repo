import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output

# Load the data
df = pd.read_csv('Soul_Foods-Pink_Morsels-Consolidated.csv')

# Preprocess
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df = df.sort_values('Date')

# Dash app init
app = Dash(__name__)

# Layout with RadioItems for region filtering
app.layout = html.Div(
    style={'fontFamily': 'Arial', 'backgroundColor': '#f0f2f5', 'padding': '20px'},
    children=[
        html.H1(
            'Soul Foods: Pink Morsels Sales Visualization',
            style={'textAlign': 'center', 'color': '#2c3e50'}
        ),
        html.Div([
            html.Label("Select Region:", style={'fontSize': '18px', 'marginRight': '10px'}),
            dcc.RadioItems(
                id='region-selector',
                options=[
                    {'label': 'All', 'value': 'all'},
                    {'label': 'North', 'value': 'north'},
                    {'label': 'East', 'value': 'east'},
                    {'label': 'South', 'value': 'south'},
                    {'label': 'West', 'value': 'west'},
                ],
                value='all',
                labelStyle={'display': 'inline-block', 'margin-right': '15px', 'fontSize': '16px'},
                style={'padding': '10px'}
            )
        ], style={'textAlign': 'center', 'marginBottom': '30px'}),

        dcc.Graph(id='sales-graph', style={'boxShadow': '0px 0px 10px #aaa', 'borderRadius': '10px'})
    ]
)

# Callback to update graph based on selected region
@app.callback(
    Output('sales-graph', 'figure'),
    Input('region-selector', 'value')
)
def update_graph(region):
    if region == 'all':
        filtered_df = df.copy()
    else:
        filtered_df = df[df['Region'].str.lower() == region]

    df_agg = filtered_df.groupby('Date')['Sales'].sum().reset_index()
    fig = px.line(df_agg, x='Date', y='Sales', title=f'{region.capitalize() if region != "all" else "All Regions"} Sales Over Time')
    fig.update_layout(
        xaxis_title='Date',
        yaxis_title='Total Sales ($)',
        plot_bgcolor='white',
        paper_bgcolor='white',
        font=dict(color='#2c3e50'),
        title_font=dict(size=22)
    )
    fig.add_vline(
        x=pd.to_datetime('2021-01-15').timestamp() * 1000,
        line_dash='dash',
        line_color='red',
        annotation_text='Price Increase',
        annotation_position='top right'
    )
    return fig

# Run app
if __name__ == '__main__':
    app.run(debug=True)
