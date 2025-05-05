import streamlit as st

#set layout to wide
st.set_page_config(layout="wide")

#add pages
table = st.Page("frontend/happiness_table.py", title="Report")
ranking = st.Page("frontend/ranking.py", title="Ranking")
plot_correlation = st.Page("frontend/plot_correlation.py", title="Plot Correlation")
trends = st.Page("frontend/trends.py", title="Trends")
contact_us = st.Page("frontend/contact_us.py", title="Contact US")
pg = st.navigation([table, ranking, plot_correlation, trends, contact_us])

pg.run()