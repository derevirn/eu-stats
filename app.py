import streamlit as st
from streamlit import session_state as session
from figure import create_figure
from options import option_dict
from util_funcs import *

desc = """ Η σελίδα αυτή περιλαμβάνει ένα σύνολο στατιστικών στοιχείων
σχετικά με την Ελλάδα. Η σελίδα δημιουργήθηκε από τον [Γιάννη Τόλιο](https://giannis.io),  

Πηγές δεδομένων: [Eurostat](https://ec.europa.eu/eurostat/web/main/home), 
[Our World In Data](https://ourworldindata.org/)

-----
"""

st.title('Στατιστικά Στοιχεία Ελλάδας')
st.markdown(desc)

plot_spot = st.empty()

st.radio('Επιλέξτε μία Κατηγορία', ['Οικονομία', 'COVID-19'], key = 'radio')
st.selectbox('Επιλέξτε ένα Στατιστικό Στοιχείο',
            get_option(), key = 'selected')

figure = create_figure(session['selected'], option_dict)

with plot_spot:
    st.plotly_chart(figure, use_container_width = True)
