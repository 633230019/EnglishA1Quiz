import streamlit as st
import spacy
import random
import pandas as pd
from spacy.tokens import Token
from utils.func import generate_quiz
from streamlit_extras.switch_page_button import switch_page


st.header("สร้างแบบทดสอบเรียบร้อย")
st.markdown("""---""")

quiz = st.button("เปิด")
if quiz:
    switch_page("quiz_page")

