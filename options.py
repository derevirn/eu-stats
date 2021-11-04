from datasets import *

option_dict = {
    
    'ΑΕΠ Χώρας σε Δισεκατομμύρια Ευρώ': {
        'df_func': get_df_gdp,
        'category': 'economy',
        'plot_type': 'line', 
        'columns': 'values',
    },

    'ΑΕΠ Περιφερειών σε Δισεκατομμύρια Ευρώ': {
        'df_func': get_df_gdp_region,
        'category': 'economy',
        'plot_type': 'choropleth',
        'columns': 'values'
    },

    'Εμβολιασμοί για COVID-19': {
        'df_func': get_vaccinations,
        'category': 'covid-19',
        'plot_type': 'line',
        'columns': ['Εμβολιασμοί με Τουλάχιστον 1 Δόση', 'Ολοκληρωμένοι Εμβολιασμοί',
                    'Εμβολιασμοί Αναμνηστικής Δόσης', 'Σύνολο Εμβολιασμών']

    } 

}