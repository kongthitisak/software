import streamlit as st
import pandas as pd
import numpy as np

np.random.seed(2)

df = pd.DataFrame(
    np.random.randn(4, 3),
    columns=('Column 1','Column 2','Column 3')
)

st.subheader('Original dataframe')
st.write(df)

st.subheader('Filtering')
df = df[df['Column 1'] > 0]
st.write(df)

st.subheader('Selection')
df = df[['Column 1', 'Column 2']]
st.write(df)

st.subheader('Sorting')
df = df.sort_values(by='Column 1',ascending=True)
st.write(df)

st.subheader('Mapping')
df = df.assign(Column_4 = lambda x: df['Column 1']*2)
st.write(df)