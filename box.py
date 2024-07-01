import streamlit as st

st.header('st.selectbox')

option = st.selectbox(
    'What is your favorite color?',
    ('Blue', 'Red', 'Green', 'Black')
)

st.write('Your favorite color is ', option)

st.subheader('st.multiselect')
options = st.multiselect(
    'What are your favorite colors',
    ['Blue', 'Red', 'Green', 'Black'],
    ['Green', 'Red']    
)

# check box
st.subheader('Check box')

st.write ('What would you like to order?')
icecream = st.checkbox('Ice Cream')
coffee = st.checkbox('Coffee')
cola = st.checkbox('Cola')

if icecream:
    st.write("Great! Heer's some more 🍦")
if coffee:
    st.write("Okay, here's some coffee ☕")
if cola:
    st.write("Here you go 🥤")