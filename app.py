import streamlit as st
from datasets import get_data
import plotly.graph_objects as go
import plotly.express as px

option_dict = {'ΑΕΠ Χώρας σε Δισεκατομμύρια Ευρώ': 'GDP', 'τεστ': 'test'}

def get_selection():
    if 'option' in st.session_state.keys():
        return st.session_state['option']
    else: 
        return 'ΑΕΠ Χώρας σε Δισεκατομμύρια Ευρώ'

def create_plot():

    select_  = option_dict[get_selection()]

    if select_ == 'GDP':
        fig = px.line(data_frame = data[select_], y='values',
        title = get_selection())
        fig.update_layout(xaxis_title = '', yaxis_title = '',
                          plot_bgcolor = 'white',
                          margin=dict(l=1, r=1, t=25, b=1, pad=1))
    else:
        fig = px.scatter(data[select_], y = 'y', x = 'x',
                         title = get_selection())
        fig.update_layout(xaxis_title = '', yaxis_title = '',
                          margin=dict(l=20, r=20, t=20, b=20))


    st.plotly_chart(fig, use_container_width = True)


data = get_data()


desc = """ Η σελίδα αυτή περιλαμβάνει ένα σύνολο στατιστικών στοιχείων
σχετικά με την Ελλάδα. Η σελίδα δημιουργήθηκε από τον [Γιάννη Τόλιο](https://giannis.io),  

Πηγές δεδομένων: Eurostat

"""

st.title('Στατιστικά Στοιχεία της Ελλάδας')
st.markdown(desc)

st.subheader("Οικονομικά Στοιχεία Χώρας")


create_plot()

st.selectbox('Επιλέξτε ένα στατιστικό στοιχείο',
             option_dict.keys(), index = 0, key = 'option')  


