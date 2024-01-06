# Import required libraries
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import os

# Create Dash app
app = dash.Dash(__name__)

# Layout of the app
app.layout = html.Div(
    children=[
        html.H1(children='Simple Dash App'),

        dcc.Graph(
            id='example-graph',
            figure={
                'data': [
                    {'x': [1, 2, 3, 4], 'y': [10, 11, 12, 13], 'type': 'bar', 'name': 'Trace 1'},
                    {'x': [1, 2, 3, 4], 'y': [15, 8, 10, 11], 'type': 'bar', 'name': 'Trace 2'},
                ],
                'layout': {
                    'title': 'Simple Bar Chart'
                }
            }
        )
    ]
)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))  # Use port 8080 if no PORT environment variable is set
    app.run_server(debug=False, host='0.0.0.0', port=port)
