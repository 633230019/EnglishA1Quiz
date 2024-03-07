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

with st.container(border=True):
    st.markdown("<h2 style='text-align: center;'>ระบบสร้างแบบทดสอบภาษาอังกฤษระดับชั้นประถมศึกษาปีที่ 6</h2>", unsafe_allow_html=True)
    st.markdown("<b style='text-align: center;'>สร้างแบบทดสอบภาษาอังกฤษประเภทเติมคำในช่องว่างแบบอัตโนมัติ</b>", unsafe_allow_html=True)
    st.markdown("<h5>1. กำหนดค่าแบบทดสอบ</h5>", unsafe_allow_html=True)
    st.markdown("ระบุจำนวนข้อแบบทดสอบที่ต้องการ เลือกจำนวนตัวเลือกต่อข้อ (4 ตัวเลือกเป็นค่ามาตรฐาน) ประเภทแบบทดสอบ")
    st.markdown("<h5>2. สร้างแบบทดสอบ</h5>", unsafe_allow_html=True)
    st.markdown("สร้างแบบทดสอบโดยรูปแบบการสุ่มประโยคและคำศัพท์จากฐานข้อมูล พร้อมกับเฉลยแบบทดสอบ")
    st.markdown("<h5>3. ดาวน์โหลด</h5>", unsafe_allow_html=True)
    st.markdown("บันทึกแบบทดสอบและเฉลยเป็นไฟล์ PDF พิมพ์แบบทดสอบ")
    st.markdown("#")
    st.markdown("#")
    start = st.button("เริ่มสร้างแบบทดสอบ", use_container_width=True)
    if start:
        switch_page("quiz_generate")

st.markdown("#")
with st.container(border=True):
    st.markdown("<h2 style='text-align: center;'>เกี่ยวกับระบบ</h2>", unsafe_allow_html=True)
    st.markdown("<h5>แหล่งข้อมูลของแบบทดสอบ</h5>", unsafe_allow_html=True)
    st.markdown("* ประโยคภาษาอังกฤษจากเว็บไซต์ Tatoeba")
    st.markdown("* คำศัพท์ภาษาอังกฤษระดับชั้นประถมศึกษาปีที่ 6 จากพจนานุกรม Oxford 3,000")
    st.markdown("<h5>ประเภทของแบบทดสอบ</h5>", unsafe_allow_html=True)
    st.markdown("* ทดสอบความรู้คำศัพท์ทั่วไป: เติมคำศัพท์ที่ถูกต้องในช่องว่างจากตัวเลือกคำศัพท์ทั่วไป")
    st.markdown("* ทดสอบความรู้ไวยากรณ์ Tense: เติมคำกริยาตามรูป Tense ที่ถูกต้องในช่องว่าง")
    st.markdown("<h5>หัวข้อ Tense ของแบบทดสอบ</h5>", unsafe_allow_html=True)
    st.markdown("* Present Simple Tense")
    st.markdown("* Past Simple Tense")
    st.markdown("* Future Simple Tense")
    st.markdown("* Present Continuous Tense")
    st.markdown("* Past Continuous Tense")
    st.markdown("* Future Continuous Tense")