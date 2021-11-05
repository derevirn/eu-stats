from urllib.request import urlopen
import json
import pandas as pd
import streamlit as st
from eurostatapiclient import EurostatAPIClient
from nuts2 import codes_el

client = EurostatAPIClient('v2.1', 'json', 'en')


#Get national GDP data
@st.cache
def get_df_gdp():
    params = {'geo': 'EL', 'unit': 'CP_MEUR', 'na_item': 'B1GQ'}
    df_gdp = client.get_dataset('nama_10_gdp', params).to_dataframe()
    df_gdp.dropna(inplace = True)
    df_gdp['values'] = df_gdp['values'] / 1000
    df_gdp['time'] = pd.to_datetime(df_gdp['time'])
    
    return df_gdp

#Get regional GDP data
@st.cache
def get_df_gdp_region():
    params = {'unit': 'MIO_EUR', 'geo': codes_el.keys()}
    df_gdp_region = client.get_dataset('nama_10r_2gdp', params).to_dataframe()
    df_gdp_region.dropna(inplace = True)
    df_gdp_region['region_name'] = df_gdp_region['geo'].apply(lambda x: codes_el[x])
    df_gdp_region['values'] = df_gdp_region['values'] / 1000
    df_gdp_region['time'] = pd.to_datetime(df_gdp_region['time'])
    df_gdp_region.set_index('time', inplace=True)  

    return df_gdp_region

@st.cache
def get_vaccinations():
    rename_dict = {'date': 'time',
                   'total_vaccinations': 'Σύνολο',
                   'people_fully_vaccinated': 'Ολοκληρωμένοι',
                   'people_vaccinated': 'Τουλάχιστον 1 Δόση',
                   'total_boosters': 'Αναμνηστική Δόση' }
    
    df_vaccinations = pd.read_csv("https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/country_data/Greece.csv")
    df_vaccinations['date'] = pd.to_datetime(df_vaccinations['date'])
    df_vaccinations.rename(columns = rename_dict, inplace = True)
    #df_vaccinations.set_index('date', inplace = True)

    return df_vaccinations

 
    
