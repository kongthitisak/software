import streamlit as st
import time

on = st.toggle('Activate counter', True)
counter = st.empty()
if 'count' not in st.session_state:    
    st.session_state.count = 0
reset = st.button('reset')
if reset:
        st.session_state.count = 0
        
counter.header(st.session_state.count)      

counter.header(st.session_state.count)

while on:
    counter.header(st.session_state.count)
    time.sleep(0.1)
    st.session_state.count +=1
    