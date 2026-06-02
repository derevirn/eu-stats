import pandas as pd
import streamlit as st
from eurostatapiclient import EurostatAPIClient
from .nuts2 import *

SEC_IN_DAY = 86400
client = EurostatAPIClient('1.0', 'json', 'en')

###############################################################################

#Economy

@st.cache_data(ttl = SEC_IN_DAY)
def get_gdp(country):
    country = countries[country]
    params = {'geo': country, 'unit': 'CP_MEUR', 'na_item': 'B1GQ'}
    df = client.get_dataset('nama_10_gdp', params).to_dataframe()
    df.dropna(inplace = True)
    df['values'] = df['values'] / 1000
    df['time'] = pd.to_datetime(df['time'])
    
    return df

@st.cache_data(ttl = SEC_IN_DAY)
def get_gdp_region(country):
    country = countries[country]
    params = {'unit': 'MIO_EUR', 'geo': codes[country], 'lastTimePeriod': 2}
    df = client.get_dataset('nama_10r_2gdp', params).to_dataframe()
    df.dropna(inplace = True)
    df['region_name'] = df['geo'].apply(lambda x: codes[country][x])
    df['values'] = df['values'] / 1000
    df['time'] = pd.to_datetime(df['time']) 

    return df

@st.cache_data(ttl = SEC_IN_DAY)
def get_gdp_capita(country):
    country = countries[country]
    params = {'geo': country, 'unit': 'CLV20_EUR_HAB', 'na_item': 'B1GQ'}
    df = client.get_dataset('nama_10_pc', params).to_dataframe()
    df.dropna(inplace = True)
    df['time'] = pd.to_datetime(df['time'])
    
    return df

@st.cache_data(ttl = SEC_IN_DAY)
def get_gdp_capita_pps(country):
    country = countries[country]
    params = {'geo': country}
    df = client.get_dataset('tec00114', params).to_dataframe()
    df.dropna(inplace = True)
    df['time'] = pd.to_datetime(df['time'])
    
    return df

@st.cache_data(ttl = SEC_IN_DAY)
def get_gdp_growth(country):
    country = countries[country]
    params = {'geo': country, 'unit': 'CLV_PCH_PRE'}
    df = client.get_dataset('tec00115', params).to_dataframe()
    df.dropna(inplace = True)
    df['time'] = pd.to_datetime(df['time'])
    
    return df

@st.cache_data(ttl = SEC_IN_DAY)
def get_gdp_capita_region(country):
    country = countries[country]
    params = {'unit': 'EUR_HAB', 'geo': codes[country], 'lastTimePeriod': 2}
    df = client.get_dataset('nama_10r_2gdp', params).to_dataframe()
    df.dropna(inplace = True)
    df['region_name'] = df['geo'].apply(lambda x: codes[country][x])
    df['time'] = pd.to_datetime(df['time'])

    return df

@st.cache_data(ttl = SEC_IN_DAY)
def get_gdp_capita_pps_region(country):
    country = countries[country]
    params = {'unit': 'PPS_HAB_EU27_2020', 'geo': codes[country], 'lastTimePeriod': 2}
    df = client.get_dataset('nama_10r_2gdp', params).to_dataframe()
    df.dropna(inplace = True)
    df['region_name'] = df['geo'].apply(lambda x: codes[country][x])
    df['time'] = pd.to_datetime(df['time'])

    return df

@st.cache_data(ttl = SEC_IN_DAY)
def get_govt_debt(country):
    country = countries[country]
    params = {'geo': country, 'unit': 'PC_GDP',
              'sector': 'S13', 'na_item': 'GD'}
    df = client.get_dataset('gov_10dd_edpt1', params).to_dataframe()
    df.dropna(inplace = True)
    df['time'] = pd.to_datetime(df['time'])
    
    return df

@st.cache_data(ttl = SEC_IN_DAY)
def get_govt_budget(country):
    country = countries[country]
    params = {'geo': country, 'unit': 'PC_GDP',
              'sector': 'S13', 'na_item': 'B9'}
    df = client.get_dataset('gov_10dd_edpt1', params).to_dataframe()
    df.dropna(inplace = True)
    df['time'] = pd.to_datetime(df['time'])
    
    return df


@st.cache_data(ttl = SEC_IN_DAY)
def get_unemployment(country):
    country = countries[country]
    params = {'geo': country, 's_adj': 'SA', 'indic': 'LM-UN-T-TOT'}
    df = client.get_dataset('ei_lmhr_m', params).to_dataframe()
    df.dropna(inplace = True)
    df['time'] = pd.to_datetime(df['time'])

    return df

