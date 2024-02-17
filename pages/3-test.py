from base64 import b64encode
from fpdf import FPDF
import streamlit as st
from datetime import datetime

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
    pdf.add_font("THSarabunB", fname="./data/THSarabun Bold.ttf", uni=True)
    pdf.set_margins(left=25, top=25, right=25)
    
    pdf.set_font("THSarabunB",  size=24)
    pdf.cell(text=f"{10*' '}แบบทดสอบภาษาอังกฤษระดับชั้นประถมศึกษาปีที่ 6", ln=True, align='L')

    pdf.set_font("THSarabun", size=18)
    pdf.cell(text=" ", ln=True, align='L')
    pdf.cell(text=f"{q_type}", align='L')
    pdf.cell(text=f"{55*' '}จำนวน {Num_quiz} ข้อ", ln=True, align='L')
    
    pdf.set_font("THSarabunB",  size=18)
    pdf.write(10, "คำชี้แจง: ")
    pdf.set_font("THSarabun", size=18)
    pdf.write(10, "เลือกคำตอบที่ถูกต้องที่สุดเพียงคำตอบเดียวลงในกระดาษคำตอบ\n")


    for i, q in enumerate(quiz_list, 1):
        question = q["question"]
        choices = q["choices"]
        quiz = ""
        # Write the question number and the question text
        quiz += f"{i}. {question}\n"
        for j, c in enumerate(choices):
            # Convert the index j to an alphabetic character
            choice_order = chr(ord('A') + j)
            # Write the choice number and the choice text
            quiz += f"    {choice_order}. {c}\n"
        
        # write quiz with no page break
        with pdf.unbreakable() as doc:
            doc.write(8, quiz)

    pdf.add_page()
    pdf.set_font("THSarabunB",  size=24)
    pdf.cell(text=f"{30*' '}เฉลยแบบทดสอบ", ln=True, align='C')

    pdf.set_font("THSarabun", size=18)
    pdf.cell(text=" ", ln=True, align='L')
    pdf.cell(text=f"{q_type}", align='L')
    pdf.cell(text=f"{55*' '}จำนวน {Num_quiz} ข้อ", ln=True, align='L')
    pdf.cell(text=" ", ln=True, align='L')

    for i, q in enumerate(quiz_list, 1):
        question = q["question"]
        choices = q["choices"]
        correct_answer = q["correct_answer"]
        for j, c in enumerate(choices):
            choice_order = chr(ord('A') + j)
            if c == correct_answer:
                correct_anwser = f"{choice_order}. {c}"
        with pdf.unbreakable() as doc:
            doc.set_font("THSarabun",  size=18)
            doc.write(8,f"{i}. {question}\n")
            doc.set_font("THSarabunB", size=18)
            doc.write(8,f"    {correct_anwser}\n")
    
    now = datetime.datetime.now()
    timestamp = f"{now:%M%H_%d%m%y}"
    return bytes(pdf.output()), f"EnglishQuiz.pdf_{timestamp}"

# Embed PDF to display it:
base64_pdf = b64encode(gen_pdf()).decode("utf-8")
pdf_display = f'<embed src="data:application/pdf;base64,{base64_pdf}" width="700" height="400" type="application/pdf">'
st.markdown(pdf_display, unsafe_allow_html=True)


# Add a download button:
st.download_button(

    label="ดาวน์โหลดแบบทดสอบ",
    data=gen_pdf()[0],
    file_name=gen_pdf()[1],
    mime="application/pdf",
)