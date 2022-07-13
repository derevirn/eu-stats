import pandas as pd
import streamlit as st
from eurostatapiclient import EurostatAPIClient
from .nuts2 import *

SEC_IN_DAY = 86400
client = EurostatAPIClient('v2.2', 'json', 'en')

###############################################################################

#Economy

@st.cache(ttl = SEC_IN_DAY)
def get_gdp(country):
    country = countries[country]
    params = {'geo': country, 'unit': 'CP_MEUR', 'na_item': 'B1GQ'}
    df = client.get_dataset('nama_10_gdp', params).to_dataframe()
    df.dropna(inplace = True)
    df['values'] = df['values'] / 1000
    df['time'] = pd.to_datetime(df['time'])
    
    return df

@st.cache(ttl = SEC_IN_DAY)
def get_gdp_region(country):
    country = countries[country]
    params = {'unit': 'MIO_EUR', 'geo': codes[country]}
    df = client.get_dataset('nama_10r_2gdp', params).to_dataframe()
    df.dropna(inplace = True)
    df['region_name'] = df['geo'].apply(lambda x: codes[country][x])
    df['values'] = df['values'] / 1000
    df['time'] = pd.to_datetime(df['time'])
    df['year'] = df['time'].dt.year
    df.set_index(pd.DatetimeIndex(df['time']), inplace=True)  

    return df

@st.cache(ttl = SEC_IN_DAY)
def get_gdp_capita(country):
    country = countries[country]
    params = {'geo': country, 'unit': 'CLV10_EUR_HAB', 'na_item': 'B1GQ'}
    df = client.get_dataset('nama_10_pc', params).to_dataframe()
    df.dropna(inplace = True)
    df['time'] = pd.to_datetime(df['time'])
    
    return df

@st.cache(ttl = SEC_IN_DAY)
def get_gdp_capita_region(country):
    country = countries[country]
    params = {'unit': 'EUR_HAB', 'geo': codes[country]}
    df = client.get_dataset('nama_10r_2gdp', params).to_dataframe()
    df.dropna(inplace = True)
    df['region_name'] = df['geo'].apply(lambda x: codes[country][x])
    df['time'] = pd.to_datetime(df['time'])
    df['year'] = df['time'].dt.year
    df.set_index(pd.DatetimeIndex(df['time']), inplace=True)  

    return df

@st.cache(ttl = SEC_IN_DAY)
def get_govt_debt(country):
    country = countries[country]
    params = {'geo': country, 'unit': 'PC_GDP',
              'sector': 'S13', 'na_item': 'GD'}
    df = client.get_dataset('gov_10dd_edpt1', params).to_dataframe()
    df.dropna(inplace = True)
    df['time'] = pd.to_datetime(df['time'])
    
    return df

@st.cache(ttl = SEC_IN_DAY)
def get_govt_budget(country):
    country = countries[country]
    params = {'geo': country, 'unit': 'PC_GDP',
              'sector': 'S13', 'na_item': 'B9'}
    df = client.get_dataset('gov_10dd_edpt1', params).to_dataframe()
    df.dropna(inplace = True)
    df['time'] = pd.to_datetime(df['time'])
    
    return df


@st.cache(ttl = SEC_IN_DAY)
def get_unemployment(country):
    country = countries[country]
    params = {'geo': country, 's_adj': 'SA', 'indic': 'LM-UN-T-TOT'}
    df = client.get_dataset('ei_lmhr_m', params).to_dataframe()
    df.dropna(inplace = True)
    df['time'] = pd.to_datetime(df['time'], format = '%YM%m')

    return df

@st.cache(ttl = SEC_IN_DAY)
def get_unemployment_region(country):
    country = countries[country]
    params = {'sex': 'T', 'geo': codes[country], 'age': 'Y15-74',
          'isced11': 'TOTAL'} 
    df = client.get_dataset('lfst_r_lfu3rt', params).to_dataframe()
    df.dropna(inplace = True)
    df['region_name'] = df['geo'].apply(lambda x: codes[country][x])
    df['time'] = pd.to_datetime(df['time'])
    df['year'] = df['time'].dt.year
    df.set_index(pd.DatetimeIndex(df['time']), inplace=True)  

    return df

@st.cache(ttl = SEC_IN_DAY)
def get_min_wage(country):
    country = countries[country]
    params = {'geo': country, 'currency': 'EUR'}
    df = client.get_dataset('earn_mw_cur', params).to_dataframe()
    df.dropna(inplace = True)
    df['time'] = df['time'].str.replace('S1','-01-01')
    df['time'] = df['time'].str.replace('S2','-07-01')
    df['time'] = pd.to_datetime(df['time'])

    return df


@st.cache(ttl = SEC_IN_DAY)
def get_inflation(country):

    country = countries[country]
    params = {'geo': country, 'coicop': 'CP00'}
    df = client.get_dataset('prc_hicp_aind', params).to_dataframe()
    df.dropna(inplace = True)
    mask = df['unit'] == 'RCH_A_AVG'
    df = df[mask]
    df['time'] = pd.to_datetime(df['time'])

    return df

