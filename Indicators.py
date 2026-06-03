import streamlit as st
from streamlit import session_state as session
from eustats import *

st.set_page_config(page_title="StatsEuropa", page_icon="📈")

st.title('StatsEuropa 📈')
st.markdown(desc_indicators, unsafe_allow_html = True)

plot_container = st.container()

colA, colB = st.columns(2)
level_help = "Show available indicators on aggregated national level (country) \
              or regional level based on NUTS2"
geo_level = colB.toggle("Toggle National/Regional Indicators", help = level_help)


col1, col2 = st.columns(2)
if geo_level:
    country = col1.selectbox("Select a Country", countries.keys(), index = 10)
else:    
    country = col1.multiselect("Select one or more Countries", countries.keys(),
                                max_selections = 5, default = ['Germany', 'France'])   
    if not country:
        st.warning("⚠️ Please select at least one country.")
        st.stop() 

cat_list = ['Economy', 'Society', 'Health', 'Environment']
category = col2.selectbox('Select a Category', cat_list)
indicator = st.selectbox('Select a Statistical Indicator',
            get_keys(option_regional if geo_level else option_national, category))

df_func = option_regional[indicator]['df_func'] if geo_level else option_national[indicator]['df_func']

if geo_level:
    df = df_func(country)
else:
    df_list = [df_func(count) for count in country]
    df = pd.concat(df_list, ignore_index=True)


if df.shape[0] == 0:
    st.warning("No data available, please select another country or indicator", )
    
 
with st.expander("Display Tabular Dataset"):
    st.dataframe(df.style.format(precision = 2, thousands = ','))

    st.download_button("Download Dataset (CSV)",
    df.to_csv(index = True, float_format = "%.2f").encode('utf-8'),
    "dataset.csv", "text/csv", key='download-csv') 

figure = create_figure(df, option_regional[indicator] if geo_level else option_national[indicator])

country_str = country if isinstance(country, str) else ", ".join(country)
with plot_container:
    st.write("##### {} - {}".format(country_str, indicator))
    st.plotly_chart(figure, use_container_width = True)

    source = '<div style="text-align: right; margin-top: -35px"> Source: {}</div>'
    source = source.format('<a href="https://ec.europa.eu/eurostat">Eurostat</a>')
    st.markdown(source, unsafe_allow_html = True) 



st.markdown(terms)
st.html(footer)
st.html(tracking)