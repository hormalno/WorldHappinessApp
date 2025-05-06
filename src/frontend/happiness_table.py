import streamlit as st
from src.backend import get_all_data, get_data_by_year, get_all_data_by_country, get_data_by_year_and_country, \
    get_all_data_by_region, get_data_by_year_and_region, get_all_region, get_all_country
from src.frontend.col_config import layout_table

#heador of the page
st.header("WORLD HAPPINESS REPORT")

# Initialize session state for the filters
if "filter_region" not in st.session_state:
    st.session_state.filter_region = "All"
if "filter_country" not in st.session_state:
    st.session_state.filter_country = "All"

# Function to clear filters
def clear_filters():
    st.session_state.filter_region = "All"
    st.session_state.filter_country = "All"

####################################
#add the sidebar filters
with st.sidebar:
    st.header("Filters:")

    #region filter
    selected_region = st.selectbox(
        "Select a region:",
        options=["All"] + get_all_region(),
        key="filter_region"
    )

    #country filter
    selected_country = st.selectbox(
        "Select a country:",
        options=["All"] + get_all_country(selected_region if not selected_region == "All" else None),
        key="filter_country"
    )

    #clear button
    st.button("Clear All Filters", on_click=clear_filters)


#####################################
#add tables with tabs per year
tab_labels = ["All", "2015", "2016", "2017", "2018", "2019"]
tabs = st.tabs(tab_labels)
for i, tab in enumerate(tabs):
    with tab:
        #no filtering
        if selected_country == "All" and selected_region == "All":
            if i == 0:
                st.write(f"Displayed all data:")
                tab.dataframe(get_all_data(),
                              column_config=layout_table(), use_container_width=True, hide_index=True)
            else:
                st.write(f"Displayed data for year {tab_labels[i]}:")
                tab.dataframe(get_data_by_year(tab_labels[i]),
                              column_config=layout_table(), use_container_width=True, hide_index=True)
        #with filtering
        else:
            if not selected_country == "All":
                st.write(f"Filtered by country {selected_country}:")
                if i == 0:
                    tab.dataframe(get_all_data_by_country(selected_country),
                                  column_config=layout_table(), use_container_width=True, hide_index=True)
                else:
                    tab.dataframe(get_data_by_year_and_country(tab_labels[i], selected_country),
                                  column_config=layout_table(), use_container_width=True, hide_index=True)
            else:
                st.write(f"Filtered by region {selected_region}:")
                if i == 0:
                    tab.dataframe(get_all_data_by_region(selected_region),
                                  column_config=layout_table(), use_container_width=True, hide_index=True)
                else:
                    tab.dataframe(get_data_by_year_and_region(tab_labels[i], selected_region),
                                  column_config=layout_table(), use_container_width=True, hide_index=True)
