import streamlit as st
from urllib.request import urlopen
import json
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
from .nuts2 import *

@st.cache_data
def get_geojson():
    nuts2_polygons = 'https://gist.githubusercontent.com/derevirn/6c433e9adacc839814cee57b6603f793/raw/40442fab2a394cfececd13db6dd9dd3ef174975a/nutsrg_2.json'
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

    fig = px.choropleth(df, geojson = get_geojson(),
                        locations = 'geo', color = columns,
                        featureidkey = 'properties.id',
                        color_continuous_scale="Viridis_r",
                        projection = 'mercator',
                        fitbounds = 'locations',
                        basemap_visible = False,
                        height = 500,
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

def lin_reg_plot(df, x, y, model):

    if model == 'lowess':
         trendline_options=dict(frac=0.6)
    else:
        trendline_options=None

    fig = px.scatter(df, x = x, y = y, trendline = model,
                    height = 400, trendline_options = trendline_options,
                    hover_data= ['region_name'], 
                    trendline_color_override = px.colors.qualitative.D3[3],
                    color_discrete_sequence=px.colors.qualitative.D3)

    fig.update_layout(plot_bgcolor = 'white',
                    legend = dict(orientation = 'h', title = ''),
                    margin=dict(l=1, r=1, t=18, b=1, pad=1))

    return fig

def pca_plot(df):

    df['pc_1'] = df['pc_1'] / 1000
    df['pc_2'] = df['pc_2'] / 1000
    fig = px.scatter(df, x = 'pc_1', y = 'pc_2', color='EU Region',
                    color_discrete_sequence=px.colors.qualitative.D3,
                    title = '',
                    height = 400, size = 'GDP per Capita',
                    hover_data = ['region_name', 'Country'])

    fig.update_layout(  margin=dict(l=1, r=1, t=15, b=1, pad=1),
                        plot_bgcolor = 'white',
                        legend = dict(orientation = 'h', title = ''),
                        yaxis_title='Principal Component 2',
                        xaxis_title='Principal Component 1')

    hovertemplate = '%{customdata[1]} - %{customdata[0]}' 
    fig.update_traces(hovertemplate=hovertemplate)

    return fig

def box_plot(df, variable):

    fig = px.box(df, x = 'EU Region', y = variable, points = 'all',
            color_discrete_sequence=px.colors.qualitative.D3,
            hover_data = ['region_name'],
            notched = True, title = '',
            color = 'EU Region', height = 400)

    fig.update_layout(margin=dict(l=1, r=1, t=23, b=1, pad=1),
                    plot_bgcolor = 'white',
                    showlegend = False,
                    yaxis_title='', xaxis_title='')
    return fig

def kde_plot(df, variable):

    fig, ax = plt.subplots(figsize = (10,6))

    ax.grid(False)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.get_yaxis().set_ticks([])

    sns.kdeplot(data = df, x = variable, fill = True,
                alpha = 0.15,
                hue = 'EU Region', ax = ax)

    return fig

def correlation_heatmap(df):

    fig, ax = plt.subplots(figsize = (10,8))

    sns.heatmap(df.corr(numeric_only = True).round(decimals=2),
    annot=True, ax = ax)

    return fig

