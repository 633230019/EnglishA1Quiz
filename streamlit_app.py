import streamlit as st
import spacy
import random
import pandas as pd
from spacy.tokens import Token
from utils.func import generate_quiz
from streamlit_extras.switch_page_button import switch_page

df_Sent=pd.read_csv("./data/filtered_sentences_dataset_a1_20k.csv")
df_Word=pd.read_csv("./data/oxford_a1.csv")

st.header("สร้างแบบทดสอบภาษาอังกฤษระดับป.6")

Num_quiz = st.number_input('ระบุจำนวนข้อแบบทดสอบที่ต้องการสร้าง', key="Num_quiz")

    
Num_choice = st.selectbox(
    'ระบุจำนวนตัวเลือกของแต่ละข้อแบบทดสอบ',
    ('2','3','4','5'), key="Num_choice")
    
q_type = st.selectbox(
    'ระบุประเภทแบบทดสอบ',
    ('ทดสอบความรู้คำศัพท์ทั่วไป','ทดสอบความรู้ไวยากรณ์'), key="q_type")

create_quiz = st.button("สร้างแบบทดสอบ")
if create_quiz:
    st.session_state.Quiz = generate_quiz(st.session_state.Num_quiz, st.session_state.Num_choice, df_Sent, df_Word)
    switch_page("1-quiz_generate")