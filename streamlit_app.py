import streamlit as st
import pandas as pd
from utils.func import generate_quiz, gen_pdf
from base64 import b64encode
from streamlit_extras.switch_page_button import switch_page

import streamlit as st

#ซ่อน sidebar หน้าเว็บ
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

# ไฟล์แบบทดสอบ
df_Sent=pd.read_csv("./data/filtered_sentences_dataset_a1_20k.csv")
df_Word=pd.read_csv("./data/oxford_a1.csv")

# กล่องข้อความ
with st.container(border=True):

    st.header("สร้างแบบทดสอบภาษาอังกฤษระดับชั้นประถมศึกษาปีที่ 6")
    st.markdown("#")

    # number input จำนวนข้อ จำนวนตัวเลือก
    col1, col2 = st.columns(2)
    with col1:
        Num_quiz = st.number_input('ระบุจำนวนข้อแบบทดสอบที่ต้องการสร้าง', 
                                min_value=1, max_value=100, value=10, key="Num_quiz")
    with col2:
        Num_choice = st.number_input('ระบุจำนวนตัวเลือกแบบทดสอบ', 
                                min_value=2, max_value=5, value=4, key="Num_choice")
        
    # select box ประเภทแบบทดสอบ
    q_type = st.selectbox(
        'ระบุประเภทแบบทดสอบ',
        ('ความรู้คำศัพท์ทั่วไป','ความรู้ไวยากรณ์ Tense'), key="q_type")
    st.markdown("#")

    if q_type == "ความรู้คำศัพท์ทั่วไป":
        q_type_code = "1"
    if q_type == "ความรู้ไวยากรณ์ Tense":
        q_type_code = "2"

    # ปุ่มสร้างแบบทดสอบ
    columns = st.columns((1, 1, 1))
    button_pressed = columns[1].button('สร้างแบบทดสอบ')



    # ปุ่มสร้างแบบทดสอบ ใช้ฟังชั่น generate_quiz() ในไฟล์ func.py
try:
    if button_pressed:
        st.cache_resource.clear()
        with st.spinner('กำลังสร้างแบบทดสอบ...'):
            st.session_state.Quiz = generate_quiz(Num_quiz, Num_choice, q_type_code, df_Sent, df_Word)
        st.session_state.Qtype = q_type
        switch_page("quiz_generate")
        with st.spinner('กำลังสร้างไฟล์แบบทดสอบ...'):
            st.session_state.pdf = gen_pdf()
except Exception:
    st.markdown(''':red[เกิดข้อผิดพลาด กรุณาสร้างแบบทดสอบใหม่อีกครั้ง]''')
