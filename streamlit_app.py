import streamlit as st
import spacy
import random
import pandas as pd
from spacy.tokens import Token
from utils.func import generate_quiz
from streamlit_extras.switch_page_button import switch_page
import streamlit_shadcn_ui as ui

df_Sent=pd.read_csv("./data/filtered_sentences_dataset_a1_20k.csv")
df_Word=pd.read_csv("./data/oxford_a1.csv")


st.header("สร้างแบบทดสอบภาษาอังกฤษระดับป.6")

    
Num_quiz = st.number_input('ระบุจำนวนข้อแบบทดสอบที่ต้องการสร้าง', 
                        min_value=1, max_value=100, value=20, key="Num_quiz")

Num_choice = st.number_input('ระบุจำนวนข้อแบบทดสอบที่ต้องการสร้าง', 
                        min_value=2, max_value=5, value=4, key="Num_choice")
    
q_type = st.selectbox(
    'ระบุประเภทแบบทดสอบ',
    ('ทดสอบความรู้คำศัพท์ทั่วไป','ทดสอบความรู้ไวยากรณ์'), key="q_type")

create_quiz = st.button("สร้างแบบทดสอบ")
if create_quiz:
    st.session_state.Quiz = generate_quiz(Num_quiz, Num_choice, df_Sent, df_Word)
    switch_page("quiz_generate")

with ui.card(key="card1"):
    ui.element("span", children=["Number of Quiz"], className="text-gray-400 text-sm font-medium m-1", key="label1")
    num_quiz = st.number_input('Enter the number of quiz questions', min_value=1, max_value=100, value=20, key="Num_quiz")

    ui.element("span", children=["Number of Choices"], className="text-gray-400 text-sm font-medium m-1", key="label2")
    num_choice = st.number_input('Enter the number of choices', min_value=2, max_value=5, value=4, key="Num_choice")

    q_type = st.selectbox(
        'Select the quiz type',
        ('General Vocabulary', 'Grammar'), key="q_type")

    create_quiz_button = ui.element("button", text="Create Quiz", key="button", className="m-1")
    create_quiz = st.button("Create Quiz")

# Handle button click
if create_quiz:
    st.session_state.Quiz = generate_quiz(num_quiz, num_choice, df_Sent, df_Word)
    st.write("Quiz generated successfully!")
    st.session_state.show_quiz = True
    