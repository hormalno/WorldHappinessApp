import streamlit as st
from backend import get_all_data

all_data = get_all_data()

st.subheader("Happiness Ranking")
tab1, tab2 = st.tabs(["All", "2015"])
tab1.dataframe(all_data[0], height=250, use_container_width=True)
tab2.dataframe(all_data[1], height=250, use_container_width=True)