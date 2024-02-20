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
</style>
""",
    unsafe_allow_html=True,
)

def disable():
    st.session_state.disabled = True

if "disabled" not in st.session_state:
    st.session_state.disabled = False

try:
    # st.session_state.Quiz = ชุดแบบทดสอบที่สร้างจากหน้าแรก
    Num_quiz = len(st.session_state.Quiz)
    Num_choice = len(st.session_state.Quiz[0]["choices"])
    q_type = st.session_state.Qtype


    # กล่องข้อความอธิบายแบบทดสอบ
    with st.container(border=True):
        st.subheader("ข้อมูลแบบทดสอบ")
        st.markdown(f"จำนวนข้อ: {Num_quiz} ข้อ")
        st.markdown(f"จำนวนตัวเลือก: {Num_choice} ตัวเลือก")
        st.markdown(f"ประเภท: {q_type}")
        quiz = st.button("เปิด", 
                         on_click=disable, disabled=st.session_state.disabled)
        if quiz:
            disable()
            switch_page("quiz_page")

except Exception: # error แสดงปุ่มย้อนกลับไปหน้าแรก
    new_q = st.button("สร้างแบบทดสอบใหม่")
    if new_q:
        switch_page("streamlit_app")
