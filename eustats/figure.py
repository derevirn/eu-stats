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
                      height = 450,
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
                      height = 450, 
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

def lin_reg_plot(df, x, y):
    df.reset_index(inplace = True)
    fig = px.scatter(df, x = x, y = y, trendline = 'ols',
                    height = 450, #color = 'EU Region',
                    hover_data= ['region_name'],
                  #  facet_col = 'EU Region', facet_col_wrap = 2,
                    color_discrete_sequence=px.colors.qualitative.D3)

   # hovertemplate = '%{customdata[0]}'
   # fig.update_traces(hovertemplate=hovertemplate)
    fig.update_layout(plot_bgcolor = 'white',
                    legend = dict(orientation = 'h', title = ''),
                    margin=dict(l=1, r=1, t=18, b=1, pad=1))

    return fig

def pca_plot(df):
    df.reset_index(inplace = True)
    df['pc_1'] = df['pc_1'] / 1000
    df['pc_2'] = df['pc_2'] / 1000
    fig = px.scatter(df, x = 'pc_1', y = 'pc_2', color='EU Region',
                    title = '',
                    height = 450, size = 'GDP per Capita',
                    hover_data = ['region_name', 'GDP per Capita'])

    fig.update_layout(  margin=dict(l=1, r=1, t=15, b=1, pad=1),
                        plot_bgcolor = 'white',
                        legend = dict(orientation = 'h', title = ''),
                        yaxis_title='Principal Component 2',
                        xaxis_title='Principal Component 1')

    hovertemplate = '%{customdata[0]}' 
    fig.update_traces(hovertemplate=hovertemplate)

    return fig

def box_plot(df, variable):
    df.reset_index(inplace = True)
    fig = px.box(df, x = 'EU Region', y = variable, points = 'all',
             color_discrete_sequence=px.colors.qualitative.D3,
             hover_data = ['region_name'],
             notched = True,
             title = f'Box Plot for {variable}',
             color = 'EU Region', height = 450)

    fig.update_layout(margin=dict(l=1, r=1, t=23, b=1, pad=1),
                    plot_bgcolor = 'white',
                    showlegend = False,
                    yaxis_title='', xaxis_title='')

    return fig

