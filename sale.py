import streamlit as st 

st.header('SIMPLE SALES PROGRAM')
item = st.text_input('Material Item')
price = st.number_input('Price',0)
qty = st.number_input('Quantity',0)
total = st.button('Click Total')

if total:
    pay = price * qty
    st.success(f'You have to pay {pay}')
    st.balloons()

