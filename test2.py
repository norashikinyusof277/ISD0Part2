import streamlit as st
import pandas as pd
import numpy as np

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to:", ["Home", "Data Viz", "Upload"])

# --- Home Page ---
if page == "Home":
    st.title("🚀 Better Streamlit App")
    st.write("This is a simple multi-page Streamlit app with sidebar navigation.")
    
    name = st.text_input("Enter your name:")
    age = st.slider("Select your age:", 1, 100, 25)
    
    if st.button("Greet me!"):
        st.success(f"Hello {name}, you are {age} years old 🎉")

# --- Data Visualization Page ---
elif page == "Data Viz":
    st.title("📊 Random Data Visualization")
    
    # Generate random data
    df = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['A', 'B', 'C']
    )
    
    st.line_chart(df)
    st.bar_chart(df)

# --- File Upload Page ---
elif page == "Upload":
    st.title("📂 Upload & Preview CSV")
    
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write("Preview of uploaded file:")
        st.dataframe(df.head())
