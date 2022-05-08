from .datasets import *

option_dict = {
    
    'National GDP (Current Prices in Billions of Euro)': {
        'df_func': get_gdp,
        'category': 'Economy',
        'plot_type': 'line', 
        'columns': 'values',
        'source': '<a href="https://ec.europa.eu/eurostat">Eurostat</a>'
    },

    'Regional GDP (Current Prices in Billions of Euro)': {
        'df_func': get_gdp_region,
        'category': 'Economy',
        'plot_type': 'choropleth',
        'columns': 'values',
        'source': '<a href="https://ec.europa.eu/eurostat">Eurostat</a>'
    },

    'National Unemployment (Percentage %)': {
        'df_func': get_unemployment,
        'category': 'Economy',
        'plot_type': 'line',
        'columns': 'values',
        'source': '<a href="https://ec.europa.eu/eurostat">Eurostat</a>'

    },

    'Regional Unemployment (Percentage %)': {
        'df_func': get_unemployment_region,
        'category': 'Economy',
        'plot_type': 'choropleth',
        'columns': 'values',
        'source': '<a href="https://ec.europa.eu/eurostat">Eurostat</a>'
    },

    'Daily Confirmed Cases of COVID-19': {
        'df_func': get_new_cases,
        'category': 'COVID-19',
        'plot_type': 'bar',
        'columns': 'values',
        'source': '<a href="https://ourworldindata.org/">Our World in Data</a>'

    },

    'Daily Deaths from COVID-19': {
        'df_func': get_new_deaths,
        'category': 'COVID-19',
        'plot_type': 'bar',
        'columns': 'values',
        'source': '<a href="https://ourworldindata.org/">Our World in Data</a>'

    },

    'Total Confirmed Cases of COVID-19': {
        'df_func': get_total_cases,
        'category': 'COVID-19',
        'plot_type': 'line',
        'columns': 'values',
        'source': '<a href="https://ourworldindata.org/">Our World in Data</a>'

    },

    'Total Confirmed Deaths from COVID-19': {
        'df_func': get_total_deaths,
        'category': 'COVID-19',
        'plot_type': 'line',
        'columns': 'values',
        'source': '<a href="https://ourworldindata.org/">Our World in Data</a>'

    },

    'Vaccinations for COVID-19': {
        'df_func': get_vaccinations,
        'category': 'COVID-19',
        'plot_type': 'line',
        'columns': ['At Least One Dose', 'Fully Vaccinated',
        'Total Vaccinations', 'Booster Dose'],
        'source': '<a href="https://ourworldindata.org/">Our World in Data</a>'

    } 

}