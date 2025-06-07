import streamlit as st

# Page Title
st.title("🚀 Welcome to My Beautiful Streamlit App!")

# Subheading
st.subheader("This is a simple interactive web app built with Python & Streamlit")

# User Input
name = st.text_input("👤 Enter your name:")
age = st.number_input("🎂 Enter your age:", min_value=1, max_value=100)
hobby = st.selectbox("🎯 What's your favorite hobby?", 
                     ["Reading", "Gaming", "Cooking", "Traveling", "Coding"])

# Displaying user input
if st.button("✨ Submit"):
    st.success(f"Hello, {name} 👋! You are {age} years old and love {hobby}.")

# Add a checkbox and image
if st.checkbox("Show an inspiring quote"):
    st.info("“The best way to predict the future is to invent it.” – Alan Kay")

# Footer
st.markdown("---")
st.caption("📌 Made with 💖 using Streamlit")
