import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import stats

from backend import get_all_data

#heador of the page
st.header("WORLD HAPPINESS PLOT CORRELATION")
st.write("Displayed scatter charts:")

# Load the data
df = get_all_data()

#
fig1, ax1 = plt.subplots(figsize=(5, 3), layout='constrained')
sns.regplot(x=df["economy"], y=df["happiness_score"],  ax=ax1, scatter_kws={'alpha': 0.6}, line_kws={"color": "red"})
ax1.set_xlabel("x=economy")
ax1.set_ylabel("y=happiness score")
ax1.set_title(f'Economy(GDP) x Happiness Score')
#
fig2, ax2 = plt.subplots(figsize=(5, 3), layout='constrained')
sns.regplot(x=df["family"], y=df["happiness_score"],  ax=ax2, scatter_kws={'alpha': 0.6}, line_kws={"color": "red"})
ax2.set_xlabel("x=social support")
ax2.set_ylabel("y=happiness score")
ax2.set_title(f'Social Support x Happiness Score')
#
fig3, ax3 = plt.subplots(figsize=(5, 3), layout='constrained')
sns.regplot(x=df["trust"], y=df["happiness_score"],  ax=ax3, scatter_kws={'alpha': 0.6}, line_kws={"color": "red"})
ax3.set_xlabel("x=trust in government")
ax3.set_ylabel("y=happiness score")
ax3.set_title(f'Trust x Happiness Score')
#
fig4, ax4 = plt.subplots(figsize=(5, 3), layout='constrained')
sns.regplot(x=df["health"], y=df["happiness_score"],  ax=ax4, scatter_kws={'alpha': 0.6}, line_kws={"color": "red"})
ax4.set_xlabel("x=health")
ax4.set_ylabel("y=happiness score")
ax4.set_title(f'Health x Happiness Score')
#
fig5, ax5 = plt.subplots(figsize=(5, 3), layout='constrained')
sns.regplot(x=df["freedom"], y=df["happiness_score"],  ax=ax5, scatter_kws={'alpha': 0.6}, line_kws={"color": "red"})
ax5.set_xlabel("x=freedom")
ax5.set_ylabel("y=happiness score")
ax5.set_title(f'Freedom x Happiness Score')
#
fig6, ax6 = plt.subplots(figsize=(5, 3), layout='constrained')
sns.regplot(x=df["generosity"], y=df["happiness_score"],  ax=ax6, scatter_kws={'alpha': 0.6}, line_kws={"color": "red"})
ax6.set_xlabel("x=generosity")
ax6.set_ylabel("y=happiness score")
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

st.subheader("INSIGHT")
scores = {
    "economy": {
        "label": "Economy (GDP)"
    },
    "family": {
        "label": "Social Support"
    },
    "trust": {
        "label": "Trust in government"
    },
    "health": {
        "label": "Health (Life expectancy)"
    },
    "generosity": {
        "label": "Generosity"
    },
    "freedom" : {
        "label": "Freedom"
    }
}

for score in scores.keys():
    value = stats.pearsonr(df['happiness_score'], df[score]).statistic
    scores[score]["value"] = value
sorted_scores = dict(sorted(scores.items(), key=lambda x: -x[1]['value']))

st.write("Here's a quick ranking of influence based on the correlations, using the Pearson correlation coefficient:")
for i, score in enumerate(sorted_scores.keys()):
    st.write(f"{i+1}. {scores[score]['label']}: {scores[score]['value']:.3f}")
st.write("The most influential factor, indicating a strong positive linear relationship between a country's economic performance (as measured by GDP) and its happiness score. In other words, countries with higher GDP per capita tend to report higher happiness levels.")



