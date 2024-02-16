from genquiz import generate_quiz
import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import spacy
import random
import pandas as pd
from spacy.tokens import Token

with st.container():
    st.title("แบบทดสอบ")
    st.markdown("""
        ---
        """)

quiz_list = st.session_state.Quiz
for i, q in enumerate(quiz_list):
    question = q["question"]
    choices = q["choices"]
    
    # Write the question number and the question text
    st.write(f"Question {i + 1}: {question}")

    # Iterate over the choices
    for j, c in enumerate(choices):
        # Convert the index j to an alphabetic character
        choice_order = chr(ord('A') + j)
        # Write the choice number and the choice text
        st.write(f"{choice_order}. {c}")
    
    # Add an empty line between questions
    st.write()

