import streamlit as st
from streamlit import session_state as session
from figure import create_figure
from options import option_dict
from util_funcs import *
from nuts2 import countries

st.set_page_config(page_title="European Union Statistics", page_icon="📈")

desc = """ 

This dashboard provides statistics and visualizations about countries in the European Union,
that were obtained from official sources. You can simply select the country and indicator 
of your preference, so you can view the associated graph. The dashboard was developed by 
[Giannis Tolios](https://giannis.io), using Python and various open source libraries.
The code is freely available at the [Github repository](https://github.com/derevirn/stats-greece).

**Data Sources:** [Eurostat](https://ec.europa.eu/eurostat/web/main/home), 
[Our World In Data](https://ourworldindata.org/)

-----
"""

st.title('European Union Statistics')
st.markdown(desc)

plot_container = st.container()


st.radio('Επιλέξτε μία Κατηγορία', ['Οικονομία', 'COVID-19'], key = 'radio')
st.selectbox("Select a Country",  countries.keys(), key = 'country')

st.selectbox('Επιλέξτε ένα Στατιστικό Στοιχείο',
            get_option(), key = 'selected')


figure = create_figure(session['selected'], option_dict, session['country'])

with plot_container:
    st.write(session['selected'])
    st.plotly_chart(figure, use_container_width = True)
