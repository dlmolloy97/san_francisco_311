
from sf311 import bigquery_connector
import geopandas as gpd
import plotly.express as px
import os
home = os.path.expanduser("~")

def update_graph(variable, grouping):
    # Get data
    query = f"""
        SELECT
            *
        FROM fluid-skyline-255211.san_francisco_311.analytics__{variable}__{grouping}
    """
    df = bigquery_connector(query)

    # Plot
    if grouping == 'neighborhood':
        # Set neighborhood column to string
        df['neighborhood'] = df['neighborhood'].astype(str)
    fig = px.bar(df, x=grouping, y=variable, barmode='group')
    fig.update_layout(
        title=f'{variable} by {grouping}',
        xaxis_title=grouping,
        yaxis_title=variable
    )
    return fig

def update_choropleth(variable):
    # Get data
    query = f"""
        SELECT
            *
        FROM fluid-skyline-255211.san_francisco_311.analytics__{variable}__neighborhood
    """
    df = bigquery_connector(query)
    df['neighborhood'] = df['neighborhood'].astype(str)
    # Exclude entries for neighborhood = 8
    df = df[df['neighborhood'] != '8']
    geo_path = os.path.join(home, 'PycharmProjects/san_francisco_311/data/neighborhoods.geojson')
    neighbourhoods_viz = gpd.read_file(geo_path, driver='GeoJSON')
    neighbourhoods_viz.columns = ['link', 'neighborhood', 'geometry']
    df_joined = neighbourhoods_viz.merge(df, on='neighborhood', how='left')
    df_joined[f'{variable}'] = df_joined[f'{variable}'].astype(float)

    fig = px.choropleth_mapbox(df_joined, geojson=df_joined.geometry, locations=df_joined.index, color=df_joined[f'{variable}'],
                               color_continuous_scale="viridis",
                               range_color=(0, df_joined[f'{variable}'].max()),
                               mapbox_style="carto-positron",
                               zoom=11, center={"lat": 37.7749, "lon": -122.4194},
                               opacity=0.5,
                               labels={
                                       'neighborhood': 'Neighborhood'}
                               )
    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})
    return fig