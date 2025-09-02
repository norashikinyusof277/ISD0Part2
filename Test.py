import streamlit as st
import pandas as pd

st.title("Finance Data Viewer")

# Read data directly from the remote CSV URL
DATA_URL = ("https://raw.githubusercontent.com/"
            "norashikinyusof277/ISD0Part2/main/Finance_data.csv")

@st.cache_data
def load_data(url):
    return pd.read_csv(url)

df = load_data(DATA_URL)

st.subheader("Raw Data")
st.dataframe(df)

st.subheader("Summary Statistics (Numeric Columns)")
st.write(df.describe())

st.subheader("Investment Avenues Distribution")
if "Investment_Avenues" in df.columns:
    st.bar_chart(df["Investment_Avenues"].value_counts())
