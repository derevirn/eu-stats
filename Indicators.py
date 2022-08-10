import streamlit as st
from streamlit import session_state as session
from eustats import *

st.set_page_config(page_title="StatsEuropa", page_icon="📈")

st.title('StatsEuropa 📈')
st.markdown(desc_indicators, unsafe_allow_html = True)

plot_container = st.container()

col1, col2 = st.columns(2)
country = col1.selectbox("Select a Country", countries.keys(), index = 9)
cat_list = ['Economy', 'Health', 'Education', 'Society', 'Environment', 'COVID-19']
category = col2.selectbox('Select a Category', cat_list)
indicator = st.selectbox('Select a Statistical Indicator', get_keys(option_dict, category))

df_func = option_dict[indicator]['df_func']
df = df_func(country)
if df.shape[0] == 0:
    st.warning("No data available, please select another country or indicator", )
 
with st.expander("Display Tabular Dataset"):
    st.dataframe(df.style.format(precision = 2, thousands = ','))

    st.download_button("Download Dataset (CSV)",
    df.to_csv(index = True, float_format = "%.2f").encode('utf-8'),
    "dataset.csv", "text/csv", key='download-csv') 

figure = create_figure(df, option_dict[indicator])

with plot_container:
    st.write("##### {} - {}".format(country, indicator))
    st.plotly_chart(figure, use_container_width = True)

    source = '<div style="text-align: right; margin-top: -35px"> Source: {}</div>'
    source = source.format(option_dict[indicator]['source'])
    st.markdown(source, unsafe_allow_html = True) 


st.markdown(terms)
st.markdown(footer, unsafe_allow_html= True)
st.components.v1.html(tracking)