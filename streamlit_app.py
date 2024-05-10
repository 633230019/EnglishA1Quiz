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
    # st.markdown("สร้างแบบทดสอบภาษาอังกฤษประเภทเติมคำในช่องว่างแบบอัตโนมัติ")
    st.markdown("#")
    start = st.button("เริ่มสร้างแบบทดสอบ", use_container_width=True)
    if start:
        switch_page("quiz_generate")

with st.container(height=500, border=False):
    st.image("./data/sample_exercise.jpg", use_column_width=None)

col1, col2, col3 = st.columns(3)
with col1:
    with st.container(height=300,border=True):
        st.markdown("<h4 style='text-align: center;'>1. สร้างแบบทดสอบ</h4>", unsafe_allow_html=True)
        st.markdown("#")
        st.markdown("ใส่จำนวนข้อสอบที่ต้องการสร้าง และข้อมูลอื่น ๆ เพื่อสร้างแบบทดสอบ")


with col2:
    with st.container(height=300,border=True):
        st.markdown("<h4 style='text-align: center;'>2. รับแบบทดสอบและเฉลยแบบทดสอบ</h4>", unsafe_allow_html=True)
        st.markdown("#")
        st.markdown("รับแบบทดสอบและเฉลยแบบทดสอบตามข้อมูลที่ได้ระบุไว้")


with col3:
    with st.container(height=300,border=True):
        st.markdown("<h4 style='text-align: center;'>3. ดาวน์โหลด</h4>", unsafe_allow_html=True)
        st.markdown("#")
        st.markdown("บันทึกแบบทดสอบและเฉลยแบบทดสอบเป็นไฟล์ PDF")



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