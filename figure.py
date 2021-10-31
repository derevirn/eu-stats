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
    
def create_line(data, selection, select_):
    fig = px.line(data_frame = data[select_], y='values',
    title = selection)
    fig.update_layout(xaxis_title = '', yaxis_title = '',
                        plot_bgcolor = 'white',
                        margin=dict(l=1, r=1, t=25, b=1, pad=1))
    return fig

def create_choropleth(data, selection, select_):
    latest = str(data[select_].index.year[-1])
    hovertemplate = '%{customdata[0]}<br>%{customdata[1]:.2f} δις €'

    fig = px.choropleth(data[select_].loc[latest], geojson = get_geojson(),
                        locations = 'geo', color = 'values',
                        featureidkey = 'properties.id',
                        color_continuous_scale="Viridis",
                        projection = 'mercator',
                        fitbounds = 'locations',
                        #animation_frame = 'time',
                        basemap_visible = False,
                        width = 700, height = 500,
                        custom_data = ['region_name', 'values'],
                        title = 'ΑΕΠ Περιφερειών σε Δισεκατομμύρια Ευρώ')

    fig.update_traces(hovertemplate=hovertemplate)
    fig.update_layout(margin={"r":0,"t":25,"l":0,"b":0})
    fig.update_coloraxes(colorbar_title_text="")

    return fig


def create_figure(data, selection, option_dict):
    select_  = option_dict[selection]

    if select_ == 'GDP':
        fig = create_line(data, selection, select_)
        
    else:
        fig = create_choropleth(data, selection, select_)
        
    return fig