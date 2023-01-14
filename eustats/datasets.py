import pandas as pd
import streamlit as st
from eurostatapiclient import EurostatAPIClient
from .nuts2 import *

SEC_IN_DAY = 86400
client = EurostatAPIClient('1.0', 'json', 'en')

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
    params = {'unit': 'MIO_EUR', 'geo': codes[country], 'lastTimePeriod': 1}
    df = client.get_dataset('nama_10r_2gdp', params).to_dataframe()
    df.dropna(inplace = True)
    df['region_name'] = df['geo'].apply(lambda x: codes[country][x])
    df['values'] = df['values'] / 1000
    df['time'] = pd.to_datetime(df['time']) 

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
    params = {'unit': 'EUR_HAB', 'geo': codes[country], 'lastTimePeriod': 1}
    df = client.get_dataset('nama_10r_2gdp', params).to_dataframe()
    df.dropna(inplace = True)
    df['region_name'] = df['geo'].apply(lambda x: codes[country][x])
    df['time'] = pd.to_datetime(df['time'])

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
          'isced11': 'TOTAL', 'lastTimePeriod': 1}
    df = client.get_dataset('lfst_r_lfu3rt', params).to_dataframe()
    df.dropna(inplace = True)
    df['region_name'] = df['geo'].apply(lambda x: codes[country][x])
    df['time'] = pd.to_datetime(df['time'])

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

@st.cache(ttl = SEC_IN_DAY)
def get_gini(country):
    country = countries[country]
    params = {'geo': country}
    df = client.get_dataset('ilc_di12', params).to_dataframe()
    df.dropna(inplace = True)
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
              'age': 'TOTAL', 'lastTimePeriod': 1}
    df = client.get_dataset('demo_r_d2jan', params).to_dataframe()
    df.dropna(inplace = True)
    df['region_name'] = df['geo'].apply(lambda x: codes[country][x])
    df['time'] = pd.to_datetime(df['time'])

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
    params = {'geo': codes[country], 'lastTimePeriod': 1}
    df = client.get_dataset('ilc_peps11', params).to_dataframe()
    df.dropna(inplace = True)
    df['region_name'] = df['geo'].apply(lambda x: codes[country][x])
    df['time'] = pd.to_datetime(df['time'])

    return df


@st.cache(ttl = SEC_IN_DAY)
def get_gender_pay_gap(country):
    country = countries[country]
    params = {'geo': country}
    df = client.get_dataset('sdg_05_20', params).to_dataframe()
    df.dropna(inplace = True)
    df['time'] = pd.to_datetime(df['time'])

    return df

##############################################################################

#Health

@st.cache(ttl = SEC_IN_DAY)
def get_life_expectancy(country):
    country = countries[country]
    params = {'geo': country, 'sex': 'T', 'age': 'Y_LT1' }
    df = client.get_dataset('demo_mlexpec', params).to_dataframe()
    df.dropna(inplace = True)
    df['time'] = pd.to_datetime(df['time'])

    return df

@st.cache(ttl = SEC_IN_DAY)
def get_life_expectancy_region(country):
    country = countries[country]
    params = {'sex': 'T', 'geo': codes[country], 'lastTimePeriod': 1}
    df = client.get_dataset('tgs00101', params).to_dataframe()
    df.dropna(inplace = True)
    df['region_name'] = df['geo'].apply(lambda x: codes[country][x]) 

    return df

@st.cache(ttl = SEC_IN_DAY)
def get_doctors(country):
    country = countries[country]
    params = {'geo': country, 'unit': 'P_HTHAB',
              'wstatus': 'PRACT', 'isco08': 'OC221' }
    df = client.get_dataset('hlth_rs_prs1', params).to_dataframe()
    df.dropna(inplace = True)
    df['time'] = pd.to_datetime(df['time'])

    return df

@st.cache(ttl = SEC_IN_DAY)
def get_doctors_region(country):
    country = countries[country]
    params = {'geo': codes[country], 'unit': 'P_HTHAB',
              'isco08': 'OC221', 'lastTimePeriod': 1}
    df = client.get_dataset('hlth_rs_prsrg', params).to_dataframe()
    df.dropna(inplace = True)
    df['region_name'] = df['geo'].apply(lambda x: codes[country][x])

    return df

@st.cache(ttl = SEC_IN_DAY)
def get_healthcare_expenditure(country):
    country = countries[country]
    params = {'geo': country, 'unit': 'PC_GDP', 'icha11_hc': 'TOT_HC'}
    df = client.get_dataset('hlth_sha11_hc', params).to_dataframe()
    df.dropna(inplace = True)
    df['time'] = pd.to_datetime(df['time'])

    return df


@st.cache(ttl = SEC_IN_DAY)
def get_hospital_beds(country):
    country = countries[country]
    params = {'geo': country, 'unit': 'P_HTHAB',
              'facility': 'HBEDT' }
    df = client.get_dataset('tps00046', params).to_dataframe()
    df.dropna(inplace = True)
    df['time'] = pd.to_datetime(df['time'])

    return df

