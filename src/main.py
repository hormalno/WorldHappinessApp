import streamlit as st

from backend import get_all_data

data = get_all_data()
st.write('2015')
st.write(data[0])
st.write('2016')
st.write(data[1])
st.write('2017')
st.write(data[2])
st.write('2018')
st.write(data[3])
st.write('2019')
st.write(data[4])

# chart_data = pd.DataFrame(
#     np.random.randn(20, 3),
#     columns=["a", "b", "c"]
# )
#
# st.button("asd")
# st.write("Hello World!")
# st.write(df)
# st.bar_chart(chart_data)