from .datasets import *

option_dict = {
# Economy

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

     'National GDP per Capita (Euros per Inhabitant)': {
        'df_func': get_gdp_capita,
        'category': 'Economy',
        'plot_type': 'line', 
        'columns': 'values',
        'source': '<a href="https://ec.europa.eu/eurostat">Eurostat</a>'
    },

    'Regional GDP per Capita (Euros per Inhabitant)': {
        'df_func': get_gdp_capita_region,
        'category': 'Economy',
        'plot_type': 'choropleth',
        'columns': 'values',
        'source': '<a href="https://ec.europa.eu/eurostat">Eurostat</a>'
    },

    'National Unemployment (Percentage of the Population %)': {
        'df_func': get_unemployment,
        'category': 'Economy',
        'plot_type': 'line',
        'columns': 'values',
        'source': '<a href="https://ec.europa.eu/eurostat">Eurostat</a>'

    },

    'Regional Unemployment (Percentage of the Population %)': {
        'df_func': get_unemployment_region,
        'category': 'Economy',
        'plot_type': 'choropleth',
        'columns': 'values',
        'source': '<a href="https://ec.europa.eu/eurostat">Eurostat</a>'
    },

     'Minimum Wage (Euros per Month) ': {
        'df_func': get_min_wage,
        'category': 'Economy',
        'plot_type': 'line',
        'columns': 'values',
        'source': '<a href="https://ec.europa.eu/eurostat">Eurostat</a>'

    },

    'Inflation Rate (Percentage Change Compared to Previous Year %)': {
        'df_func': get_inflation,
        'category': 'Economy',
        'plot_type': 'bar',
        'columns': 'values',
        'source': '<a href="https://ec.europa.eu/eurostat">Eurostat</a>'

    },

    'Government Gross Debt (Percentage of the GDP %)': {
        'df_func': get_govt_debt,
        'category': 'Economy',
        'plot_type': 'line',
        'columns': 'values',
        'source': '<a href="https://ec.europa.eu/eurostat">Eurostat</a>'

    },

    'Government Budget Balance (Percentage of the GDP %)': {
        'df_func': get_govt_budget,
        'category': 'Economy',
        'plot_type': 'bar',
        'columns': 'values',
        'source': '<a href="https://ec.europa.eu/eurostat">Eurostat</a>'

    },

    # Society

     'National Population (Absolute Number)': {
        'df_func': get_population,
        'category': 'Society',
        'plot_type': 'line',
        'columns': ['Total Population', 'Male Population','Female Population'],
        'source': '<a href="https://ec.europa.eu/eurostat">Eurostat</a>'

    },

     'Regional Population (Absolute Number)': {
        'df_func': get_population_region,
        'category': 'Society',
        'plot_type': 'choropleth',
        'columns': 'values',
        'source': '<a href="https://ec.europa.eu/eurostat">Eurostat</a>'

    },

    'Gender Pay Gap (Percentage of hourly earnings of men %)': {
        'df_func': get_gender_pay_gap,
        'category': 'Society',
        'plot_type': 'line',
        'columns': 'values',
        'source': '<a href="https://ec.europa.eu/eurostat">Eurostat</a>'

    },

    'National Percentage of People at Risk of Poverty (Population %)': {
        'df_func': get_poverty_risk,
        'category': 'Society',
        'plot_type': 'line',
        'columns': 'values',
        'source': '<a href="https://ec.europa.eu/eurostat">Eurostat</a>'

    },

    'Regional Percentage of People at Risk of Poverty (Population %)': {
        'df_func': get_poverty_risk_region,
        'category': 'Society',
        'plot_type': 'choropleth',
        'columns': 'values',
        'source': '<a href="https://ec.europa.eu/eurostat">Eurostat</a>'

    },


    # COVID-19

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