@st.cache(ttl = SEC_IN_DAY)
def get_hospital_beds_region(country):
    country = countries[country]
    params = {'geo': codes[country], 'unit': 'P_HTHAB',
              'facility': 'HBEDT', 'lastTimePeriod': 1}
    df = client.get_dataset('hlth_rs_bdsrg', params).to_dataframe()
    df.dropna(inplace = True)
    df['region_name'] = df['geo'].apply(lambda x: codes[country][x]) 

    return df

###############################################################################

#Education

@st.cache(ttl = SEC_IN_DAY)
def get_tertiary_attainment(country):
    country = countries[country]
    params = {'geo': country, 'sex': 'T', 'unit': 'PC',
              'age': 'Y25-64', 'isced11': 'ED5-8'  }
    df = client.get_dataset('edat_lfse_03', params).to_dataframe()
    df.dropna(inplace = True)
    df['time'] = pd.to_datetime(df['time'])

    return df


@st.cache(ttl = SEC_IN_DAY)
def get_tertiary_attainment_region(country):
    country = countries[country]
    params = {'geo': codes[country], 'sex': 'T', 'unit': 'PC',
              'age': 'Y25-64', 'isced11': 'ED5-8', 'lastTimePeriod': 1}
    df = client.get_dataset('edat_lfse_04', params).to_dataframe()
    df.dropna(inplace = True)
    df['region_name'] = df['geo'].apply(lambda x: codes[country][x])

    return df

@st.cache(ttl = SEC_IN_DAY)
def get_early_leavers(country):
    country = countries[country]
    params = {'geo': country, 'sex': 'T', 'unit': 'PC',
              'age': 'Y18-24' }
    df = client.get_dataset('sdg_04_10', params).to_dataframe()
    df.dropna(inplace = True)
    df['time'] = pd.to_datetime(df['time'])

    return df

@st.cache(ttl = SEC_IN_DAY)
def get_employment_graduates(country):
    country = countries[country]
    params = {'geo': country, 'sex': 'T', 'unit': 'PC',
              'age': 'Y20-34' }
    df = client.get_dataset('tps00053', params).to_dataframe()
    df.dropna(inplace = True)
    df['time'] = pd.to_datetime(df['time'])

    return df


###############################################################################

#Environment

@st.cache(ttl = SEC_IN_DAY)
def get_ghg_emissions(country):
    country = countries[country]
    params = {'geo': country, 'src_crf': 'TOTX4_MEMONIA',
              'unit': 'T_HAB'}
    df = client.get_dataset('sdg_13_10', params).to_dataframe()
    df.dropna(inplace = True)
    df['time'] = pd.to_datetime(df['time'])

    return df

@st.cache(ttl = SEC_IN_DAY)
def get_renewable_pct(country):
    country = countries[country]
    params = {'geo': country, 'nrg_bal': 'REN'}
    df = client.get_dataset('nrg_ind_ren', params).to_dataframe()
    df.dropna(inplace = True)
    df['time'] = pd.to_datetime(df['time'])

    return df

@st.cache(ttl = SEC_IN_DAY)
def get_energy_cons(country):
    country = countries[country]
    params = {'geo': country, 'unit': 'KGOE_HAB',
              'nrg_bal': ['FC_OTH_HH_E', 'FC_IND_E', 'FC_TRA_E'] }
    df = client.get_dataset('nrg_ind_esc', params).to_dataframe()
    df.dropna(inplace = True)

    df['time'] = pd.to_datetime(df['time'])
    df = df.pivot(index = 'time', columns = 'nrg_bal', values = 'values').reset_index()
    
    columns = {'FC_OTH_HH_E': 'Households',
               'FC_IND_E': 'Industry Sector',
               'FC_TRA_E': 'Transport Sector'}
    df.rename(columns = columns, inplace = True)

    return df

@st.cache(ttl = SEC_IN_DAY)
def get_energy_imports(country):
    country = countries[country]
    params = {'geo': country, 'siec': 'TOTAL'}
    df = client.get_dataset('nrg_ind_id', params).to_dataframe()
    df.dropna(inplace = True)
    df['time'] = pd.to_datetime(df['time'])

    return df

@st.cache(ttl = SEC_IN_DAY)
def get_recycling_rate(country):
    country = countries[country]
    params = {'geo': country}
    df = client.get_dataset('cei_wm011', params).to_dataframe()
    df.dropna(inplace = True)
    df['time'] = pd.to_datetime(df['time'])

    return df

@st.cache(ttl = SEC_IN_DAY)
def get_plastic_waste(country):
    country = countries[country]
    params = {'geo': country, 'unit': 'KG_HAB'}
    df = client.get_dataset('cei_pc050', params).to_dataframe()
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