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

st.header("เกี่ยวกับระบบ")
st.markdown("#")
st.markdown("-")
st.markdown("-")
st.markdown("-")

col1, col2, col3 = st.columns(3)
with col2:
    back = st.button("ย้อนกลับ", use_container_width=True)
    if back:
        switch_page("streamlit_app")