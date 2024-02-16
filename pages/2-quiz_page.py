import streamlit as st
import spacy
import random
import pandas as pd
from spacy.tokens import Token
from utils.func import generate_quiz
from streamlit_extras.switch_page_button import switch_page
from fpdf import FPDF
import base64

new_q = st.button("สร้างแบบทดสอบใหม่")
if new_q:
    switch_page("streamlit_app")

q_answer = st.button("เฉลย")
if q_answer:
    switch_page("quiz_answer_page")

with st.container(border=True):
    tab1, tab2, = st.tabs(["แบบทดสอบ", "เฉลย"])

    with tab1:
        st.title("แบบทดสอบ")
        st.markdown("""
            ---
            """)
        quiz_list = st.session_state.Quiz
        for i, q in enumerate(quiz_list, 1):
            question = q["question"]
            choices = q["choices"]
            
            # Write the question number and the question text
            st.markdown(f" {i}.{question}")

            # Iterate over the choices
            for j, c in enumerate(choices):
                # Convert the index j to an alphabetic character
                choice_order = chr(ord('A') + j)
                # Write the choice number and the choice text
                st.markdown(f"{choice_order}. {c}")
            
            # Add an empty line between questions
            st.write()
    with tab2:
        st.title("เฉลย")
        st.markdown("""
            ---
            """)

        quiz_list = st.session_state.Quiz
        for i, q in enumerate(quiz_list, 1):
            question = q["question"]
            choices = q["choices"]
            correct_answer = q["correct_answer"]
            
            for j, c in enumerate(choices):
                choice_order = chr(ord('A') + j)
                if c == correct_answer:
                    correct_anwser = f"**{choice_order}. {c}**"
            st.markdown(f" {i}. {question}    {correct_anwser}")
            st.write()