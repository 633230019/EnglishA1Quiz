import streamlit as st
from utils.func import gen_pdf
from streamlit_extras.switch_page_button import switch_page
from base64 import b64encode
from fpdf import FPDF

# st.set_page_config(initial_sidebar_state="collapsed")
# st.markdown(
#     """
# <style>
#     [data-testid="collapsedControl"] {
#         display: none
#     }
# </style>
# """,
#     unsafe_allow_html=True,
# )

Num_quiz = len(st.session_state.Quiz)
Num_choice = len(st.session_state.Quiz[0]["choices"])
q_type = 'ประเภท: ความรู้คำศัพท์ทั่วไป'

if Num_quiz is None or Num_choice is None or Num_choice is None:
    new_q = st.button("สร้างแบบทดสอบใหม่")
    if new_q:
        switch_page("streamlit_app")
else:
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
            
        with tab2:
            st.subheader("เฉลยแบบทดสอบ")
            col1, col2 = st.columns([0.8, 0.2])
            with col1:
                st.markdown(f"**{q_type}**")
            with col2:
                st.markdown(f"**จำนวน {Num_quiz} ข้อ**")
            st.write('***')   
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

    st.download_button(
        label="ดาวน์โหลดแบบทดสอบ",
        data=gen_pdf(),
        file_name=f"EnglishQuiz.pdf",
        mime="application/pdf",
    )

    new_q = st.button("สร้างแบบทดสอบใหม่")
    if new_q:
        switch_page("streamlit_app")