@st.cache_data(ttl = SEC_IN_DAY)
def get_unemployment_region(country):
    country = countries[country]
    params = {'sex': 'T', 'geo': codes[country], 'age': 'Y15-74',
          'isced11': 'TOTAL', 'lastTimePeriod': 2}
    df = client.get_dataset('lfst_r_lfu3rt', params).to_dataframe()
    df.dropna(inplace = True)
    df['region_name'] = df['geo'].apply(lambda x: codes[country][x])
    df['time'] = pd.to_datetime(df['time'])

    return df

@st.cache_data(ttl = SEC_IN_DAY)
def get_min_wage(country):
    country = countries[country]
    params = {'geo': country, 'currency': 'EUR'}
    df = client.get_dataset('earn_mw_cur', params).to_dataframe()
    df.dropna(inplace = True)
    df['time'] = df['time'].str.replace('S1','-01-01')
    df['time'] = df['time'].str.replace('S2','-07-01')
    df['time'] = pd.to_datetime(df['time'])

    return df


@st.cache_data(ttl = SEC_IN_DAY)
def get_inflation(country):

    country = countries[country]
    params = {'geo': country, 'coicop': 'CP00'}
    df = client.get_dataset('prc_hicp_aind', params).to_dataframe()
    df.dropna(inplace = True)
    mask = df['unit'] == 'RCH_A_AVG'
    df = df[mask]
    df['time'] = pd.to_datetime(df['time'])

    return df

@st.cache_data(ttl = SEC_IN_DAY)
def get_gini(country):
    country = countries[country]
    params = {'geo': country, 'age': 'TOTAL'}
    df = client.get_dataset('ilc_di12', params).to_dataframe()
    df.dropna(inplace = True)
    df['time'] = pd.to_datetime(df['time'])

    return df


###############################################################################

#Society 

@st.cache_data(ttl = SEC_IN_DAY)
def get_population(country):
    country = countries[country]
    params = {'geo': country, 'indic_de': 'JAN'}
    df = client.get_dataset('demo_gind', params).to_dataframe()
    df.dropna(inplace = True)
    df['time'] = pd.to_datetime(df['time'])

    return df

@st.cache_data(ttl = SEC_IN_DAY)
def get_population_change(country):
    country = countries[country]
    params = {'geo': country, 'indic_de': 'GROWRT'}
    df = client.get_dataset('tps00019', params).to_dataframe()
    df.dropna(inplace = True)
    df['time'] = pd.to_datetime(df['time'])

    return df

@st.cache_data(ttl = SEC_IN_DAY)
def get_population_region(country):
    country = countries[country]
    params = {'geo': codes[country], 'sex': 'T',
              'age': 'TOTAL', 'lastTimePeriod': 2}
    df = client.get_dataset('demo_r_d2jan', params).to_dataframe()
    df.dropna(inplace = True)
    df['region_name'] = df['geo'].apply(lambda x: codes[country][x])
    df['time'] = pd.to_datetime(df['time'])

    return df

@st.cache_data(ttl = SEC_IN_DAY)
def get_population_density_region(country):
    country = countries[country]
    params = {'geo': codes[country], 'lastTimePeriod': 2}
    df = client.get_dataset('tgs00024', params).to_dataframe()
    df.dropna(inplace = True)
    df['region_name'] = df['geo'].apply(lambda x: codes[country][x])
    df['time'] = pd.to_datetime(df['time'])

    return df

@st.cache_data(ttl = SEC_IN_DAY)
def get_poverty_risk(country):
    country = countries[country]
    params = {'geo': country, 'age': 'TOTAL', 'unit': 'PC'}
    df = client.get_dataset('sdg_01_10', params).to_dataframe()
    df.dropna(inplace = True)
    df['time'] = pd.to_datetime(df['time'])

    return df

@st.cache_data(ttl = SEC_IN_DAY)
def get_asylum_applicants(country):
    country = countries[country]
    params = {'geo': country, 'applicant': 'TOTAL' }
    df = client.get_dataset('tps00191', params).to_dataframe()
    df.dropna(inplace = True)
    df['time'] = pd.to_datetime(df['time'])

    return df

