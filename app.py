import streamlit as st
from streamlit import session_state as session
from eustats import *

st.set_page_config(page_title="StatsEuropa", page_icon="📈")

desc = """ 
This dashboard provides statistical indicators and visualizations about European Union countries, 
based on data from reliable sources. You can easily view the graph of your preference, 
by selecting a country and indicator below. Furthermore, it is also possible to display
the data in standard tabular format, as well as download the CSV file. The dashboard was developed by 
[Giannis Tolios](https://giannis.io), using Python and various open source libraries, with the code
being freely available at [Github](https://github.com/derevirn/stats-greece).
I would love to hear your feedback and suggestions, so feel free to
[send me an email](&#109;&#97;&#105;&#108;&#116;&#111;&#58;%64%65%72%65%76%69%72%6e%40%67%6d%61%69%6c%2e%63%6f%6d).  

-----
"""

st.title('StatsEuropa 📈')
st.markdown(desc)

plot_container = st.container()


st.selectbox("Select a Country",  countries.keys(), key = 'country')

col1, col2 = st.columns(2)

col1.selectbox('Select a Category', ['Economy', 'COVID-19'], key = 'category')
col2.selectbox('Select a Statistical Indicator', get_option(), key = 'indicator')

selection = session['indicator']
df_func = option_dict[selection]['df_func']
df = df_func(session['country'])

with st.expander("Display Tabular Dataset"):
    st.dataframe(df)

    st.download_button("Download Dataset (CSV)",
    df.to_csv(index = False, float_format = "%.2f").encode('utf-8'),
    "dataset.csv", "text/csv", key='download-csv') 


figure = create_figure(session['indicator'], option_dict, session['country'])

with plot_container:
    st.write("##### {} - {}".format(session['country'], session['indicator']))
    st.plotly_chart(figure, use_container_width = True)

    source = '<div style="text-align: right; margin-top: -35px"> Source: {}</div>'
    source = source.format(option_dict[selection]['source'])
    st.markdown(source, unsafe_allow_html = True) 


tracking = '''<!-- Default Statcounter code for StatsEuropa
https://eu-stats.herokuapp.com/ -->
<script type="text/javascript">
var sc_project=12751725; 
var sc_invisible=0; 
var sc_security="35d8e5a4"; 
</script>
<script type="text/javascript"
src="https://www.statcounter.com/counter/counter.js"
async></script>
<noscript><div class="statcounter"><a title="Web Analytics"
href="https://statcounter.com/" target="_blank"><img
class="statcounter"
src="https://c.statcounter.com/12751725/0/35d8e5a4/1/"
alt="Web Analytics"
referrerPolicy="no-referrer-when-downgrade"></a></div></noscript>
<!-- End of Statcounter Code --> '''

st.markdown(tracking, unsafe_allow_html = True)