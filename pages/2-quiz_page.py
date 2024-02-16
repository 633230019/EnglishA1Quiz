import streamlit as st
import spacy
import random
import pandas as pd
from spacy.tokens import Token
from utils.func import generate_quiz
from streamlit_extras.switch_page_button import switch_page
from fpdf import FPDF
import base64

Num_quiz = len(st.session_state.Quiz)
Num_choice = len(st.session_state.Quiz[0]["choices"])
q_type = 'ประเภท: ความรู้คำศัพท์ทั่วไป'

with st.container(border=True):
    tab1, tab2, = st.tabs(["แบบทดสอบ", "เฉลย"])
    with tab1:
        st.subheader("แบบทดสอบภาษาอังกฤษระดับชั้นประถมศึกษาปีที่ 6")
        col1, col2 = st.columns([0.8, 0.2])
        with col1:
            st.markdown(f"**{q_type}**")
        with col2:
            st.markdown(f"**จำนวน {Num_quiz} ข้อ**")
        st.write('***')   
        st.markdown("**คำชี้แจง**: เลือกคำตอบที่ถูกต้องที่สุดเพียงคำตอบเดียวลงในกระดาษคำตอบ")
        quiz_list = st.session_state.Quiz
        for i, q in enumerate(quiz_list, 1):
            question = q["question"]
            choices = q["choices"]
            
            # Write the question number and the question text
            st.markdown(f"{i}.&nbsp;{question}")

            # Iterate over the choices
            for j, c in enumerate(choices):
                # Convert the index j to an alphabetic character
                choice_order = chr(ord('A') + j)
                # Write the choice number and the choice text
                st.markdown(f"&nbsp;&nbsp;&nbsp;&nbsp;{choice_order}.&nbsp;{c}")
            
            # Add an empty line between questions
            st.write()
    with tab2:
        st.subheader("เฉลย")
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
            st.markdown(f"{i}.&nbsp;{question}&nbsp;&nbsp;&nbsp;&nbsp;{correct_anwser}")
            st.write()

new_q = st.button("สร้างแบบทดสอบใหม่")
if new_q:
    switch_page("streamlit_app")