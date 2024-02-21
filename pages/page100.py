import streamlit as st
import pandas as pd
import random

def random_data(n):
    y = [random.randint(-1, 1) for value in range(n)]
    return y

if __name__ == '__main__':
    if 'df1' not in st.session_state:
        st.session_state.df1 = pd.DataFrame(data={'y':[1,0]})
    
    col1, col2 = st.columns([1,3])
    with col1:
        table = st.table(st.session_state.df1)

    with col2:
        chart = st.line_chart(st.session_state.df1)
        n = st.number_input('Number of rows to add',0,10,1)
        if st.button('Update'):
            y = random_data(n)
            df2 = pd.DataFrame(data={'y':y})
            st.session_state.df1 = pd.concat([st.session_state.df1, df2], ignore_index = True)
            st.session_state.df1.reset_index() 