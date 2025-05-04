import streamlit as st
from backend import *

#heador of the page
st.header("Happiness Ranking")

#add the sidebar filters
st.sidebar.header("Filters:")
selected_country = st.sidebar.selectbox(
    "Select a country:",
    options=["All"] + get_all_countries()
)
selected_region = st.sidebar.selectbox(
    "Select a region:",
    options=["All"]
)
print(get_all_regions())
st.sidebar.slider("Size", 1, 5, key="size")

#add tables with tabs per year
tab_labels = ["All", "2015", "2016", "2017", "2018", "2019"]
tabs = st.tabs(tab_labels)
for i, tab in enumerate(tabs):
    with tab:
        if selected_country == "All":
            if i == 0:
                st.write(f"This is all data:")
                tab.dataframe(get_all_data(), height=250, use_container_width=True)
            else:
                st.write(f"This is all data per year {tab_labels[i]}:")
                tab.dataframe(get_data_by_year(tab_labels[i]), height=250, use_container_width=True)
        else:
            st.write(f"Filtered by country {selected_country}:")
            if i == 0:
                tab.dataframe(get_all_data_by_country(selected_country), height=250, use_container_width=True)
            else:
                tab.dataframe(get_data_by_year_and_country(tab_labels[i], selected_country), height=250, use_container_width=True)


