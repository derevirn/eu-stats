import streamlit as st
from urllib.request import urlopen
import json
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
from .nuts2 import *

@st.cache_data
def get_geojson():
    nuts2_polygons = 'https://gist.githubusercontent.com/derevirn/bb384d57e971384fc125b0f342461b64/raw/b06abd34816029ba95167f2e4407c620c0d9d2d8/nutsrg_2.json'
    #nuts2_polygons = "https://raw.githubusercontent.com/eurostat/Nuts2json/refs/heads/master/pub/v2/2024/4326/20M/nutsrg_2.json"
    with urlopen(nuts2_polygons) as response:
        regions = json.load(response)

    return regions
    
def create_line(df, columns):

    fig = px.line(data_frame = df, x = 'time',  y = columns,
                  line_shape = 'linear', color = 'geo',
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
    fig.update_yaxes(automargin = False, showgrid=False)

    return fig

def create_bar(df, columns):

    fig = px.bar(data_frame = df[-60:], x = 'time',  y = columns,
                 color='geo', barmode = 'group',
                 color_discrete_sequence=px.colors.qualitative.D3)   

    hovertemplate = '%{x|%d/%m/%Y} <br>%{y:,.2f}'
    fig.update_traces(hovertemplate=hovertemplate)
    fig.update_layout(xaxis_title = '', yaxis_title = '',
                      height = 400, 
                      plot_bgcolor = 'white',
                      margin=dict(l=26, r=1, t=18, b=1, pad=1))
    fig.update_yaxes(automargin = False, showgrid=False)

    return fig

@st.cache_resource(max_entries=5)
def create_choropleth(df, columns):

    fig = px.choropleth(df, geojson = get_geojson(),
                        locations = 'geo', color = columns,
                        featureidkey = 'properties.id',
                        color_continuous_scale="Viridis_r",
                        color_discrete_sequence= px.colors.qualitative.Vivid,
                        projection = 'miller',
                        fitbounds = 'locations',
                        basemap_visible = False,
                        height = 500,
                        custom_data = ['region_name', 'values'])

    hovertemplate = '%{customdata[0]}<br>%{customdata[1]:,.2f}'
    fig.update_traces(hovertemplate=hovertemplate)
    fig.update_layout(margin={"r":1,"t":2,"l":1,"b":2})
    fig.update_coloraxes(colorbar_title_text="")

    return fig

@st.cache_resource(max_entries=5)
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

@st.cache_resource(max_entries=5)
def lin_reg_plot(df, x, y, model):

    if model == 'lowess':
         trendline_options=dict(frac=0.6)
    else:
        trendline_options=None

    fig = px.scatter(df, x = x, y = y, trendline = model,
                    height = 500, trendline_options = trendline_options,
                    hover_data= ['region_name'], 
                    #color='EU Region',
                    trendline_color_override = px.colors.qualitative.D3[3],
                    color_discrete_sequence=px.colors.qualitative.D3)

    fig.update_layout(plot_bgcolor = 'white',
                    legend = dict(orientation = 'h', title = ''),
                    margin=dict(l=1, r=1, t=18, b=1, pad=1))
    fig.update_yaxes(showgrid=False, zeroline = False)

    return fig

@st.cache_resource(max_entries=5)
def dimensionality_plot(df, color):

    df['pc_1'] = df['pc_1'] 
    df['pc_2'] = df['pc_2'] 
    fig = px.scatter(df, x = 'pc_1', y = 'pc_2', color=color,
                    color_discrete_sequence=px.colors.qualitative.D3,
                    title = '',
                    height = 480, size = 'GDP per Capita', size_max = 17,
                    custom_data = [color, 'region_name', 'Country'])

    fig.update_layout(  margin=dict(l=1, r=1, t=15, b=1, pad=1),
                        plot_bgcolor = 'white',
                        legend = dict(orientation = 'h', title = ''),
                        yaxis_title='Component 2',
                        xaxis_title='Component 1')

    hovertemplate = '%{customdata[1]} - %{customdata[0]} <extra></extra>' 
    fig.update_traces(hovertemplate=hovertemplate)
    fig.update_yaxes(showgrid=False, zeroline = False)

    return fig

@st.cache_resource(max_entries=5)
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
    fig.update_yaxes(showgrid=False, zeroline = False)
    
    return fig

@st.cache_resource(max_entries=5)
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

@st.cache_resource(max_entries=5)
def correlation_heatmap(df):

    fig, ax = plt.subplots(figsize = (10,8))

    sns.heatmap(df.corr(numeric_only = True).round(decimals=2),
    annot=True, ax = ax)

    return fig

