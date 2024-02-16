import streamlit as st
import spacy
import random
import pandas as pd
from spacy.tokens import Token
from utils.func import generate_quiz
from streamlit_extras.switch_page_button import switch_page

st.header("สร้างแบบทดสอบเรียบร้อย")

quiz = st.button("เปิดแบบทดสอบ")
if quiz:
    switch_page("2-quiz_page")
    
quiz = st.button("เปิดเฉลย")
if quiz:
    switch_page("3-quiz_answer_page")

st.markdown('<a href="/2-quiz_page" target="_self">2-quiz_page</a>', unsafe_allow_html=True)
st.markdown('<a href="/3-quiz_answer_page" target="_self">3-quiz_answer_page</a>', unsafe_allow_html=True)