@st.cache_data(ttl = SEC_IN_DAY)
def get_poverty_risk_region(country):
    country = countries[country]
    params = {'geo': codes[country], 'lastTimePeriod': 2}
    df = client.get_dataset('ilc_peps11n', params).to_dataframe()
    df.dropna(inplace = True)
    df['region_name'] = df['geo'].apply(lambda x: codes[country][x])
    df['time'] = pd.to_datetime(df['time'])

    return df


@st.cache_data(ttl = SEC_IN_DAY)
def get_gender_pay_gap(country):
    country = countries[country]
    params = {'geo': country}
    df = client.get_dataset('sdg_05_20', params).to_dataframe()
    df.dropna(inplace = True)
    df['time'] = pd.to_datetime(df['time'])

    return df

@st.cache_data(ttl = SEC_IN_DAY)
def get_homicide_rate(country):
    country = countries[country]
    params = {'geo': country, 'iccs': 'ICCS0101',
              'unit': 'P_HTHAB'}
    df = client.get_dataset('crim_off_cat', params).to_dataframe()
    df.dropna(inplace = True)
    df['time'] = pd.to_datetime(df['time'])

    return df

@st.cache_data(ttl = SEC_IN_DAY)
def get_femicide_rate(country):
    country = countries[country]
    params = {'geo': country, 'sex': 'F',
              'pers_cat': 'IPTN_FAM', 'unit': 'P_HTHAB' }
    df = client.get_dataset('crim_hom_vrel', params).to_dataframe()
    df.dropna(inplace = True)
    df['time'] = pd.to_datetime(df['time'])

    return df

##############################################################################

#Health

@st.cache_data(ttl = SEC_IN_DAY)
def get_life_expectancy(country):
    country = countries[country]
    params = {'geo': country, 'sex': 'T', 'age': 'Y_LT1' }
    df = client.get_dataset('demo_mlexpec', params).to_dataframe()
    df.dropna(inplace = True)
    df['time'] = pd.to_datetime(df['time'])

    return df

@st.cache_data(ttl = SEC_IN_DAY)
def get_healthy_years(country):
    country = countries[country]
    params = {'geo': country, 'sex': 'T' }
    df = client.get_dataset('tps00150', params).to_dataframe()
    df.dropna(inplace = True)
    df['time'] = pd.to_datetime(df['time'])

    return df

@st.cache_data(ttl = SEC_IN_DAY)
def get_population_healthy(country):
    country = countries[country]
    params = {'geo': country, 'sex': 'T' }
    df = client.get_dataset('sdg_03_20', params).to_dataframe()
    df.dropna(inplace = True)
    df['time'] = pd.to_datetime(df['time'])

    return df

@st.cache_data(ttl = SEC_IN_DAY)
def get_unmet_need_health(country):
    country = countries[country]
    params = {'geo': country, 'sex': 'T' }
    df = client.get_dataset('sdg_03_60', params).to_dataframe()
    df.dropna(inplace = True)
    df['time'] = pd.to_datetime(df['time'])

    return df


@st.cache_data(ttl = SEC_IN_DAY)
def get_life_expectancy_region(country):
    country = countries[country]
    params = {'sex': 'T', 'geo': codes[country], 'lastTimePeriod': 2}
    df = client.get_dataset('tgs00101', params).to_dataframe()
    df.dropna(inplace = True)
    df['region_name'] = df['geo'].apply(lambda x: codes[country][x]) 

    return df

@st.cache_data(ttl = SEC_IN_DAY)
def get_doctors(country):
    country = countries[country]
    params = {'geo': country, 'unit': 'NR',
              'age': 'TOTAL', 'sex': 'T' }
    df = client.get_dataset('hlth_rs_phys', params).to_dataframe()
    df.dropna(inplace = True)
    df['time'] = pd.to_datetime(df['time'])

    return df

@st.cache_data(ttl = SEC_IN_DAY)
def get_doctors_region(country):
    country = countries[country]
    params = {'geo': codes[country], 'unit': 'NR', 'lastTimePeriod': 2}
    df = client.get_dataset('hlth_rs_physreg', params).to_dataframe()
    df.dropna(inplace = True)
    df['region_name'] = df['geo'].apply(lambda x: codes[country][x])

    return df

@st.cache_data(ttl = SEC_IN_DAY)
def get_healthcare_expenditure(country):
    country = countries[country]
    params = {'geo': country, 'unit': 'PC_GDP', 'icha11_hc': 'TOT_HC'}
    df = client.get_dataset('hlth_sha11_hc', params).to_dataframe()
    df.dropna(inplace = True)
    df['time'] = pd.to_datetime(df['time'])

    return df


