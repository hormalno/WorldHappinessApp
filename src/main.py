import streamlit as st

#set layout to wide
st.set_page_config(layout="wide")

#add pages
table = st.Page("frontend/happiness_table.py", title="Tables")
charts = st.Page("frontend/charts.py", title="Charts")
contact_us = st.Page("frontend/contact_us.py", title="Contact US")
pg = st.navigation([table, charts, contact_us])

#add the sidebar
st.sidebar.selectbox("Group", ["A","B","C"], key="group")
st.sidebar.slider("Size", 1, 5, key="size")

pg.run()