import streamlit as st
import random
import string
import pyperclip

st.title("PASSWORD-#-GENERATOR")
st.subheader("Generate a strong password")

st.text("Please move the slider for your password safety")
length = st.select_slider("Password length", ["weak", "Good", "Strong", "Ultimate"])
if length == "weak":
    st.text("Password length is weak")
    length = 8
elif length == "Good":
    st.text("Password length is good")
    length = 12
elif length == "Strong":
    length = 16
    st.text("Password length is Strong")
elif length == "Ultimate":
    length = 20
    st.text("Password length is Ultimate")


st.text("Tick below checkbox to add these characters to your password")
col1, col2, col3, col4 = st.columns(4)
with col1:
    capital = st.checkbox("ABC")
with col2:
    small = st.checkbox("abc")
with col3:
    numbers = st.checkbox("123")
with col4:
    if length == 20:
        special = st.checkbox("!@#", value=True, disabled=True)
    elif length == 8:
        special = st.checkbox("!@#", value=False, disabled=True)
    else:
        special = st.checkbox("!@#")

def generate_password(length):
    # Initialize an empty string to collect the chosen character types
    characters = ''
    
    # Add character types based on user selection
    if capital:
        characters += string.ascii_uppercase
    if small:
        characters += string.ascii_lowercase
    if numbers:
        characters += string.digits
    if special:
        characters += string.punctuation
    if not characters:
        return "Please select at least one character type."
    
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if st.button("Generate Password"):
    password = generate_password(length)
    st.write("Generated password:")
    Path = f'''{password}'''
    st.code(Path, language="")
    st.text("Now You Can Copy Password Easily")