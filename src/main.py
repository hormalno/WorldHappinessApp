import streamlit as st

from backend import get_all_data

data = get_all_data()
st.write(data)

# chart_data = pd.DataFrame(
#     np.random.randn(20, 3),
#     columns=["a", "b", "c"]
# )
#
# st.button("asd")
# st.write("Hello World!")
# st.write(df)
# st.bar_chart(chart_data)