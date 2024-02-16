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

col1, col2 = st.columns(2)

with col1:
    Num_quiz = st.number_input('ระบุจำนวนข้อแบบทดสอบที่ต้องการสร้าง', 
                            min_value=1, max_value=100, value=20, key="Num_quiz")
with col2:
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
    ui.element("span", children=["Email"], className="text-gray-400 text-sm font-medium m-1", key="label1")
    ui.element("input", key="email_input", placeholder="Your email")

    ui.element("span", children=["User Name"], className="text-gray-400 text-sm font-medium m-1", key="label2")
    ui.element("input", key="username_input", placeholder="Create a User Name")
    ui.element("button", text="Submit", key="button", className="m-1")