import streamlit as st
import random

with st.form('feedback_form'):
    col1 = st.columns(1)
    with col1:
        name = st.text_input('Enter your name:')
        submitted = st.form_submit_button('Submit')
if submitted:
           st.write('**Name:**', name), \
          
           
def generate_password(character,password_length=6):
    random.shuffle(character)
    password = []
    for i in range(password_length):
        password.append(random.choice(character))
    return("".join(password)) 

#const
lower = "abcdefghijklmnopqrstuvwxyz" 
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" 
number = "012346789" 

total = lower + upper + number + name

def main():
    st.title("Generator Password App")
    
    menu = ["HOME"]
    Choice = st.sidebar.selectbox("Menu",menu)
    if menu == "HOME":
        st.subheader("HOME")
        if st.button("Generate"):
            password_result = generate_password(total)
            
            
            st.write(total)
            st.code(password_result)