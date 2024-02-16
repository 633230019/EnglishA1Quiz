import streamlit as st
import spacy
import random
import pandas as pd
from spacy.tokens import Token
from utils.func import generate_quiz
from streamlit_extras.switch_page_button import switch_page

with st.container(border=True):
    st.header("สร้างแบบทดสอบเรียบร้อย")
    st.markdown("""---""")
    st.subheader("ข้อมูลแบบทดสอบ")
    st.caption(f"จำนวนข้อ: {st.session_state.Num_quiz} ข้อ")
    st.caption(f"จำนวนตัวเลือก: {st.session_state.Num_choice} ตัวเลือก")
    st.caption(f"ประเภท: {st.session_state.q_type}")
    quiz = st.button("เปิด")
    if quiz:
        switch_page("quiz_page")

