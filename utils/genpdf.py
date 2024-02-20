import pandas as pd
from base64 import b64encode
from fpdf import FPDF
import streamlit as st


@st.cache_resource(show_spinner=False)
def gen_pdf():
  Num_quiz = len(st.session_state.Quiz)
  Num_choice = len(st.session_state.Quiz[0]["choices"])
  q_type = st.session_state.Qtype
  quiz_list = st.session_state.Quiz

  pdf = FPDF()
  pdf.add_page()
  pdf.add_font("THSarabun", fname="./data/THSarabun.ttf", uni=True)
  pdf.add_font("THSarabunB", fname="./data/THSarabun Bold.ttf", uni=True)
  pdf.set_margins(left=25, top=25, right=25)
  
  pdf.set_font("THSarabunB",  size=24)
  pdf.cell(text=f"{10*' '}แบบทดสอบภาษาอังกฤษระดับชั้นประถมศึกษาปีที่ 6", ln=True, align='L')

  pdf.set_font("THSarabunB", size=18)
  pdf.cell(text=" ", ln=True, align='L')
  pdf.cell(text=f"ประเภท: {q_type}", align='L')
  pdf.cell(text=f"{55*' '}จำนวน {Num_quiz} ข้อ", ln=True, align='L')
  
  pdf.set_font("THSarabunB",  size=18)
  pdf.write(10, "คำชี้แจง: ")
  pdf.set_font("THSarabun", size=18)
  pdf.write(10, "เลือกคำตอบที่ถูกต้องที่สุดเพียงคำตอบเดียวลงในกระดาษคำตอบ\n")


  for i, q in enumerate(quiz_list, 1):
      question = q["question"]
      choices = q["choices"]
      quiz = ""

      # เพิ่มคำถามใส่ quiz
      quiz += f"{i}. {question}\n"
      
      for j, c in enumerate(choices):
          # แปลงข้อมูลเลขใน index j เป็นตัวอักษร
          choice_order = chr(ord('A') + j)
          # เพิ่มตัวเลือกใส่ quiz
          quiz += f"    {choice_order}. {c}\n"
      
      with pdf.unbreakable() as doc: # เพิ่มใส่แบบไม่ถูกตัดกลางหน้ากระดาษ
          doc.write(8, quiz)

  pdf.add_page()
  pdf.set_font("THSarabunB",  size=24)
  pdf.cell(text=f"{30*' '}เฉลยแบบทดสอบ", ln=True, align='C')

  pdf.set_font("THSarabunB", size=18)
  pdf.cell(text=" ", ln=True, align='L')
  pdf.cell(text=f"ประเภท: {q_type}", align='L')
  pdf.cell(text=f"{55*' '}จำนวน {Num_quiz} ข้อ", ln=True, align='L')
  pdf.cell(text=" ", ln=True, align='L')

  for i, q in enumerate(quiz_list, 1):
      question = q["question"]
      choices = q["choices"]
      correct_answer = q["correct_answer"]
      for j, c in enumerate(choices):
          # แปลงข้อมูลเลขใน index j เป็นตัวอักษร
          choice_order = chr(ord('A') + j) 
          if c == correct_answer:
              correct_anwser = f"{choice_order}. {c}"
      with pdf.unbreakable() as doc: # เพิ่มใส่แบบไม่ถูกตัดกลางหน้ากระดาษ
          doc.set_font("THSarabun",  size=18)
          doc.write(8,f"{i}. {question}\n")
          doc.set_font("THSarabunB", size=18)
          doc.write(8,f"    {correct_anwser}\n")

  return bytes(pdf.output())