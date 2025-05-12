desc_indicators = """ 
This dashboard provides statistical indicators and analysis for European Union countries, 
based on data from official sources. You can easily view the graph of your preference
by selecting a country and indicator below. Furthermore, you can visit the
<a href ="/Analysis" target = "_self">Analysis</a> page for advanced statistics,
including linear regression modeling and dimensionality reduction (PCA, t-SNE and UMAP).
The dashboard was developed by [Giannis Tolios](https://giannis.io),
using Python and various open source libraries, with the code being freely available
at [Github](https://github.com/derevirn/eu-stats).
If you have any feedback and suggestions, feel free to [send an email](mailto:info@statseuropa.com).  

-----
"""

desc_analysis = """ 
This page provides statistical analysis for administrative regions of
EU countries ([NUTS 2](https://en.wikipedia.org/wiki/Nomenclature_of_Territorial_Units_for_Statistics) level).
The **Descriptive Statistics** tab contains the dataset (based on year 2022), as well as summary statistics and visualizations. 
Furthermore, the **Regression Modeling** tab lets you create a linear regression or LOWESS model,
by choosing two variables of your preference.
Finally, the **Dimensionality Reduction** tab provides visualizations of various dimensionality
reduction methods applied on the dataset (PCA, t-SNE and UMAP), with the bubble size representing GDP per capita.
You can click <a href ="/Indicators" target = "_self">Here</a> to go back to the Indicators page.

-----
"""

terms = ''' &nbsp; 

-------------------
##### Privacy & Terms

**Privacy**

No user data are collected, apart from basic analytics like number of visitors and pageviews,
provided by the StatCounter service. You can [click here](https://statcounter.com/about/legal/)
to read their privacy policy.  

**Terms of Use**

You are free to use any plots or datasets that are available on this website, 
under the term of giving appropriate credit and referencing [StatsEuropa.com](https://statseuropa.com).

--------------------
'''

footer = """
<style>
footer {visibility: hidden;}    

.footer_ {
  position: relative;
  bottom: 0;
  right: 0;
  width: 100%;
  font-family: "Source Sans Pro", sans-serif;
  font-size: 0.9rem;
  color: rgb(49, 51, 63);
  text-align: right;
}
</style>

<div class="footer_">
  <p>Giannis Tolios 2022</p>
</div>
"""

tracking = '''<!-- Default Statcounter code for StatsEuropa https://eu-stats.herokuapp.com/ -->

<script type="text/javascript">
var sc_project=12751725; 
var sc_invisible=1; 
var sc_security="35d8e5a4"; 
</script>

<script type="text/javascript" src="https://www.statcounter.com/counter/counter.js" async></script>

<noscript>
<div class="statcounter"><a title="Web Analytics" href="https://statcounter.com/" target="_blank">
<img class="statcounter" src="https://c.statcounter.com/12751725/0/35d8e5a4/1/" alt="Web Analytics" referrerPolicy="no-referrer-when-downgrade"></a>
</div>
</noscript>

<!-- End of Statcounter Code -->'''