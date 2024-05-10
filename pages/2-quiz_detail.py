import streamlit as st
from streamlit_extras.switch_page_button import switch_page

#ซ่อน sidebar หน้าเว็บ
st.set_page_config(initial_sidebar_state="collapsed")
st.markdown(
    """
<style>
    [data-testid="collapsedControl"] {
        display: none
    }

    div.stButton > button:first-child {
    background-color: #FF4B4B;
    color:#ffffff;
    }

    div.stButton > button:hover {
    background-color: #ffffff;
    color:#FF4B4B;
    }
</style>
""",
    unsafe_allow_html=True,
)

try:
    #ชุดแบบทดสอบที่สร้างจากหน้าแรก
    Num_quiz = len(st.session_state.Quiz)
    Num_choice = len(st.session_state.Quiz[0]["choices"])
    q_type = st.session_state.Qtype


    # กล่องข้อความอธิบายแบบทดสอบ
    with st.container(border=True):
        st.subheader("ข้อมูลแบบทดสอบ")
        st.markdown(f"จำนวนข้อ: {Num_quiz} ข้อ")
        st.markdown(f"จำนวนตัวเลือก: {Num_choice} ตัวเลือก")
        st.markdown(f"หัวข้อเนื้อหา: {q_type}")
        quiz = st.button("เปิด")
        if quiz:
            switch_page("quiz_page")
            st.container.empty()

except Exception: # error แสดงปุ่มย้อนกลับไปหน้าแรก
    new_q = st.button("ย้อนกลับไปหน้าแรก")
    if new_q:
        switch_page("streamlit_app")
