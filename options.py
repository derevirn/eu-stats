from datasets import *

option_dict = {
    
    'ΑΕΠ Χώρας σε Δισεκατομμύρια Ευρώ': {
        'df_func': get_df_gdp,
        'category': 'Οικονομία',
        'plot_type': 'line', 
        'columns': 'values',
    },

    'ΑΕΠ Περιφερειών σε Δισεκατομμύρια Ευρώ': {
        'df_func': get_df_gdp_region,
        'category': 'Οικονομία',
        'plot_type': 'choropleth',
        'columns': 'values'
    },

    'Εμβολιασμοί για COVID-19': {
        'df_func': get_vaccinations,
        'category': 'COVID-19',
        'plot_type': 'line',
        'columns': ['Τουλάχιστον 1 Δόση', 'Ολοκληρωμένοι', 'Σύνολο']

    } 

}