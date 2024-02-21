import streamlit as st

# stateless counter
st.title('Counter Example')
count = 0

increment = st.button('Increment',key='b1')
if increment:
    count += 1

st.write('Count = ', count)

# with stateful counter
if 'count' not in st.session_state:
    st.session_state.count = 0

increment2 = st.button('Increment',key='b2')
if increment2:
    st.session_state.count += 1

st.write('Count = ', st.session_state.count)