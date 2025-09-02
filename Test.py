import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📊 Finance Data Visualization")

# Load data
DATA_URL = "https://raw.githubusercontent.com/norashikinyusof277/ISD0Part2/main/Finance_data.csv"
df = pd.read_csv(DATA_URL)

# Plot histogram of ages
st.subheader("Distribution of Ages")
fig, ax = plt.subplots(figsize=(10, 6))
ax.hist(df['age'], bins=10, edgecolor='black')
ax.set_title('Distribution of Ages')
ax.set_xlabel('Age')
ax.set_ylabel('Frequency')
ax.grid(axis='y', alpha=0.75)

# Display in Streamlit
st.pyplot(fig)
