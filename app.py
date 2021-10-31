import streamlit as st
from urllib.request import urlopen
import json
import plotly.express as px
from datasets import get_data
from figure import create_figure

option_dict = {'ΑΕΠ Χώρας σε Δισεκατομμύρια Ευρώ': 'GDP',
               'ΑΕΠ Περιφερειών σε Δισεκατομμύρια Ευρώ': 'GDP_region'}

def get_selection():
    if 'option' in st.session_state.keys():
        return st.session_state['option']
    else: 
        return 'ΑΕΠ Χώρας σε Δισεκατομμύρια Ευρώ'


data = get_data()


desc = """ Η σελίδα αυτή περιλαμβάνει ένα σύνολο στατιστικών στοιχείων
σχετικά με την Ελλάδα. Η σελίδα δημιουργήθηκε από τον [Γιάννη Τόλιο](https://giannis.io),  

Πηγές δεδομένων: Eurostat

"""

st.title('Στατιστικά Στοιχεία της Ελλάδας')
st.markdown(desc)

st.subheader("Οικονομικά Στοιχεία Χώρας")


selection = get_selection()
figure = create_figure(data, selection, option_dict)

st.plotly_chart(figure, use_container_width = True)

st.selectbox('Επιλέξτε ένα στατιστικό στοιχείο',
             option_dict.keys(), index = 0, key = 'option')  


