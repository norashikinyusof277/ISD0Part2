import streamlit as st

# Title
st.title("Hello Streamlit 👋")

# Input
name = st.text_input("Enter your name:")

# Button
if st.button("Say Hello"):
    st.write(f"Hello, {name}!")
