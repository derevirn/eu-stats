import os, sys
sys.path.insert(1, os.path.abspath('..'))
from eustats import *
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import plotly.express as px
from statsmodels.stats.descriptivestats import describe

plt.style.use('seaborn-whitegrid')
mpl.rcParams['figure.dpi'] = 300
st.set_page_config(page_title="StatsEuropa", page_icon="📈")

desc = """ 
This page provides statistical analysis for NUTS 2 regions of the European Union. 
You can also visit the <a href ="/Indicators" target = "_self">Indicators</a> page.

-----
"""

st.title('StatsEuropa 📈')
st.markdown(desc, unsafe_allow_html= True)

df = pd.read_csv('data/eu_regional_data.csv')
df_pca = pd.read_csv('data/eu_regional_data_pca.csv')
num_cols = list(df.columns[3:])

tab_str = ['Descriptive Statistics', 'Regression Modeling',
           'Principal Component Analysis']
tab1, tab2, tab3 = st.tabs(tab_str)

with tab1:

    st.markdown('##### Descriptive Statistics for NUTS 2 Region Data')

    with st.expander("Display NUTS 2 Region Tabular Dataset"):
        #df.set_index('region_name', inplace = True)
        st.dataframe(df.style.format(precision = 2))

        st.download_button("Download Dataset (CSV)",
        df.to_csv(index = False, float_format = "%.2f").encode('utf-8'),
        "nuts2_dataset.csv", "text/csv", key='download-csv') 

    with st.expander("Basic Summary Statistics for NUTS 2 Region Data"):
        df_desc = describe(df, percentiles = [25, 75])
        st.dataframe(df_desc.style.format(precision = 2))

    with st.expander("Distribution Plot for NUTS 2 Region Data", expanded = True):

        desc_cont= st.container()
        col1, col2 = st.columns(2)
        variable = col1.selectbox('Select Variable: ', options = num_cols, index = 1)
        plot_type = col2.selectbox('Select Plot: ', options = ['KDE Plot', 'Box Plot'])

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

with tab2:

    st.markdown('##### Regression Modeling for NUTS 2 Region Data')

    lin_reg_cont = st.container()

    col3, col4 = st.columns(2)
    col5, col6 = st.columns(2)
    iv = col3.selectbox('Select X (Independent Variable): ', options = num_cols, index = 1 )
    dv = col4.selectbox('Select Y (Dependent Variable): ', options = num_cols, index = 3)
    model_dict = {'Linear Regression': 'ols', 'LOWESS': 'lowess'}
    model = col5.radio('Select Model: ', options = model_dict.keys(), horizontal = True)

    if model == 'Linear Regression':
        show_res = col6.checkbox("Display Model Summary", value = False)

    with lin_reg_cont:
        fig2 = lin_reg_plot(df, iv, dv, model_dict[model])
        st.plotly_chart(fig2, use_container_width = True)

        if 'show_res' in globals() and show_res == True:
            summary = px.get_trendline_results(fig2).px_fit_results.iloc[0].summary()
            st.write(summary)

with tab3:

    st.markdown('##### Principal Component Analysis (PCA) Plot for NUTS 2 Region Data')

    fig3 = pca_plot(df_pca)
    st.plotly_chart(fig3, use_container_width = True)

st.markdown(terms)
st.markdown(footer, unsafe_allow_html= True)
