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

with st.container():
    st.title("แบบทดสอบ")
    st.markdown("""
        ---
        """)

quiz_list = st.session_state.Quiz
for i, q in enumerate(quiz_list, 1):
    question = q["question"]
    choices = q["choices"]
    
    # Write the question number and the question text
    st.markdown(f" {i} .{question}")

    # Iterate over the choices
    for j, c in enumerate(choices):
        # Convert the index j to an alphabetic character
        choice_order = chr(ord('A') + j)
        # Write the choice number and the choice text
        st.markdown(f"{choice_order}. {c}")
    
    # Add an empty line between questions
    st.write()


def generate_pdf_content():
    # Generate PDF content
    pdf_content = "แบบทดสอบ\n\n"
    for i, question_data in enumerate(quiz_list, 1):
        question = question_data["question"]
        choices = question_data["choices"]
        
        # Add question number and text
        pdf_content += f"{i}. {question}\n"
        
        # Add choices
        for j, choice in enumerate(choices):
            choice_letter = chr(ord('A') + j)
            pdf_content += f"{choice_letter}. {choice}\n"
        
        # Add space between questions
        pdf_content += "\n"
    
    return pdf_content

# Generate PDF content
pdf_content = generate_pdf_content()

# Encode PDF content to Base64
pdf_base64 = base64.b64encode(pdf_content.encode('utf-8')).decode('utf-8')

# Display PDF in Streamlit app
st.markdown(f'<embed src="data:application/pdf;base64,{pdf_base64}" width="700" height="1000"></embed>', unsafe_allow_html=True)
if st.button("pdf"):
    generate_pdf_content()