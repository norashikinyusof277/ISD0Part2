import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("📊 Finance Data Visualization")

# Load data
DATA_URL = "https://raw.githubusercontent.com/norashikinyusof277/ISD0Part2/main/Finance_data.csv"
df = pd.read_csv(DATA_URL)

# Scatterplot with seaborn
st.subheader("Relationship between Age, Fixed Deposits, and Gender")

fig, ax = plt.subplots(figsize=(10, 6))
sns.scatterplot(data=df, x='age', y='Fixed_Deposits', hue='gender', ax=ax)

ax.set_title('Relationship between Age, Fixed Deposits, and Gender')
ax.set_xlabel('Age')
ax.set_ylabel('Fixed Deposits')
ax.grid(True)

# Show in Streamlit
st.pyplot(fig)
