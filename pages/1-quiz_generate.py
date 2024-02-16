import streamlit as st
import spacy
import random
import pandas as pd
from spacy.tokens import Token
from utils.func import generate_quiz
from streamlit_extras.switch_page_button import switch_page

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

Num_quiz = len(st.session_state.Quiz)
Num_choice = len(st.session_state.Quiz[0]["choices"])
q_type = 'แบบทดสอบความรู้คำศัพท์ทั่วไป'

with st.container(border=True):
    st.subheader("ข้อมูลแบบทดสอบ")
    st.caption(f"จำนวนข้อ: {Num_quiz} ข้อ")
    st.caption(f"จำนวนตัวเลือก: {Num_choice} ตัวเลือก")
    st.caption(f"ประเภท: {q_type}")
    quiz = st.button("เปิด")
    if quiz:
        switch_page("quiz_page")

