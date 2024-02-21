import streamlit as st
import time

on = st.toggle('Activate counter', True)

counter = st.empty()
count = 0
while on:
    counter.header(count)
    time.sleep(0.1)
    count +=1