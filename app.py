import streamlit as st

import pandas as pd

st.title ('Hello World!!🙂fsdfsdf')

df = pd.DataFrame ({'A': [1,44], 'B': [3,4]})
df2 = df*2
df2


x = st.number_input ('Enter stenosis')
y= st.number_input ('Enter normal diameter')

z = (((y-x)/y)*100)
st.write ('Stenosis is', z)

if st.checkbox ('Enter'):
    st.subheader (z)


if st.toggle ('check'):
    st.header (z)


num1 = st.number_input ('Enter number 1')
num2 = st.number_input ('Enter number 2')

st.header ('Select Operation')

operation = st.radio ('Select 1 option', ('Add', 'Subtraction', 'Multiplication', 'Division'))

ans = 0

def calculate ():
    if operation == 'Add':
        ans = num1+num2
    elif operation == 'Subtraction':
        ans = num1-num2
    elif operation == 'Multiplication':
        ans = num1*num2
    else:
        ans = num1/num2


    st.header (ans)

if st.button ('Calculate'):
    calculate ()
