import streamlit as st
import time

st.title('Clock')

# for i in range(15):
#     st.write(i)
#     time.sleep(i)

count = 0
clock = st.empty()

while True:
    clock.info(f'⏳ {count} seconds have passed')
    if count >= 10:
        clock.empty()
        st.warning("✔️ time's up!")
        break
    count += 1
    time.sleep(1)

with st.empty():
    for seconds in range(10):
        st.info(f"⏳ {seconds} seconds have passed")
        time.sleep(1)
    st.warning("✔️ time's up!")