import streamlit as st

def layout_table():
    return {
        "country": st.column_config.TextColumn(
            label="Country",
            help="Country of origin"
        ),
        "region": st.column_config.TextColumn(
            label="Region",
            help="Region"
        ),
        "happiness_rank": st.column_config.NumberColumn(
            label="Happiness Rank",
            help="The rank based on the score compared to the other countries"
        ),
        "happiness_score": st.column_config.NumberColumn(
            label="Happiness Score",
            help="Final happiness score as a total from the other score columns"
        ),
        "economy": st.column_config.NumberColumn(
            label="Economy (GDP)",
            help="This measures the economic output per person, adjusted for purchasing power. It reflects the material wealth and standard of living, which contributes to people's ability to meet basic needs and enjoy life."
        ),
        "family": st.column_config.NumberColumn(
            label="Social Support",
            help="Represents whether people feel they have someone to rely on in times of need, based on responses to the question about having friends or relatives to count on."
        ),
        "health": st.column_config.NumberColumn(
            label="Health",
            help="This reflects not just how long people live, but how many of those years are lived in good health. A longer and healthier life generally correlates with higher life satisfaction."
        ),
        "freedom": st.column_config.NumberColumn(
            label="Freedom",
            help="This measures the extent to which people feel free to make decisions about their own lives. It’s based on responses to the question, “Are you satisfied or dissatisfied with your freedom to choose what you do with your life?”"
        ),
        "trust": st.column_config.NumberColumn(
            label="Trust",
            help="This captures the public’s trust in government and business, and whether they perceive these institutions to be corrupt. Lower perceived corruption is associated with higher trust and happiness."
        ),
        "generosity": st.column_config.NumberColumn(
            label="Generosity",
            help="This is based on donations and helping behavior, measured through responses to questions like “Have you donated money to a charity in the past month?” It reflects a sense of community and altruism, which are linked to well-being."
        ),
        "dyst_res": st.column_config.NumberColumn(
            label="Dystopian Residual",
            help="Each country is also compared against a hypothetical nation called Dystopia. Dystopia represents the lowest national averages for each key variable and is, along with residual error, used as a regression benchmark. The six metrics are used to explain the estimated extent to which each of these factors contribute to increasing life satisfaction when compared to the hypothetical nation of Dystopia, but they themselves do not have an effect on the total score reported for each country."
        )
    }