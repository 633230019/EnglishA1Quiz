import streamlit as st
from streamlit_option_menu import option_menu
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


st.markdown("<h2 style='text-align: center;'>ระบบสร้างแบบทดสอบภาษาอังกฤษระดับชั้นประถมศึกษาปีที่ 6</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>สร้างแบบทดสอบภาษาอังกฤษประเภทเติมคำในช่องว่างแบบอัตโนมัติ</p>", unsafe_allow_html=True)
st.markdown("#")
st.markdown("#")
st.markdown("#")
st.markdown("#")
st.markdown("#")
st.markdown("#")

col1, col2 = st.columns(2)
with col1:
    start = st.button("เกี่ยวกับระบบ")
    if start:
        switch_page("about_page")
with col2:
    start = st.button("เริ่มสร้างแบบทดสอบ")
    if start:
        switch_page("quiz_generate")
