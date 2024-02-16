import streamlit as st
import spacy
import random
import pandas as pd
from spacy.tokens import Token
from utils.func import generate_quiz
from streamlit_extras.switch_page_button import switch_page
from fpdf import FPDF

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
for i, q in enumerate(quiz_list):
    question = q["question"]
    choices = q["choices"]
    
    # Write the question number and the question text
    st.markdown(f" {i + 1} .{question}")

    # Iterate over the choices
    for j, c in enumerate(choices):
        # Convert the index j to an alphabetic character
        choice_order = chr(ord('A') + j)
        # Write the choice number and the choice text
        st.markdown(f"{choice_order}. {c}")
    
    # Add an empty line between questions
    st.write()


def generate_pdf():

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="English Quiz!", ln=1, align="C")
    pdf.output("Quiz.pdf")


if st.button("Generate PDF"):
    generate_pdf()

with open("example.pdf", "rb") as f:
    st.download_button("Downloada pdf", f, "example.pdf")

# Create PDF
pdf = FPDF()
pdf.add_page()

# Set font for the quiz
pdf.set_font("Arial", size=12)

# Add quiz title
pdf.cell(200, 10, txt="แบบทดสอบ", ln=True, align="C")
pdf.cell(200, 10, ln=True)

# Add quiz questions and choices
for i, question_data in enumerate(quiz_list, 1):
    question = question_data["question"]
    choices = question_data["choices"]
    
    # Add question number and text
    pdf.cell(200, 10, txt=f"{i}. {question}", ln=True)
    
    # Add choices
    for j, choice in enumerate(choices):
        choice_letter = chr(ord('A') + j)
        pdf.cell(10, 10, txt=f"{choice_letter}.", ln=False)
        pdf.multi_cell(190, 10, txt=choice)
    
    # Add space between questions
    pdf.cell(200, 10, ln=True)

# Save PDF to file
pdf.output("quiz.pdf")
with open("example.pdf", "rb") as f:
    st.download_button("Download pdf", f, "quiz.pdf")