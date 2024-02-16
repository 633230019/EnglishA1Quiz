import streamlit as st
import spacy
import random
import pandas as pd
from spacy.tokens import Token
from utils.func import generate_quiz
from streamlit_extras.switch_page_button import switch_page
from streamlit_extras.stylable_container import stylable_container

df_Sent=pd.read_csv("./data/filtered_sentences_dataset_a1_20k.csv")
df_Word=pd.read_csv("./data/oxford_a1.csv")

st.set_page_config(initial_sidebar_state="collapsed")
st.markdown(
    """
<style>
    [data-testid="collapsedControl"] {
        display: none
    }
</style>
""",
    unsafe_allow_html=True,
)

with st.container(border=True):
    st.header("สร้างแบบทดสอบภาษาอังกฤษระดับชั้นประถมศึกษาปีที่ 6")
    st.markdown("#")
    col1, col2 = st.columns(2)

    with col1:
        Num_quiz = st.number_input('ระบุจำนวนข้อแบบทดสอบที่ต้องการสร้าง', 
                                min_value=1, max_value=100, value=10, key="Num_quiz")
    with col2:
        Num_choice = st.number_input('ระบุจำนวนตัวเลือกแบบทดสอบ', 
                                min_value=2, max_value=5, value=4, key="Num_choice")
        
    q_type = st.selectbox(
        'ระบุประเภทแบบทดสอบ',
        ('ทดสอบความรู้คำศัพท์ทั่วไป','ทดสอบความรู้ไวยากรณ์'), key="q_type")

    st.markdown("#")
    columns = st.columns((1, 1, 1))
    button_pressed = columns[1].button('สร้างแบบทดสอบ')

    if button_pressed:
        st.session_state.Quiz = generate_quiz(Num_quiz, Num_choice, df_Sent, df_Word)
        switch_page("quiz_generate")
