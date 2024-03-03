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

def navigation_bar():
    with st.container():
        selected = option_menu(
            menu_title=None,
            options=["หน้าแรก", "สร้างแบบทดสอบ", "เกี่ยวกับระบบ"],
            #icons=['house', 'cloud-upload', "graph-up-arrow", 'gear', 'phone'],
            menu_icon="cast",
            orientation="horizontal",
            styles={
                "nav-link": {
                    "text-align": "left",
                    "--hover-color": "#eee",
                }
            }
        )
        if selected == "หน้าแรก":
            switch_page("streamlit_app")
        if selected == "สร้างแบบทดสอบ":
            switch_page("quiz_setting")
        if selected == "เกี่ยวกับระบบ":
            switch_page("about_page")


    
try:
    #navigation_bar()
    with st.container(border=True):

        st.header("ระบบสร้างแบบทดสอบภาษาอังกฤษระดับชั้นประถมศึกษาปีที่ 6 แบบอัตโนมัติ")
        st.markdown("#")
        st.markdown("สร้างแบบทดสอบโดยใช้ ประโยคภาษาอังกฤษจากเว็บไซต์ Tatoeba และคำศัพท์ภาษาอังกฤษพื้นฐานชั้นป.6 จาก พจนานุกรม Oxford 3,000 ")

        col1, col2, col3 = st.columns(3)
        with col1:
            start = st.button("เกี่ยวกับระบบ", use_container_width=True)
            if start:
                switch_page("about_page")
                st.container.empty()
        with col3:
            start = st.button("เริ่มสร้างแบบทดสอบ", use_container_width=True)
            if start:
                switch_page("quiz_setting")
                st.container.empty()

except Exception:
    st.markdown(''':red[เกิดข้อผิดพลาด กรุณาสร้างแบบทดสอบใหม่อีกครั้ง]''')