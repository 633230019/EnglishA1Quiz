import streamlit as st
import spacy
import random
import pandas as pd
from spacy.tokens import Token
from utils.func import generate_quiz
from streamlit_extras.switch_page_button import switch_page

for k, v in st.session_state.to_dict().items():
   st.session_state[k] = v

st.header("สร้างแบบทดสอบเรียบร้อย")

quiz = st.button("เปิดแบบทดสอบ")
if quiz:
    switch_page("quiz_page")
    
quiz = st.button("เปิดเฉลย")
if quiz:
    switch_page("quiz_answer_page")

st.markdown('<a href="/quiz_page" target="_self">quiz_page</a>', unsafe_allow_html=True)
st.markdown('<a href="/quiz_answer_page" target="_self">quiz_answer_page</a>', unsafe_allow_html=True)