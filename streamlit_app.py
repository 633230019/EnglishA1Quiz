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

with st.container(border=True):
    st.markdown("<h3 style='text-align: center;'>ระบบสร้างแบบทดสอบภาษาอังกฤษระดับชั้นประถมศึกษาปีที่ 6 แบบอัตโนมัติ</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>สร้างแบบทดสอบภาษาอังกฤษประเภทเติมคำในช่องว่างแบบอัตโนมัติ</p>", unsafe_allow_html=True)
    st.markdown("#")
    start = st.button("เริ่มสร้างแบบทดสอบ", use_container_width=True)
    if start:
        switch_page("quiz_generate")

st.markdown("#")
col1, col2, col3 = st.columns(3)
with col1:
    with st.container(height=200,border=True):
        st.markdown("<h6 style='text-align: center;'>1. สร้างแบบทดสอบ</h6>", unsafe_allow_html=True)
        st.markdown("#")
        st.markdown("ใส่จำนวนข้อสอบที่ต้องการสร้าง และข้อมูลอื่น ๆ เพื่อสร้างแบบทดสอบ")

with col2:
    with st.container(height=200,border=True):
        st.markdown("<h6 style='text-align: center;'>2. รับแบบทดสอบและเฉลยแบบทดสอบ</h6>", unsafe_allow_html=True)
        st.markdown("#")
        st.markdown("รับแบบทดสอบและเฉลยแบบทดสอบตามข้อมูลที่ได้ระบุไว้")

with col3:
    with st.container(height=200,border=True):
        st.markdown("<h6 style='text-align: center;'>3. ดาวน์โหลด</h6>", unsafe_allow_html=True)
        st.markdown("#")
        st.markdown("บันทึกแบบทดสอบและเฉลยแบบทดสอบเป็นไฟล์ PDF")

st.markdown("#")   
st.markdown("<p style='text-align: center;'>ตัวอย่างแบบทดสอบ</p>", unsafe_allow_html=True)
with st.container(height=500, border=True):
    st.image("./data/sample_exercise.jpg", use_column_width=None)
    st.markdown("#")





st.markdown("#")
with st.container(border=True):
    st.markdown("<h2 style='text-align: center;'>เกี่ยวกับระบบ</h2>", unsafe_allow_html=True)
    st.markdown("<h5>แหล่งข้อมูลของแบบทดสอบ</h5>", unsafe_allow_html=True)
    st.markdown("* ประโยคภาษาอังกฤษ ระดับ CEFR A1 จากเว็บไซต์ <a href='https://tatoeba.org/en/sentences/show_all_in/eng/none'>Tatoeba</a>", unsafe_allow_html=True)
    st.markdown("* คำศัพท์ภาษาอังกฤษระดับชั้นประถมศึกษาปีที่ 6 ระดับ CEFR A1 จากพจนานุกรม The Oxford 3000 by CEFR Level")
    st.markdown("<h5>หัวข้อเนื้อหาของแบบทดสอบ</h5>", unsafe_allow_html=True)
    st.markdown("* ทดสอบความรู้คำศัพท์ทั่วไป: เติมคำศัพท์ที่ถูกต้องในช่องว่างจากตัวเลือกคำศัพท์ทั่วไป")
    st.markdown("* ทดสอบความรู้ไวยากรณ์ Tense: เติมคำกริยาตามรูป Tense ที่ถูกต้องในช่องว่าง")
    st.markdown("<h5>หัวข้อ Tense ของแบบทดสอบ</h5>", unsafe_allow_html=True)
    st.markdown("* Present Simple Tense")
    st.markdown("* Past Simple Tense")
    st.markdown("* Future Simple Tense")
    st.markdown("* Present Continuous Tense")
    st.markdown("* Past Continuous Tense")
    st.markdown("* Future Continuous Tense")