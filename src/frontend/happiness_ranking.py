import streamlit as st

from backend import sort_all_data_by_rank_asc, sort_all_data_by_rank_desc
from frontend.col_config import layout_table

#heador of the page
st.header("HAPPINESS RANKING")

# Initialize session state for both sliders
if "top_n" not in st.session_state:
    st.session_state.top_n = 0
if "bottom_n" not in st.session_state:
    st.session_state.bottom_n = 0

def update_top_n():
    if st.session_state.top_n > 0:
        st.session_state.bottom_n = 0

def update_bottom_n():
    if st.session_state.bottom_n > 0:
        st.session_state.top_n = 0

with st.sidebar:
    # Sliders with range 0-100 and step 10
    top_n_option = st.slider(
        "Display top N happiest countries:",
        0, 100, st.session_state.top_n,
        step=5,
        key="top_n",
        on_change=update_top_n
    )

    bottom_n_option = st.slider(
        "Display bottom N countries:",
        0, 100, st.session_state.bottom_n,
        step=5,
        key="bottom_n",
        on_change=update_bottom_n
    )

#####################################
#add tables with tabs per year
if top_n_option == 0 and bottom_n_option == 0:
    st.write(f"Displayed all data:")
    st.dataframe(sort_all_data_by_rank_asc(), column_config=layout_table(), use_container_width=True, hide_index=True)
elif top_n_option > 0:
    df = sort_all_data_by_rank_asc()
    st.write(f"Displayed top {top_n_option} happiest countries:")
    st.dataframe(df.head(top_n_option), column_config=layout_table(), use_container_width=True, hide_index=True)
elif bottom_n_option > 0:
    st.write(f"Displayed bottom {bottom_n_option} happiest countries:")
    df = sort_all_data_by_rank_desc()
    st.dataframe(df.head(bottom_n_option), column_config=layout_table(), use_container_width=True, hide_index=True)