import streamlit as st
from urllib.request import urlopen
import json
import plotly.express as px
from .nuts2 import *


@st.cache
def get_geojson():
    nuts2_polygons = 'https://raw.githubusercontent.com/eurostat/Nuts2json/master/2021/4326/20M/nutsrg_2.json'
    with urlopen(nuts2_polygons) as response:
        regions = json.load(response)

    return regions
    
def create_line(df, columns):

    fig = px.line(data_frame = df, x = 'time',  y = columns,
                  line_shape = 'linear',
                  render_mode = 'svg',
                  color_discrete_sequence=px.colors.qualitative.D3)

    hovertemplate = '%{x|%d/%m/%Y} <br>%{y:,.2f}'
    fig.update_traces(hovertemplate=hovertemplate)
    fig.update_traces(line_width = 3)
    fig.update_layout(xaxis_title = '', yaxis_title = '',
                      height = 400,
                      plot_bgcolor = 'white',
                      legend = dict(orientation = 'h', title = ''),
                      margin=dict(l=22, r=1, t=18, b=1, pad=1))
    fig.update_yaxes(automargin = False)

    return fig

def create_bar(df, columns):

    fig = px.bar(data_frame = df[-60:], x = 'time',  y = columns,
                 color_discrete_sequence=px.colors.qualitative.D3)   

    hovertemplate = '%{x|%d/%m/%Y} <br>%{y:,.2f}'
    fig.update_traces(hovertemplate=hovertemplate)
    fig.update_layout(xaxis_title = '', yaxis_title = '',
                      height = 400, 
                      plot_bgcolor = 'white',
                      margin=dict(l=26, r=1, t=18, b=1, pad=1))
    fig.update_yaxes(automargin = False)

    return fig


def create_choropleth(df, columns):

    latest = str(df.index.year[-1])
    fig = px.choropleth(df.loc[latest], geojson = get_geojson(),
                        locations = 'geo', color = columns,
                        featureidkey = 'properties.id',
                        color_continuous_scale="Viridis_r",
                        projection = 'mercator',
                        fitbounds = 'locations',
                        basemap_visible = False,
                        height = 600,
                        custom_data = ['region_name', 'values'])

    hovertemplate = '%{customdata[0]}<br>%{customdata[1]:,.2f}'
    fig.update_traces(hovertemplate=hovertemplate)
    fig.update_layout(margin={"r":1,"t":15,"l":1,"b":10})
    fig.update_coloraxes(colorbar_title_text="")

    return fig


def create_figure(df, dict_selection):

    plot_type = dict_selection['plot_type']
    columns = dict_selection['columns']

    if plot_type == 'line':
        fig = create_line(df, columns)

    elif plot_type == 'bar':
        fig = create_bar(df, columns)
        
    elif plot_type == 'choropleth':
        fig = create_choropleth(df, columns)

    return fig