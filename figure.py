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
    
def create_line(data, columns):
    df = data()

    fig = px.line(data_frame = df, x = 'time',  y = columns,
                  line_shape = 'linear',
                  color_discrete_sequence=px.colors.qualitative.D3)

    hovertemplate = '%{x|%d/%m/%Y} <br>%{y:.2f}'
    fig.update_traces(hovertemplate=hovertemplate)
    fig.update_layout(xaxis_title = '', yaxis_title = '',
                        plot_bgcolor = 'white',
                        margin=dict(l=20, r=1, t=1, b=1, pad=1))
    fig.update_yaxes(automargin = False)

    return fig

def create_bar(data, columns):
    df = data()

    fig = px.bar(data_frame = df[-90:], x = 'time',  y = columns,
                 color_discrete_sequence=px.colors.qualitative.D3)   

    hovertemplate = '%{x|%d/%m/%Y} <br>%{y:.2f}'
    fig.update_traces(hovertemplate=hovertemplate)
    fig.update_layout(xaxis_title = '', yaxis_title = '',
                        plot_bgcolor = 'white',
                        margin=dict(l=26, r=1, t=1, b=1, pad=1))
    fig.update_yaxes(automargin = False)

    return fig



def create_choropleth(data, columns):
    df = data()
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

    hovertemplate = '%{customdata[0]}<br>%{customdata[1]:.2f}'
    fig.update_traces(hovertemplate=hovertemplate)
    fig.update_layout(margin={"r":1,"t":1,"l":1,"b":1})
    fig.update_coloraxes(colorbar_title_text="")

    return fig


def create_figure(selection, option_dict):

    data = option_dict[selection]['df_func']
    plot_type = option_dict[selection]['plot_type']
    columns = option_dict[selection]['columns']

    if plot_type == 'line':
        fig = create_line(data, columns)

    elif plot_type == 'bar':
        fig = create_bar(data, columns)
        
    elif plot_type == 'choropleth':
        fig = create_choropleth(data, columns)

    return fig