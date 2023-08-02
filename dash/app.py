import dash
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import components
import data

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = components.app_layout

@app.callback(
    Output('graph', 'figure'),
    [Input('variable', 'value'),
     Input('grouping', 'value')])
def update_graph(variable, grouping):
    return data.update_graph(variable, grouping)

@app.callback(
    Output('choropleth', 'figure'),
    [Input('variable', 'value')])
def update_choropleth(variable):
    return data.update_choropleth(variable)

if __name__ == '__main__':
    app.run_server(debug=True)