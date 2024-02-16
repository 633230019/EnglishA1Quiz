from genquiz import generate_quiz
import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import spacy
import random
import pandas as pd
from spacy.tokens import Token

st.header("สร้างแบบทดสอบเรียบร้อย")

quiz = st.button("เปิดแบบทดสอบ")
if quiz:
    switch_page("2-quiz_page")
    
quiz = st.button("เปิดเฉลย")
if quiz:
    switch_page("3-quiz_answer_page")