import streamlit as st
import sys
import os

# Add the root directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

#set layout to wide
st.set_page_config(layout="wide")


#add pages
about = st.Page("frontend/about.py", title="About")
table = st.Page("frontend/happiness_table.py", title="Report")
ranking = st.Page("frontend/ranking.py", title="Ranking")
plot_correlation = st.Page("frontend/plot_correlation.py", title="Plot Correlation")
trends = st.Page("frontend/trends.py", title="Trends")
contact_us = st.Page("frontend/contact_us.py", title="Contact US")
pg = st.navigation([table, about, ranking, plot_correlation, trends, contact_us])

pg.run()