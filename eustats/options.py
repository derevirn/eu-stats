from .datasets import *

option_dict = {

    #Economy

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

    'Gini Income Inequality Coefficient (Scale from 0 to 100)': {
        'df_func': get_gini,
        'category': 'Economy',
        'plot_type': 'line',
        'columns': 'values',
        'source': '<a href="https://ec.europa.eu/eurostat">Eurostat</a>'

    },

    #Society

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

    'National Percentage of People at Risk of Poverty or Social Exclusion (Population %)': {
        'df_func': get_poverty_risk,
        'category': 'Society',
        'plot_type': 'line',
        'columns': 'values',
        'source': '<a href="https://ec.europa.eu/eurostat">Eurostat</a>'

    },

    'Regional Percentage of People at Risk of Poverty or Social Exclusion (Population %)': {
        'df_func': get_poverty_risk_region,
        'category': 'Society',
        'plot_type': 'choropleth',
        'columns': 'values',
        'source': '<a href="https://ec.europa.eu/eurostat">Eurostat</a>'

    },

    #Health

    'National Life Expectancy at Birth (Years)': {
        'df_func': get_life_expectancy,
        'category': 'Health',
        'plot_type': 'line',
        'columns': 'values',
        'source': '<a href="https://ec.europa.eu/eurostat">Eurostat</a>'

    },    

    'Regional Life Expectancy at Birth (Years)': {
        'df_func': get_life_expectancy_region,
        'category': 'Health',
        'plot_type': 'choropleth',
        'columns': 'values',
        'source': '<a href="https://ec.europa.eu/eurostat">Eurostat</a>'

    },

    'Healthcare Expenditure (Percentage of GDP %)': {
        'df_func': get_healthcare_expenditure,
        'category': 'Health',
        'plot_type': 'line',
        'columns': 'values',
        'source': '<a href="https://ec.europa.eu/eurostat">Eurostat</a>'

    },

    'Heart Disease Deaths (per 100K Inhabitants)': {
        'df_func': get_heart_deaths,
        'category': 'Health',
        'plot_type': 'choropleth',
        'columns': 'values',
        'source': '<a href="https://ec.europa.eu/eurostat">Eurostat</a>'

    },

    'Cancer Deaths (per 100K inhabitants)': {
        'df_func': get_cancer_deaths,
        'category': 'Health',
        'plot_type': 'choropleth',
        'columns': 'values',
        'source': '<a href="https://ec.europa.eu/eurostat">Eurostat</a>'

    },

    'National Availability of Doctors (per 100K Inhabitants)': {
        'df_func': get_doctors,
        'category': 'Health',
        'plot_type': 'line',
        'columns': 'values',
        'source': '<a href="https://ec.europa.eu/eurostat">Eurostat</a>'

    },  

    'Regional Availability of Doctors (per 100K Inhabitants)': {
        'df_func': get_doctors_region,
        'category': 'Health',
        'plot_type': 'choropleth',
        'columns': 'values',
        'source': '<a href="https://ec.europa.eu/eurostat">Eurostat</a>'

    },  

    'National Availability of Hospital Beds (per 100K Inhabitants)': {
        'df_func': get_hospital_beds,
        'category': 'Health',
        'plot_type': 'line',
        'columns': 'values',
        'source': '<a href="https://ec.europa.eu/eurostat">Eurostat</a>'

    },  

    'Regional Availability of Hospital Beds (per 100K Inhabitants)': {
        'df_func': get_hospital_beds_region,
        'category': 'Health',
        'plot_type': 'choropleth',
        'columns': 'values',
        'source': '<a href="https://ec.europa.eu/eurostat">Eurostat</a>'

    },  


    #Education

    'National Tertiary Educational Attainment at Ages 25-64 (Population %)': {
        'df_func': get_tertiary_attainment,
        'category': 'Education',
        'plot_type': 'line',
        'columns': 'values',
        'source': '<a href="https://ec.europa.eu/eurostat">Eurostat</a>'

    },

    'Regional Tertiary Educational Attainment at Ages 25-64 (Population %)': {
        'df_func': get_tertiary_attainment_region,
        'category': 'Education',
        'plot_type': 'choropleth',
        'columns': 'values',
        'source': '<a href="https://ec.europa.eu/eurostat">Eurostat</a>'

    },

    'Get Early Leavers from Education and Training at Ages 18-24 (Population %)': {
        'df_func': get_early_leavers,
        'category': 'Education',
        'plot_type': 'line',
        'columns': 'values',
        'source': '<a href="https://ec.europa.eu/eurostat">Eurostat</a>'

    },

    'Get Employment Rates of Recent Graduates at Ages 20-34 (Population %)': {
        'df_func': get_employment_graduates,
        'category': 'Education',
        'plot_type': 'line',
        'columns': 'values',
        'source': '<a href="https://ec.europa.eu/eurostat">Eurostat</a>'

    },


    #Environment

    'Greenhouse Gas Emissions (CO2 Equivalent in Tonnes per Capita)': {
        'df_func': get_ghg_emissions,
        'category': 'Environment',
        'plot_type': 'line',
        'columns': 'values',
        'source': '<a href="https://ec.europa.eu/eurostat">Eurostat</a>'

    },

    'Renewable Energy (Percentage of Gross Energy Consumption %)': {
        'df_func': get_renewable_pct,
        'category': 'Environment',
        'plot_type': 'line',
        'columns': 'values',
        'source': '<a href="https://ec.europa.eu/eurostat">Eurostat</a>'

    },

    'Energy Consumption (Kilograms of Oil Equivalent per Capita)': {
        'df_func': get_energy_cons,
        'category': 'Environment',
        'plot_type': 'line',
        'columns': ['Industry Sector', 'Transport Sector', 'Households'],
        'source': '<a href="https://ec.europa.eu/eurostat">Eurostat</a>'

    },

    'Energy Imports Dependency (Percentage of Gross Available Energy %)': {
        'df_func': get_energy_imports,
        'category': 'Environment',
        'plot_type': 'line',
        'columns': 'values',
        'source': '<a href="https://ec.europa.eu/eurostat">Eurostat</a>'

    },

    'Recycling Rate of Municipal Waste (Percentage of Total Waste %)': {
        'df_func': get_recycling_rate,
        'category': 'Environment',
        'plot_type': 'line',
        'columns': 'values',
        'source': '<a href="https://ec.europa.eu/eurostat">Eurostat</a>'

    },

    'Generation of Plastic Packaging Waste (Kilograms per Capita)': {
        'df_func': get_plastic_waste,
        'category': 'Environment',
        'plot_type': 'line',
        'columns': 'values',
        'source': '<a href="https://ec.europa.eu/eurostat">Eurostat</a>'

    },


    #COVID-19

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