@st.cache_data(ttl = SEC_IN_DAY)
def get_hospital_beds(country):
    country = countries[country]
    params = {'geo': country, 'unit': 'P_HTHAB',
              'facility': 'HBEDT' }
    df = client.get_dataset('tps00046', params).to_dataframe()
    df.dropna(inplace = True)
    df['time'] = pd.to_datetime(df['time'])

    return df

@st.cache_data(ttl = SEC_IN_DAY)
def get_hospital_beds_region(country):
    country = countries[country]
    params = {'geo': codes[country], 'unit': 'P_HTHAB',
             'lastTimePeriod': 2}
    df = client.get_dataset('hlth_rs_bdsrg2', params).to_dataframe()
    df.dropna(inplace = True)
    df['region_name'] = df['geo'].apply(lambda x: codes[country][x]) 

    return df

@st.cache_data(ttl = SEC_IN_DAY)
def get_heart_deaths(country):
    country = countries[country]
    params = {'geo': country, 'sex': 'T',
              'age': 'TOTAL', 'icd10': 'I20-I25'}
    df = client.get_dataset('hlth_cd_asdr2', params).to_dataframe()
    df.dropna(inplace = True)
    df['time'] = pd.to_datetime(df['time'])
    
    return df

@st.cache_data(ttl = SEC_IN_DAY)
def get_heart_deaths_region(country):
    country = countries[country]
    params = {'geo': codes[country], 'lastTimePeriod': 2}
    df = client.get_dataset('tgs00059', params).to_dataframe()
    df.dropna(inplace = True)
    df['region_name'] = df['geo'].apply(lambda x: codes[country][x])
    
    return df

@st.cache_data(ttl = SEC_IN_DAY)
def get_suicide_rate(country):
    country = countries[country]
    params = {'geo': country, 'sex': 'T'}
    df = client.get_dataset('tps00122', params).to_dataframe()
    df.dropna(inplace = True)
    df['time'] = pd.to_datetime(df['time'])

    return df

@st.cache_data(ttl = SEC_IN_DAY)
def get_cancer_deaths(country):
    country = countries[country]
    params = {'geo': country, 'sex': 'T'}
    df = client.get_dataset('tps00116', params).to_dataframe()
    df.dropna(inplace = True)
    df['time'] = pd.to_datetime(df['time'])
    
    return df

@st.cache_data(ttl = SEC_IN_DAY)
def get_cancer_deaths_region(country):
    country = countries[country]
    params = {'geo': codes[country], 'lastTimePeriod': 2}
    df = client.get_dataset('tgs00058', params).to_dataframe()
    df.dropna(inplace = True)
    df['region_name'] = df['geo'].apply(lambda x: codes[country][x])
    
    return df


###############################################################################

#Education

@st.cache_data(ttl = SEC_IN_DAY)
def get_tertiary_attainment(country):
    country = countries[country]
    params = {'geo': country, 'sex': 'T', 'unit': 'PC',
              'age': 'Y25-64', 'isced11': 'ED5-8'  }
    df = client.get_dataset('edat_lfse_03', params).to_dataframe()
    df.dropna(inplace = True)
    df['time'] = pd.to_datetime(df['time'])

    return df


@st.cache_data(ttl = SEC_IN_DAY)
def get_tertiary_attainment_region(country):
    country = countries[country]
    params = {'geo': codes[country], 'sex': 'T', 'unit': 'PC',
              'age': 'Y25-64', 'isced11': 'ED5-8', 'lastTimePeriod': 2}
    df = client.get_dataset('edat_lfse_04', params).to_dataframe()
    df.dropna(inplace = True)
    df['region_name'] = df['geo'].apply(lambda x: codes[country][x])

    return df

@st.cache_data(ttl = SEC_IN_DAY)
def get_early_leavers(country):
    country = countries[country]
    params = {'geo': country, 'sex': 'T', 'unit': 'PC',
              'age': 'Y18-24' }
    df = client.get_dataset('sdg_04_10', params).to_dataframe()
    df.dropna(inplace = True)
    df['time'] = pd.to_datetime(df['time'])

    return df

@st.cache_data(ttl = SEC_IN_DAY)
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

@st.cache_data(ttl = SEC_IN_DAY)
def get_ghg_emissions(country):
    country = countries[country]
    params = {'geo': country, 'src_crf': 'TOTX4_MEMO',
              'unit': 'MTCO2E'}
    df = client.get_dataset('sdg_13_10', params).to_dataframe()
    df.dropna(inplace = True)
    df['time'] = pd.to_datetime(df['time'])

    return df