###############################################################################

#Society 

@st.cache(ttl = SEC_IN_DAY)
def get_population(country):
    country = countries[country]
    params = {'geo': country, 'indic_de': ['JAN', 'MJAN', 'FJAN']}
    df = client.get_dataset('demo_gind', params).to_dataframe()
    df.dropna(inplace = True)
    df['time'] = pd.to_datetime(df['time'])
    df = df.pivot(index = 'time', columns = 'indic_de', values = 'values').reset_index()

    columns = {'JAN': 'Total Population',
               'MJAN': 'Male Population',
               'FJAN': 'Female Population'}
    df.rename(columns = columns, inplace = True)

    return df

@st.cache(ttl = SEC_IN_DAY)
def get_population_region(country):
    country = countries[country]
    params = {'geo': codes[country], 'sex': 'T',
              'age': 'TOTAL'}
    df = client.get_dataset('demo_r_d2jan', params).to_dataframe()
    df.dropna(inplace = True)
    df['region_name'] = df['geo'].apply(lambda x: codes[country][x])
    df['time'] = pd.to_datetime(df['time'])
    df['year'] = df['time'].dt.year
    df.set_index(pd.DatetimeIndex(df['time']), inplace=True)  

    return df

@st.cache(ttl = SEC_IN_DAY)
def get_poverty_risk(country):
    country = countries[country]
    params = {'geo': country, 'age': 'TOTAL', 'unit': 'PC'}
    df = client.get_dataset('sdg_01_10', params).to_dataframe()
    df.dropna(inplace = True)
    df['time'] = pd.to_datetime(df['time'])

    return df

@st.cache(ttl = SEC_IN_DAY)
def get_poverty_risk_region(country):
    country = countries[country]
    params = {'geo': codes[country]}
    df = client.get_dataset('ilc_peps11', params).to_dataframe()
    df.dropna(inplace = True)
    df['region_name'] = df['geo'].apply(lambda x: codes[country][x])
    df['time'] = pd.to_datetime(df['time'])
    df['year'] = df['time'].dt.year
    df.set_index(pd.DatetimeIndex(df['time']), inplace=True)  

    return df


@st.cache(ttl = SEC_IN_DAY)
def get_gender_pay_gap(country):
    country = countries[country]
    params = {'geo': country}
    df = client.get_dataset('sdg_05_20', params).to_dataframe()
    df.dropna(inplace = True)
    df['time'] = pd.to_datetime(df['time'])

    return df



###############################################################################

#COVID-19

@st.cache(ttl = SEC_IN_DAY)
def get_new_cases(country):
    df = pd.read_csv('https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/jhu/new_cases.csv')
    df['date'] = pd.to_datetime(df['date'])
    cols = ['date', country]
    df = df[cols]
    df.rename(columns = {'date': 'time', country: 'values'}, inplace = True)
    df.dropna(inplace = True)

    return df

@st.cache(ttl = SEC_IN_DAY)
def get_new_deaths(country):
    df = pd.read_csv('https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/jhu/new_deaths.csv')
    df['date'] = pd.to_datetime(df['date'])
    cols = ['date', country]
    df = df[cols]
    df.rename(columns = {'date': 'time', country: 'values'}, inplace = True)
    df.dropna(inplace = True)
    
    return df

@st.cache(ttl = SEC_IN_DAY)
def get_total_cases(country):
    df = pd.read_csv('https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/jhu/total_cases.csv')
    df['date'] = pd.to_datetime(df['date'])
    cols = ['date', country]
    df = df[cols]
    df.rename(columns = {'date': 'time', country: 'values'}, inplace = True)
    df.dropna(inplace = True)
    
    return df

@st.cache(ttl = SEC_IN_DAY)
def get_total_deaths(country):
    df = pd.read_csv('https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/jhu/total_deaths.csv')
    df['date'] = pd.to_datetime(df['date'])
    cols = ['date', country]
    df = df[cols]
    df.rename(columns = {'date': 'time', country: 'values'}, inplace = True)
    df.dropna(inplace = True)
    
    return df

@st.cache(ttl = SEC_IN_DAY)
def get_vaccinations(country):
    rename_dict = {'date': 'time',
                   'total_vaccinations': 'Total Vaccinations',
                   'people_fully_vaccinated': 'Fully Vaccinated',
                   'people_vaccinated': 'At Least One Dose',
                   'total_boosters': 'Booster Dose' }
    
    df_vaccinations = pd.read_csv("https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/country_data/{}.csv".format(country))
    df_vaccinations['date'] = pd.to_datetime(df_vaccinations['date'])
    df_vaccinations.rename(columns = rename_dict, inplace = True)
    #df_vaccinations.set_index('date', inplace = True)

    return df_vaccinations