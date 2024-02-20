import streamlit as st
from utils.func import gen_pdf
from streamlit_extras.switch_page_button import switch_page
from base64 import b64encode
from fpdf import FPDF

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


try:
    # st.session_state.Quiz = ชุดข้อสอบที่สร้างจากหน้าแรก
    Num_quiz = len(st.session_state.Quiz)
    Num_choice = len(st.session_state.Quiz[0]["choices"])
    q_type = st.session_state.Qtype

    # กล่องข้อความแบบทดสอบ
    with st.container(border=True):

        #tab1 = แบบทดสอบ, tab2 = เฉลย
        tab1, tab2, = st.tabs(["แบบทดสอบ", "เฉลย"])

        with tab1: #แบบทดสอบ
            st.subheader("แบบทดสอบภาษาอังกฤษระดับชั้นประถมศึกษาปีที่ 6")

            col1, col2 = st.columns([0.8, 0.2])
            with col1:
                st.markdown(f"**ประเภท: {q_type}**")
            with col2:
                st.markdown(f"**จำนวน {Num_quiz} ข้อ**")
            st.write('***')   
            st.markdown("**คำชี้แจง**: เลือกคำตอบที่ถูกต้องที่สุดเพียงคำตอบเดียวลงในกระดาษคำตอบ")
            
            # ข้อมูลแบบทดสอบ
            quiz_list = st.session_state.Quiz
            for i, q in enumerate(quiz_list, 1):
                question = q["question"]
                choices = q["choices"]
                
                # สร้างคำถาม 1 ข้อ
                st.markdown(f"{i}.&nbsp;{question}")

                # สร้างตัวเลือกคำถาม
                for j, c in enumerate(choices):
                    # แปลงข้อมูลเลขใน index j เป็นตัวอักษร
                    choice_order = chr(ord('A') + j)
                    st.markdown(f"&nbsp;&nbsp;&nbsp;&nbsp;{choice_order}.&nbsp;{c}")
            

        with tab2: #เฉลย
            st.subheader("เฉลยแบบทดสอบ")

            col1, col2 = st.columns([0.8, 0.2])
            with col1:
                st.markdown(f"**ประเภท: {q_type}**")
            with col2:
                st.markdown(f"**จำนวน {Num_quiz} ข้อ**")
            st.write('***')   

            # ข้อมูลแบบทดสอบ
            quiz_list = st.session_state.Quiz
            for i, q in enumerate(quiz_list, 1):
                question = q["question"]
                choices = q["choices"]
                correct_answer = q["correct_answer"]
                
                # สร้างเฉลยแต่ละข้อ
                for j, c in enumerate(choices):
                    choice_order = chr(ord('A') + j)
                    if c == correct_answer:
                        correct_anwser = f"**{choice_order}. {c}**"
                st.markdown(f"{i}.&nbsp;{question}&nbsp;&nbsp;&nbsp;&nbsp;{correct_anwser}")


    # ปุ่มดาวน์โหลด pdf ใช้ฟังชั่น gen_pdf() ในไฟล์ func.py
    st.download_button(
        label="ดาวน์โหลดแบบทดสอบ",
        data=gen_pdf(),
        file_name=f"grade6englishquiz.pdf",
        mime="application/pdf",
    )

    # ปุ่มย้อนกลับไปหน้าแรก
    new_q = st.button("สร้างแบบทดสอบใหม่")
    if new_q:
        switch_page("streamlit_app")

except Exception: # error แสดงปุ่มย้อนกลับไปหน้าแรก
    new_q = st.button("สร้างแบบทดสอบใหม่")
    if new_q:
        switch_page("streamlit_app")