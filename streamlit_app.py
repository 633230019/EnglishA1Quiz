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

st.number_input('ระบุจำนวนข้อแบบทดสอบที่ต้องการสร้าง',
min_value=1, max_value=100, value=int, key="Num_Quiz")

    
st.session_state.Num_choice = st.selectbox(
    'ระบุจำนวนตัวเลือกของแต่ละข้อแบบทดสอบ',
    ('2','3','4','5'), key="Num_choice")
    
st.session_state.Quiz_Type = st.selectbox(
    'ระบุประเภทแบบทดสอบ',
    ('ทดสอบความรู้คำศัพท์ทั่วไป'), key="q_type")

create_quiz = st.button("สร้างแบบทดสอบ")
if create_quiz:
    st.session_state.Quiz = generate_quiz(st.session_state.Num_Quiz, st.session_state.Num_choice, df_Sent, df_Word)
    switch_page("1-quiz_generate")