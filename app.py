import streamlit as st
from transformers import pipeline

nlp=pipeline('sentiment-analysis')

st.title('Sentiment-Analysizer')

input=st.text_input('Write your comment')

clicked=st.button('Predict')


if clicked:
    output=nlp(input)
    st.write(output[0]['label'])
    st.write('Your Score is :',output[0]['score'])
