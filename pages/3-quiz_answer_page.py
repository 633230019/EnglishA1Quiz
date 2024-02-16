import streamlit as st
import spacy
import random
import pandas as pd
from spacy.tokens import Token
from utils.func import generate_quiz
from streamlit_extras.switch_page_button import switch_page

new_q = st.button("สร้างแบบทดสอบใหม่")
if new_q:
    switch_page("streamlit_app")

quiz = st.button("แบบทดสอบ")
if quiz:
    switch_page("quiz_page")

with st.container():
    st.title("เฉลย")
    st.markdown("""
        ---
        """)

quiz_list = st.session_state.Quiz
for i, q in enumerate(quiz_list):
    question = q["question"]
    choices = q["choices"]
    correct_answer = q["correct_answer"]
    
    for j, c in enumerate(choices):
        choice_order = chr(ord('A') + j)
        if c == correct_answer:
            correct_anwser = f"**{choice_order}. {c}**"
    st.write(f"{i + 1}. {question} คำตอบ: {correct_anwser}")
    st.write()