from .datasets import *

option_national = {

    #Economy

    'National GDP (Current Prices in Billions of Euros)': {
        'df_func': get_gdp,
        'category': 'Economy',
        'plot_type': 'line', 
        'columns': 'values',
        'source': '<a href="https://ec.europa.eu/eurostat">Eurostat</a>'
    },

    'National GDP per Capita (Adjusted for Inflation in Euros)': {
        'df_func': get_gdp_capita,
        'category': 'Economy',
        'plot_type': 'line', 
        'columns': 'values',
        'source': '<a href="https://ec.europa.eu/eurostat">Eurostat</a>'
    },

     'National GDP per Capita (Purchasing Power Standards - EU = 100 )': {
        'df_func': get_gdp_capita_pps,
        'category': 'Economy',
        'plot_type': 'line', 
        'columns': 'values',
        'source': '<a href="https://ec.europa.eu/eurostat">Eurostat</a>'
    },

    'National GDP Growth (Change Compared to Previous Year %)': {
        'df_func': get_gdp_growth,
        'category': 'Economy',
        'plot_type': 'bar', 
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

     'Minimum Wage (Euros per Month) ': {
        'df_func': get_min_wage,
        'category': 'Economy',
        'plot_type': 'line',
        'columns': 'values',
        'source': '<a href="https://ec.europa.eu/eurostat">Eurostat</a>'

    },

    'Inflation Rate (Change Compared to Previous Year %)': {
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
        'columns': 'values',
        'source': '<a href="https://ec.europa.eu/eurostat">Eurostat</a>'

    },

    'National Population Change (Rate per 1000 People)': {
        'df_func': get_population_change,
        'category': 'Society',
        'plot_type': 'bar',
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

    'Intentional Homicides (Rate per 100K Inhabitants)': {
        'df_func': get_homicide_rate,
        'category': 'Society',
        'plot_type': 'line',
        'columns': 'values',
        'source': '<a href="https://ec.europa.eu/eurostat">Eurostat</a>'

    },   

    'Women Killed by Intimate Partner or Family (Rate per 100K Inhabitants)': {
        'df_func': get_femicide_rate,
        'category': 'Society',
        'plot_type': 'line',
        'columns': 'values',
        'source': '<a href="https://ec.europa.eu/eurostat">Eurostat</a>'

    },   

     'Asylum Applicants (Absolute Number)': {
        'df_func': get_asylum_applicants,
        'category': 'Society',
        'plot_type': 'bar',
        'columns': 'values',
        'source': '<a href="https://ec.europa.eu/eurostat">Eurostat</a>'

    },

    'People at Risk of Poverty or Social Exclusion (Population %)': {
        'df_func': get_poverty_risk,
        'category': 'Society',
        'plot_type': 'line',
        'columns': 'values',
        'source': '<a href="https://ec.europa.eu/eurostat">Eurostat</a>'

    },

    'National Tertiary Educational Attainment at Ages 25-64 (Population %)': {
        'df_func': get_tertiary_attainment,
        'category': 'Society',
        'plot_type': 'line',
        'columns': 'values',
        'source': '<a href="https://ec.europa.eu/eurostat">Eurostat</a>'

    },

    'Early Leavers from Education and Training at Ages 18-24 (Population %)': {
        'df_func': get_early_leavers,
        'category': 'Society',
        'plot_type': 'line',
        'columns': 'values',
        'source': '<a href="https://ec.europa.eu/eurostat">Eurostat</a>'

    },

    'Employment Rates of Recent Graduates at Ages 20-34 (Population %)': {
        'df_func': get_employment_graduates,
        'category': 'Society',
        'plot_type': 'line',
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

    'Healthy Life Years at Birth (Years)': {
        'df_func': get_healthy_years,
        'category': 'Health',
        'plot_type': 'line',
        'columns': 'values',
        'source': '<a href="https://ec.europa.eu/eurostat">Eurostat</a>'

    },        

    'Share of People with Good Health (Percentage of Population %)': {
        'df_func': get_population_healthy,
        'category': 'Health',
        'plot_type': 'line',
        'columns': 'values',
        'source': '<a href="https://ec.europa.eu/eurostat">Eurostat</a>'

    },        

    'Unmet Need for Medical Examination/Care (Percentage of Population %)': {
        'df_func': get_unmet_need_health,
        'category': 'Health',
        'plot_type': 'line',
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

    # 'Regional Ischemic Heart Disease Deaths (Rate per 100K Inhabitants)': {
    #     'df_func': get_heart_deaths,
    #     'category': 'Health',
    #     'plot_type': 'choropleth',
    #     'columns': 'values',
    #     'source': '<a href="https://ec.europa.eu/eurostat">Eurostat</a>'

    # },

    'National Cancer Deaths (Rate per 100K inhabitants)': {
        'df_func': get_cancer_deaths,
        'category': 'Health',
        'plot_type': 'line',
        'columns': 'values',
        'source': '<a href="https://ec.europa.eu/eurostat">Eurostat</a>'

    },

    'National Deaths due to Suicide (Rate per 100K Inhabitants)': {
        'df_func': get_suicide_rate,
        'category': 'Health',
        'plot_type': 'line',
        'columns': 'values',
        'source': '<a href="https://ec.europa.eu/eurostat">Eurostat</a>'

    },   

    'National Availability of Doctors': {
        'df_func': get_doctors,
        'category': 'Health',
        'plot_type': 'line',
        'columns': 'values',
        'source': '<a href="https://ec.europa.eu/eurostat">Eurostat</a>'

    },  


    'National Availability of Hospital Beds (Rate per 100K Inhabitants)': {
        'df_func': get_hospital_beds,
        'category': 'Health',
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

}

option_regional = {

    'Regional GDP (Current Prices in Billions of Euro)': {
        'df_func': get_gdp_region,
        'category': 'Economy',
        'plot_type': 'choropleth',
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

    'Regional GDP per Capita (Purchasing Power Standards - EU = 100 )': {
        'df_func': get_gdp_capita_pps_region,
        'category': 'Economy',
        'plot_type': 'choropleth', 
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

    'Regional Population (Absolute Number)': {
        'df_func': get_population_region,
        'category': 'Society',
        'plot_type': 'choropleth',
        'columns': 'values',
        'source': '<a href="https://ec.europa.eu/eurostat">Eurostat</a>'

    },

    'Regional Tertiary Educational Attainment at Ages 25-64 (Population %)': {
        'df_func': get_tertiary_attainment_region,
        'category': 'Society',
        'plot_type': 'choropleth',
        'columns': 'values',
        'source': '<a href="https://ec.europa.eu/eurostat">Eurostat</a>'

    },    

    'People at Risk of Poverty or Social Exclusion (Population %)': {
        'df_func': get_poverty_risk_region,
        'category': 'Society',
        'plot_type': 'choropleth',
        'columns': 'values',
        'source': '<a href="https://ec.europa.eu/eurostat">Eurostat</a>'

    },

    'Regional Cancer Deaths (Rate per 100K inhabitants)': {
        'df_func': get_cancer_deaths_region,
        'category': 'Health',
        'plot_type': 'choropleth',
        'columns': 'values',
        'source': '<a href="https://ec.europa.eu/eurostat">Eurostat</a>'

    },

    'Regional Availability of Doctors': {
        'df_func': get_doctors_region,
        'category': 'Health',
        'plot_type': 'choropleth',
        'columns': 'values',
        'source': '<a href="https://ec.europa.eu/eurostat">Eurostat</a>'

    },  


    'Regional Availability of Hospital Beds (Rate per 100K Inhabitants)': {
        'df_func': get_hospital_beds_region,
        'category': 'Health',
        'plot_type': 'choropleth',
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
}