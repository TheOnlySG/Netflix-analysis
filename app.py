import pandas as pd
import streamlit as st


df = pd.read_csv('/home/spandan/Desktop/project/Netflix-analysis/data/netflix_titles.csv')


df["date_added"] = pd.to_datetime(df["date_added"].str.strip(), errors='coerce')
df["year_added"] = df["date_added"].dt.year
df["country"] = df["country"].fillna("Unknown")



st.title("🎬 Netflix Data Dashboard")


type_filter = st.sidebar.selectbox("Select Type", df["type"].unique())
year_filter = st.sidebar.slider(
    "Select Year",
    int(df["year_added"].min()),
    int(df["year_added"].max()),
    int(df["year_added"].max())
)

filtered_df = df[
    (df["type"] == type_filter) &
    (df["year_added"] <= year_filter)
]

st.write("Filtered Data", filtered_df.head())


st.subheader("Content Distribution")
st.bar_chart(filtered_df["country"].value_counts().head(10))


st.subheader("Content Over Years")
st.line_chart(df["year_added"].value_counts().sort_index())