@st.cache_data(ttl = SEC_IN_DAY)
def get_ghg_emissions_capita(country):
    country = countries[country]
    params = {'geo': country, 'src_crf': 'TOTX4_MEMO',
              'unit': 'T_HAB'}
    df = client.get_dataset('sdg_13_10', params).to_dataframe()
    df.dropna(inplace = True)
    df['time'] = pd.to_datetime(df['time'])

    return df

@st.cache_data(ttl = SEC_IN_DAY)
def get_renewable_pct(country):
    country = countries[country]
    params = {'geo': country, 'nrg_bal': 'REN'}
    df = client.get_dataset('nrg_ind_ren', params).to_dataframe()
    df.dropna(inplace = True)
    df['time'] = pd.to_datetime(df['time'])

    return df

@st.cache_data(ttl = SEC_IN_DAY)
def get_energy_cons(country):
    country = countries[country]
    params = {'geo': country, 'unit': 'TOE_HAB'}
    df = client.get_dataset('sdg_07_10', params).to_dataframe()
    df.dropna(inplace = True)
    df['time'] = pd.to_datetime(df['time'])
    return df

@st.cache_data(ttl = SEC_IN_DAY)
def get_energy_imports(country):
    country = countries[country]
    params = {'geo': country, 'siec': 'TOTAL'}
    df = client.get_dataset('nrg_ind_id', params).to_dataframe()
    df.dropna(inplace = True)
    df['time'] = pd.to_datetime(df['time'])

    return df

@st.cache_data(ttl = SEC_IN_DAY)
def get_electricity_prices(country):
    country = countries[country]
    params = {'geo': country, 'currency': 'EUR', 
              'nrg_cons': 'KWH2500-4999', 'tax': 'I_TAX', }
    df = client.get_dataset('nrg_pc_204', params).to_dataframe()
    df.dropna(inplace = True)
    df['time'] = df['time'].str.replace('S1','-01-01')
    df['time'] = df['time'].str.replace('S2','-07-01')
    df['time'] = pd.to_datetime(df['time'])

    return df

@st.cache_data(ttl = SEC_IN_DAY)
def get_recycling_rate(country):
    country = countries[country]
    params = {'geo': country}
    df = client.get_dataset('cei_wm011', params).to_dataframe()
    df.dropna(inplace = True)
    df['time'] = pd.to_datetime(df['time'])

    return df

@st.cache_data(ttl = SEC_IN_DAY)
def get_plastic_waste(country):
    country = countries[country]
    params = {'geo': country, 'unit': 'KG_HAB'}
    df = client.get_dataset('cei_pc050', params).to_dataframe()
    df.dropna(inplace = True)
    df['time'] = pd.to_datetime(df['time'])

    return df



###############################################################################

#COVID-19

@st.cache_data(ttl = SEC_IN_DAY)
def get_new_cases(country):
    df = pd.read_csv('https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/cases_deaths/new_cases.csv')
    df['date'] = pd.to_datetime(df['date'])
    cols = ['date', country]
    df = df[cols]
    df.rename(columns = {'date': 'time', country: 'values'}, inplace = True)
    df.dropna(inplace = True)

    return df

@st.cache_data(ttl = SEC_IN_DAY)
def get_new_deaths(country):
    df = pd.read_csv('https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/cases_deaths/new_deaths.csv')
    df['date'] = pd.to_datetime(df['date'])
    cols = ['date', country]
    df = df[cols]
    df.rename(columns = {'date': 'time', country: 'values'}, inplace = True)
    df.dropna(inplace = True)
    
    return df

@st.cache_data(ttl = SEC_IN_DAY)
def get_total_cases(country):
    df = pd.read_csv('https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/cases_deaths/total_cases.csv')
    df['date'] = pd.to_datetime(df['date'])
    cols = ['date', country]
    df = df[cols]
    df.rename(columns = {'date': 'time', country: 'values'}, inplace = True)
    df.dropna(inplace = True)
    
    return df

@st.cache_data(ttl = SEC_IN_DAY)
def get_total_deaths(country):
    df = pd.read_csv('https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/cases_deaths/total_deaths.csv')
    df['date'] = pd.to_datetime(df['date'])
    cols = ['date', country]
    df = df[cols]
    df.rename(columns = {'date': 'time', country: 'values'}, inplace = True)
    df.dropna(inplace = True)
    
    return df

@st.cache_data(ttl = SEC_IN_DAY)
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