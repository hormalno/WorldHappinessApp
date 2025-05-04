import streamlit as st

#set layout to wide
st.set_page_config(layout="wide")

#add pages
table = st.Page("frontend/happiness_table.py", title="World Happiness Report")
ranking = st.Page("frontend/happiness_ranking.py", title="Happiness Ranking")
charts = st.Page("frontend/charts.py", title="Charts")
contact_us = st.Page("frontend/contact_us.py", title="Contact US")
pg = st.navigation([table, ranking, charts, contact_us])

pg.run()