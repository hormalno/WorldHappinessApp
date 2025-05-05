import streamlit as st
import matplotlib.pyplot as plt

from backend import get_all_data

#heador of the page
st.header("WORLD HAPPINESS PLOT CORRELATION")
st.write("Displayed scatter charts:")

# Load the data
df = get_all_data()

#
fig1, ax1 = plt.subplots(figsize=(5, 3), layout='constrained')
ax1.scatter(df["economy"], df["happiness_score"], alpha=0.7)
ax1.set_xlabel("economy")
ax1.set_ylabel("happiness score")
ax1.set_title(f'Economy(GDP) x Happiness Score')
#
fig2, ax2 = plt.subplots(figsize=(5, 3), layout='constrained')
ax2.scatter(df["family"], df["happiness_score"], alpha=0.7)
ax2.set_xlabel("social support")
ax2.set_ylabel("happiness score")
ax2.set_title(f'Social Support x Happiness Score')
#
fig3, ax3 = plt.subplots(figsize=(5, 3), layout='constrained')
ax3.scatter(df["trust"], df["happiness_score"], alpha=0.7)
ax3.set_xlabel("trust in government")
ax3.set_ylabel("happiness score")
ax3.set_title(f'Trust x Happiness Score')
#
fig4, ax4 = plt.subplots(figsize=(5, 3), layout='constrained')
ax4.scatter(df["health"], df["happiness_score"], alpha=0.7)
ax4.set_xlabel("health")
ax4.set_ylabel("happiness score")
ax4.set_title(f'Health x Happiness Score')
#
fig5, ax5 = plt.subplots(figsize=(5, 3), layout='constrained')
ax5.scatter(df["freedom"], df["happiness_score"], alpha=0.7)
ax5.set_xlabel("freedom")
ax5.set_ylabel("happiness score")
ax5.set_title(f'Freedom x Happiness Score')
#
fig6, ax6 = plt.subplots(figsize=(5, 3), layout='constrained')
ax6.scatter(df["generosity"], df["happiness_score"], alpha=0.7)
ax6.set_xlabel("generosity")
ax6.set_ylabel("happiness score")
ax6.set_title(f'Generosity x Happiness Score')

# --- Display in 3x2 layout ---
col1, col2, col3 = st.columns(3)

with col1:
    st.pyplot(fig1)
    st.pyplot(fig2)

with col2:
    st.pyplot(fig3)
    st.pyplot(fig4)

with col3:
    st.pyplot(fig5)
    st.pyplot(fig6)

