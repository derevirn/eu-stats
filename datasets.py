from urllib.request import urlopen
import json
import pandas as pd
import streamlit as st
from eurostatapiclient import EurostatAPIClient
from nuts2 import codes_el

data = {}


@st.cache
def get_data():
    client = EurostatAPIClient('v2.1', 'json', 'en')

    #Get national GDP data
    params = {'geo': 'EL', 'unit': 'CP_MEUR', 'na_item': 'B1GQ'}
    df_gdp = client.get_dataset('nama_10_gdp', params).to_dataframe()
    df_gdp.dropna(inplace = True)
    df_gdp['values'] = df_gdp['values'] / 1000
    df_gdp['time'] = pd.to_datetime(df_gdp['time'])
    df_gdp.set_index('time', inplace=True)
    data['GDP'] = df_gdp

    #Get regional GDP data
    params = {'unit': 'MIO_EUR', 'geo': codes_el.keys()}
    df_gdp_region = client.get_dataset('nama_10r_2gdp', params).to_dataframe()
    df_gdp_region.dropna(inplace = True)
    df_gdp_region['region_name'] = df_gdp_region['geo'].apply(lambda x: codes_el[x])
    df_gdp_region['values'] = df_gdp_region['values'] / 1000
    df_gdp_region['time'] = pd.to_datetime(df_gdp_region['time'])
    df_gdp_region.set_index('time', inplace=True)    
    data['GDP_region'] = df_gdp_region

    
    return data 

 
    
