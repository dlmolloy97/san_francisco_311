import dash_core_components as dcc
import dash_html_components as html

app_layout = html.Div([
    html.H1('311 Data Explorer'),
    html.Div([
        html.Div([
            html.H3('Variable'),
            dcc.Dropdown(
                id='variable',
                options=[
                    {'label': 'Frequency', 'value': 'frequency'},
                    {'label': 'Response Time', 'value': 'resolution_time'}
                ],
                value='frequency'
            )
        ], className='six columns'),
        html.Div([
            html.H3('Grouping'),
            dcc.Dropdown(
                id='grouping',
                options=[
                    {'label': 'Neighbourhood', 'value': 'neighborhood'},
                    {'label': 'Supervisor District', 'value': 'supervisor_district'}
                ],
                value='neighborhood'
            )
        ], className='six columns')
    ], className='row'),
    html.Div([
        html.Div([
            dcc.Graph(id='graph')
        ], className='six columns'),
        html.Div([
            dcc.Graph(id='choropleth')
        ], className='six columns')
    ], className='row'),
    ])