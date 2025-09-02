import streamlit as st
import pandas as pd
import numpy as np

st.title("📊 Simple Streamlit Chart")

# Create random data
data = pd.DataFrame(np.random.randn(20, 3), columns=["A", "B", "C"])

# Display chart
st.line_chart(data)
