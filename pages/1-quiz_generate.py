import streamlit as st
import spacy
import random
import pandas as pd
from spacy.tokens import Token
from utils.func import generate_quiz
from streamlit_extras.switch_page_button import switch_page

quiz = st.button("สร้างแบบทดสอบใหม่")
if quiz:
    switch_page("streamlit_app")

st.header("สร้างแบบทดสอบเรียบร้อย")

quiz = st.button("เปิดแบบทดสอบ")
if quiz:
    switch_page("quiz_page")
    
quiz = st.button("เปิดเฉลย")
if quiz:
    switch_page("quiz_answer_page")
