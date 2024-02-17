import streamlit as st
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

try:
    Num_quiz = len(st.session_state.Quiz)
    Num_choice = len(st.session_state.Quiz[0]["choices"])
    q_type = 'แบบทดสอบความรู้คำศัพท์ทั่วไป'

    with st.container(border=True):
        st.subheader("ข้อมูลแบบทดสอบ")
        st.markdown(f"จำนวนข้อ: {Num_quiz} ข้อ")
        st.markdown(f"จำนวนตัวเลือก: {Num_choice} ตัวเลือก")
        st.markdown(f"ประเภท: {q_type}")
        quiz = st.button("เปิด")
        if quiz:
            switch_page("quiz_page")
except Exception:
    new_q = st.button("สร้างแบบทดสอบใหม่")
    if new_q:
        switch_page("streamlit_app")
