import streamlit as st

def display_name(name):
    st.info(f'**Name:** {name}')
    
name = st.text_input('Please enter your name')
if not name:
    st.error('No name entered')
if name and len(name)<5:
    st.error('no name')
if name and len(name)>5:
    display_name(name)

