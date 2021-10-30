import pandas as pd
import streamlit as st
from eurostatapiclient import EurostatAPIClient

data = {}


@st.cache
def get_data():
    client = EurostatAPIClient('v2.1', 'json', 'en')

    params = {'geo': 'EL', 'unit': 'CP_MEUR', 'na_item': 'B1GQ'}
    df_gdp = client.get_dataset('nama_10_gdp', params).to_dataframe()
    df_gdp.dropna(inplace = True)
    df_gdp['values'] = df_gdp['values'] / 1000
    df_gdp['time'] = pd.to_datetime(df_gdp['time'])
    df_gdp.set_index('time', inplace=True)

    data['GDP'] = df_gdp

    data['test'] = pd.DataFrame([[10,30], [20,50], [30,40], [50,60]],
                                 columns=['x', 'y'])

    return data 


    
