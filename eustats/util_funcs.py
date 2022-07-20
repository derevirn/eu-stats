from streamlit import session_state as session
from .options import option_dict

def get_keys(dict_, category):
    arr = []
    for k, v in dict_.items():
        if category in v.values():
            arr.append(k)
    return arr