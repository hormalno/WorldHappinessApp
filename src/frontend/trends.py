import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

from backend import get_all_years

#heador of the page
st.header("WORLD HAPPINESS TREND")

#get the dataset
df = get_all_years()

#sidebar: choose countries
countries = df["country"].unique()
selected_countries = st.multiselect("Select countries:", countries,
                                    default=["Norway", "Denmark", "Finland", "Bulgaria", "Romania"])

#filter data
filtered_df = df[df["country"].isin(selected_countries)]

#pivot for bar plotting
pivot_df = filtered_df.pivot(index="year", columns="country", values="happiness_score")

#bar chart setup
fig, ax = plt.subplots(figsize=(30, 10))
bar_width = 0.05
years = pivot_df.index
x = np.arange(len(years))

for i, country in enumerate(pivot_df.columns):
    scores = pivot_df[country]
    ax.bar(x + i * bar_width, scores, width=bar_width, label=country, edgecolor="black")

#customizing gridlines
ax.set_xticks(x + bar_width * (len(pivot_df.columns) - 1) / 2)
ax.set_xticklabels(years)
ax.set_xlabel("Year",fontsize=14)
ax.set_ylabel("Happiness Score", fontsize=14)
ax.set_title("Happiness Scores per Year", fontsize=20)
ax.legend(fontsize=20)

#customize gridlines: light vertical gridlines for better visual separation
ax.grid(axis="y", linestyle="--", alpha=0.5, color='gray')
ax.grid(axis="x", linestyle=":", alpha=0.3, color='blue')

#show plot
st.pyplot(fig)