from base64 import b64encode
from fpdf import FPDF
import streamlit as st


Num_quiz = len(st.session_state.Quiz)
Num_choice = len(st.session_state.Quiz[0]["choices"])
q_type = 'ประเภท: ความรู้คำศัพท์ทั่วไป'
quiz_list = st.session_state.Quiz


st.title("Demo of fpdf2 usage with streamlit")

@st.cache_data
def gen_pdf():
    pdf = FPDF()
    pdf.add_page()
    pdf.add_font("THSarabun", fname="./data/THSarabun.ttf", uni=True)
    pdf.set_margins(left=25, top=25, right=25)
    pdf.set_font("THSarabun", style="B", size=24)
    pdf.cell(text="แบบทดสอบภาษาอังกฤษระดับชั้นประถมศึกษาปีที่ 6", ln=True, align='C')
    pdf.set_font("THSarabun", size=18)
    pdf.cell(text=f"{q_type}", align='L')
    pdf.cell(text=f"{50*' '}จำนวน {Num_quiz} ข้อ", ln=True, align='L')
    pdf.Line(25, pdf.get_y(), 575, pdf.get_y())
    pdf.cell(text="คำชี้แจง: เลือกคำตอบที่ถูกต้องที่สุดเพียงคำตอบเดียวลงในกระดาษคำตอบ", ln=True, align='L')
    for i, q in enumerate(quiz_list, 1):
        question = q["question"]
        choices = q["choices"]
        
        # Write the question number and the question text
        pdf.cell(text=f"{i}. {question}", ln=True, align='L')

        for j, c in enumerate(choices):
            # Convert the index j to an alphabetic character
            choice_order = chr(ord('A') + j)
            # Write the choice number and the choice text
            pdf.cell(text=f"    {choice_order}. {c}", ln=True, align='L')
    return bytes(pdf.output())

# Embed PDF to display it:
base64_pdf = b64encode(gen_pdf()).decode("utf-8")
pdf_display = f'<embed src="data:application/pdf;base64,{base64_pdf}" width="700" height="400" type="application/pdf">'
st.markdown(pdf_display, unsafe_allow_html=True)

# Add a download button:
st.download_button(
    label="Download PDF",
    data=gen_pdf(),
    file_name="file_name.pdf",
    mime="application/pdf",
)