import os, sys
sys.path.insert(1, os.path.abspath('..'))
from eustats import *
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib as mpl
import plotly.express as px
import pingouin as pg

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

df = pd.read_csv('data/eu_regional_data.csv', index_col = 'region_name')
df_pca = pd.read_csv('data/eu_regional_data_pca.csv', index_col = 'region_name')

num_cols = list(df.columns[2:])


with st.expander("Linear Regression Model Plot", expanded = True):

    lin_reg_cont = st.container()
    st.write('*You can hover/click on the regression line to view the coefficients \
              and R-Squared metric.*')

    col1, col2 = st.columns(2)
    iv = col1.selectbox('Select X (Independent Variable): ', options = num_cols, index = 1 )
    dv = col2.selectbox('Select Y (Dependent Variable): ', options = num_cols, index = 3)
    show_res = st.checkbox("Display Model Summary", value = False)

    with lin_reg_cont:
        fig1 = lin_reg_plot(df, x = iv, y = dv)
        summary = px.get_trendline_results(fig1).px_fit_results.iloc[0].summary()
        st.plotly_chart(fig1, use_container_width = True)
        if show_res :st.write(summary)

with st.expander("Principal Component Analysis (PCA) Plot for NUTS 2 Regions", expanded = False):
        
    fig2 = pca_plot(df_pca)
    st.plotly_chart(fig2, use_container_width = True)

with st.expander("Statistical Hypothesis Testing"):

    hypothesis_cont= st.container()

    col3, col4 = st.columns(2)
    variable = col3.selectbox('Select Variable: ', options = num_cols, index = 1)
    options_test = ['Shapiro-Wilk Normality', 'Levene Homoscedasticity',
                    'ANOVA', 'Pairwise Tukey', 'Kruskal-Wallis' ]
    test = col4.selectbox('Select Hypothesis Test: ', options_test)

    with hypothesis_cont:

        fig3 = box_plot(df, variable)
        st.plotly_chart(fig3, use_container_width = True)

        if test == options_test[0]:
            st.dataframe( pg.normality(df, dv = variable, group = 'EU Region') )

        elif test == options_test[1]:
            st.dataframe( pg.homoscedasticity(df, dv = variable, group = 'EU Region') )

        elif test == options_test[2]:
            st.dataframe( pg.anova(df, dv = variable, between = 'EU Region') )

        elif test == options_test[3]:
            st.dataframe( pg.pairwise_tukey(df, dv = variable, between = 'EU Region') )

        elif test == options_test[4]:
            st.dataframe( pg.kruskal(df, dv = variable, between = 'EU Region') )


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
