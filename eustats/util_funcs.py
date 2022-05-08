from streamlit import session_state as session
from .options import option_dict

def get_keys(dict_, category):
    arr = []
    for k, v in dict_.items():
        if category in v.values():
            arr.append(k)
    return arr

def get_option():
    if 'category' in session.keys():
        cat = session['category']
        return get_keys(option_dict, cat)
    else:
        return get_keys(option_dict, 'Economy')