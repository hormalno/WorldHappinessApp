import streamlit as st

from src.backend import sort_all_data_by_rank_asc, sort_all_data_by_rank_desc
from src.frontend.col_config import layout_table

#heador of the page
st.header("WORLD HAPPINESS RANKING")

#update values when changing between sliders
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
        0, 100, 0,
        step=5,
        key="top_n",
        on_change=update_top_n
    )

    bottom_n_option = st.slider(
        "Display bottom N countries:",
        0, 100, 0,
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
    st.write(f"Displayed top {top_n_option} happiest countries:")
    df = sort_all_data_by_rank_asc()
    st.dataframe(df.head(top_n_option), column_config=layout_table(), use_container_width=True, hide_index=True)
elif bottom_n_option > 0:
    st.write(f"Displayed bottom {bottom_n_option} happiest countries:")
    df = sort_all_data_by_rank_desc()
    st.dataframe(df.head(bottom_n_option), column_config=layout_table(), use_container_width=True, hide_index=True)