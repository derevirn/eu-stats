from datasets import *

option_dict = {
    
    'ΑΕΠ Χώρας - Δισεκατομμύρια Ευρώ': {
        'df_func': get_gdp,
        'category': 'Οικονομία',
        'plot_type': 'line', 
        'columns': 'values',
    },

    'ΑΕΠ Περιφερειών - Δισεκατομμύρια Ευρώ': {
        'df_func': get_gdp_region,
        'category': 'Οικονομία',
        'plot_type': 'choropleth',
        'columns': 'values'
    },

    'Ανεργία - Ποσοστό % ': {
        'df_func': get_unemployment,
        'category': 'Οικονομία',
        'plot_type': 'line',
        'columns': 'values'

    },

    'Ανεργία Περιφερειών - Ποσοστό % ': {
        'df_func': get_unemployment_region,
        'category': 'Οικονομία',
        'plot_type': 'choropleth',
        'columns': 'values'
    },

    'Εμβολιασμοί COVID-19': {
        'df_func': get_vaccinations,
        'category': 'COVID-19',
        'plot_type': 'line',
        'columns': ['Τουλάχιστον 1 Δόση', 'Ολοκληρωμένοι', 'Σύνολο']

    } 

}