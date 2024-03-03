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


    

navigation_bar()
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
    start = st.button("เกี่ยวกับระบบ", use_container_width=True)
    if start:
        switch_page("about_page")
        st.container.empty()
with col2:
    start = st.button("เริ่มสร้างแบบทดสอบ", use_container_width=True)
    if start:
        switch_page("quiz_generate")
        st.container.empty()
