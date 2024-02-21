import streamlit as st
import datetime
today = datetime.datetime.now()
last_30year = today.year - 30
jan_1_last30years = datetime.datetime(last_30year, 1, 1);
with st.form('feedback_form'):
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input('Enter your name:')
        rating = st.slider('Rate this app:', 0, 10, 5)
    with col2:
        dob = st.date_input('Enter your date of birth:' ,min_value=jan_1_last30years)
        buy = st.radio('Will you buy this app?', ('Yes', 'No'))
    submitted = st.form_submit_button('Submit')

if submitted:
           st.write('**Name:**', name, '**DOB**', dob, \
           '**Rating**',rating, '**Buy**', buy)