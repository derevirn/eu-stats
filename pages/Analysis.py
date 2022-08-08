import os, sys
sys.path.insert(1, os.path.abspath('..'))
from eustats import *
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import plotly.express as px

plt.style.use('seaborn-whitegrid')
mpl.rcParams['figure.dpi'] = 300
st.set_page_config(page_title="StatsEuropa", page_icon="📈")

desc = """ 
This pages provides statistical analysis for NUTS 2 regions of the European Union. 
You can also visit the <a href ="/Indicators" target = "_self">Indicators</a> page.

-----
"""

st.title('StatsEuropa 📈')
st.markdown(desc, unsafe_allow_html= True)

df = pd.read_csv('data/eu_regional_data.csv')
df_pca = pd.read_csv('data/eu_regional_data_pca.csv')
num_cols = list(df.columns[2:])

tab_str = ['Descriptive Statistics', 'Linear Regression',
           'Principal Component Analysis']
tab1, tab2, tab3 = st.tabs(tab_str)

with tab1:

    st.markdown('##### Descriptive Statistics for NUTS 2 Region Data')
    with st.expander("Distribution Plot for NUTS 2 Region Data", expanded = True):

        desc_cont= st.container()
        col3, col4 = st.columns(2)
        variable = col3.selectbox('Select Variable: ', options = num_cols, index = 1)
        plot_type = col4.selectbox('Select Plot: ', options = ['KDE Plot', 'Box Plot'])

        with desc_cont:
            if plot_type == 'KDE Plot':
                fig1 = kde_plot(df, variable)
                st.pyplot(fig1)

            elif plot_type == 'Box Plot':
                fig1 = box_plot(df, variable)
                st.plotly_chart(fig1, use_container_width = True)

    with st.expander("Correlation Heatmap for NUTS 2 Region Data"):
        fig = correlation_heatmap(df)
        st.pyplot(fig)

    with st.expander("Display NUTS 2 Region Tabular Dataset"):
        #df.set_index('region_name', inplace = True)
        st.dataframe(df)

        st.download_button("Download Dataset (CSV)",
        df.to_csv(index = False, float_format = "%.2f").encode('utf-8'),
        "nuts2_dataset.csv", "text/csv", key='download-csv') 

with tab2:

    st.markdown('##### Linear Regression Modeling for NUTS 2 Region Data')
    st.markdown('You can hover/click on the regression line to view the coefficients \
                   and R-Squared metric.')

    lin_reg_cont = st.container()

    col1, col2 = st.columns(2)
    iv = col1.selectbox('Select X (Independent Variable): ', options = num_cols, index = 1 )
    dv = col2.selectbox('Select Y (Dependent Variable): ', options = num_cols, index = 3)
    show_res = st.checkbox("Display Model Summary", value = False)

    with lin_reg_cont:
        fig2 = lin_reg_plot(df, x = iv, y = dv)
        summary = px.get_trendline_results(fig2).px_fit_results.iloc[0].summary()
        st.plotly_chart(fig2, use_container_width = True)
        if show_res :st.write(summary)

with tab3:

    st.markdown('##### Principal Component Analysis (PCA) Plot for NUTS 2 Region Data')

    fig3 = pca_plot(df_pca)
    st.plotly_chart(fig3, use_container_width = True)


terms = ''' &nbsp; 

-------------------
##### Privacy & Terms

**Privacy**

No user data are collected, apart from basic analytics like number of visitors and pageviews,
provided by the StatCounter service. You can [click here](https://statcounter.com/about/legal/)
to read their privacy policy.  

**Terms of Use**

You are free to use any plots or datasets that are available on this website, 
under the term of giving appropriate credit and referencing [StatsEuropa.eu](https://statseuropa.eu).

--------------------
'''

st.markdown(terms)

st.markdown(footer, unsafe_allow_html= True)
