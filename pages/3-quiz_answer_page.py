import streamlit as st
import spacy
import random
import pandas as pd
from spacy.tokens import Token
from utils.func import generate_quiz
from streamlit_extras.switch_page_button import switch_page

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
    
    # Write the question number and the question text
    st.write(f"Question {i + 1}: {question}")

    # Iterate over the choices
    for j, c in enumerate(choices):
        choice_order = chr(ord('A') + j)
        if c == correct_answer:
            st.write(f"**{choice_order}. {c}**")
        st.write(f"{choice_order}. {c}")
    # Add an empty line between questions
    st.write()