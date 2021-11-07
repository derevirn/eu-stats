import streamlit as st
from urllib.request import urlopen
import json
import plotly.express as px


@st.cache
def get_geojson():
    nuts2_polygons = 'https://raw.githubusercontent.com/eurostat/Nuts2json/master/2021/4326/10M/nutsrg_2.json'
    with urlopen(nuts2_polygons) as response:
        regions = json.load(response)

    return regions
    
def create_line(data, selection, columns):
    df = data()

    fig = px.line(data_frame = df, x = 'time',  y = columns,
    title = selection)

    hovertemplate = '%{x|%d/%m/%Y} <br>%{y:.2f}'
    fig.update_traces(hovertemplate=hovertemplate)
    fig.update_layout(xaxis_title = '', yaxis_title = '',
                        plot_bgcolor = 'white',
                        margin=dict(l=1, r=1, t=25, b=1, pad=1))
    return fig

def create_bar(data, selection, columns):
    df = data()

    fig = px.bar(data_frame = df[-120:], x = 'time',  y = columns,
    title = selection)

    hovertemplate = '%{x|%d/%m/%Y} <br>%{y:.2f}'
    fig.update_traces(hovertemplate=hovertemplate)
    fig.update_layout(xaxis_title = '', yaxis_title = '',
                        plot_bgcolor = 'white',
                        margin=dict(l=1, r=1, t=25, b=1, pad=1))
    return fig



def create_choropleth(data, selection, columns):
    df = data()
    latest = str(df.index.year[-1])
    fig = px.choropleth(df.loc[latest], geojson = get_geojson(),
                        locations = 'geo', color = columns,
                        featureidkey = 'properties.id',
                        color_continuous_scale="Viridis_r",
                        projection = 'mercator',
                        fitbounds = 'locations',
                        #animation_frame = 'year',
                        basemap_visible = False,
                        height = 600,
                        custom_data = ['region_name', 'values'],
                        title = selection)

    hovertemplate = '%{customdata[0]}<br>%{customdata[1]:.2f}'
    fig.update_traces(hovertemplate=hovertemplate)
    fig.update_layout(margin={"r":0,"t":25,"l":0,"b":0})
    fig.update_coloraxes(colorbar_title_text="")

    return fig


def create_figure(selection, option_dict):

    data = option_dict[selection]['df_func']
    plot_type = option_dict[selection]['plot_type']
    columns = option_dict[selection]['columns']

    if plot_type == 'line':
        fig = create_line(data, selection, columns)

    elif plot_type == 'bar':
        fig = create_bar(data, selection, columns)
        
    elif plot_type == 'choropleth':
        fig = create_choropleth(data, selection, columns)

    return fig