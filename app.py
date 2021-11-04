import streamlit as st
from figure import create_figure
from options import option_dict
from streamlit import experimental_rerun


def get_keys(dict_, category):
    arr = []
    for k, v in dict_.items():
        if category in v.values():
            arr.append(k)
    return arr

def get_selection():
    if 'selected' in st.session_state.keys():
        return st.session_state['selected']
    else: 
        return 'ΑΕΠ Χώρας σε Δισεκατομμύρια Ευρώ'


desc = """ Η σελίδα αυτή περιλαμβάνει ένα σύνολο στατιστικών στοιχείων
σχετικά με την Ελλάδα. Η σελίδα δημιουργήθηκε από τον [Γιάννη Τόλιο](https://giannis.io),  

Πηγές δεδομένων: Eurostat

"""

st.title('Στατιστικά Στοιχεία της Ελλάδας')
st.markdown(desc)

selection = get_selection()
figure = create_figure(selection, option_dict)

st.plotly_chart(figure, use_container_width = True)


st.selectbox('Επιλέξτε ένα στατιστικό στοιχείο',
             option_dict.keys(), key = 'selected')

print(st.session_state)


