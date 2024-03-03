import streamlit as st
from streamlit_extras.switch_page_button import switch_page

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