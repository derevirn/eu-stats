import pandas as pd
import streamlit as st
from eurostatapiclient import EurostatAPIClient
from nuts2 import codes_el

client = EurostatAPIClient('v2.1', 'json', 'en')

#Economy

@st.cache
def get_gdp():
    params = {'geo': 'EL', 'unit': 'CP_MEUR', 'na_item': 'B1GQ'}
    df = client.get_dataset('nama_10_gdp', params).to_dataframe()
    df.dropna(inplace = True)
    df['values'] = df['values'] / 1000
    df['time'] = pd.to_datetime(df['time'])
    
    return df

@st.cache
def get_gdp_region():
    params = {'unit': 'MIO_EUR', 'geo': codes_el.keys()}
    df = client.get_dataset('nama_10r_2gdp', params).to_dataframe()
    df.dropna(inplace = True)
    df['region_name'] = df['geo'].apply(lambda x: codes_el[x])
    df['values'] = df['values'] / 1000
    df['time'] = pd.to_datetime(df['time'])
    df.set_index('time', inplace=True)  

    return df

@st.cache
def get_unemployment():
    params = {'geo': 'EL', 's_adj': 'SA', 'indic': 'LM-UN-T-TOT'}
    df = client.get_dataset('ei_lmhr_m', params).to_dataframe()
    df.dropna(inplace = True)
    df['time'] = pd.to_datetime(df['time'], format = '%YM%m')

    return df

@st.cache
def get_unemployment_region():
    params = {'sex': 'T', 'geo': codes_el.keys(), 'age': 'Y15-74',
          'isced11': 'TOTAL'} 
    df = client.get_dataset('lfst_r_lfu3rt', params).to_dataframe()
    df.dropna(inplace = True)
    df['region_name'] = df['geo'].apply(lambda x: codes_el[x])
    df['time'] = pd.to_datetime(df['time'])
    df['year'] = df['time'].dt.year
    df.set_index('time', inplace = True)

    return df

#COVID-19

@st.cache
def get_new_cases():
    df = pd.read_csv('https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/jhu/new_cases.csv')
    df['date'] = pd.to_datetime(df['date'])
    cols = ['date', 'Greece']
    df = df[cols]
    df.rename(columns = {'date': 'time', 'Greece': 'values'}, inplace = True)
    df.dropna(inplace = True)

    return df

@st.cache
def get_new_deaths():
    df = pd.read_csv('https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/jhu/new_deaths.csv')
    df['date'] = pd.to_datetime(df['date'])
    cols = ['date', 'Greece']
    df = df[cols]
    df.rename(columns = {'date': 'time', 'Greece': 'values'}, inplace = True)
    df.dropna(inplace = True)
    
    return df

@st.cache
def get_total_cases():
    df = pd.read_csv('https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/jhu/total_cases.csv')
    df['date'] = pd.to_datetime(df['date'])
    cols = ['date', 'Greece']
    df = df[cols]
    df.rename(columns = {'date': 'time', 'Greece': 'values'}, inplace = True)
    df.dropna(inplace = True)
    
    return df

@st.cache
def get_total_deaths():
    df = pd.read_csv('https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/jhu/total_deaths.csv')
    df['date'] = pd.to_datetime(df['date'])
    cols = ['date', 'Greece']
    df = df[cols]
    df.rename(columns = {'date': 'time', 'Greece': 'values'}, inplace = True)
    df.dropna(inplace = True)
    
    return df

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

 
    
