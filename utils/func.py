import spacy
import random
import pandas as pd
from base64 import b64encode
from fpdf import FPDF
import streamlit as st
from spacy.tokens import Token
nlp = spacy.load("en_core_web_sm")


# comment
# comment
# comment
# comment

def generate_quiz(num_quiz, num_choice, df_Sent, df_Word):

  def get_random_sentences(df, num_sentences):
      num_rows = len(df)
      if num_sentences > num_rows:
          num_sentences = num_rows  # Ensure not to select more sentences than available rows
      
      random_indices = random.sample(range(num_rows), num_sentences)  # Randomly select indices
      random_sentences = df.iloc[random_indices]['Sentence'].tolist()  # Retrieve sentences at selected indices
      
      return random_sentences

  def filter_pos(token):
    if token.pos_ in ["VERB","NOUN","ADV","ADJ"] and token.lemma_ != "do":
      return True
    else:
      return False

  def format_pos(token):
    token = token.pos_
    if token == "NOUN":
      return "noun"
    if token == "VERB":
      return "verb"
    if token == "ADJ":
      return "adjective"
    if token == "ADV":
      return "adverb"
    else:
      return token
  
  def get_wrong_choices(token,num_choices):
    pos_list = ["noun", "verb", "adjective", "adverb"] #สุ่มเฉพาะ Part of speech ใน list
    pos_list.remove(format_pos(token)) #ลบ Part of speech ของ Token ออกจาก list
    random.shuffle(pos_list)
    filtered_pos = pos_list[0]

    #return 1 คำ ที่ไม่ใช่คำเดียวกับ token และที่ไม่เป็นชนิดเดียวกัน
    filtered_df = df_Word[(df_Word['Word'] != token.lemma_) & (df_Word['PartofSpeech'] == filtered_pos)]
    choices = filtered_df.sample(num_choices-1)['Word'].values
    return choices.tolist()


  quiz_questions = []

  sentences = get_random_sentences(df_Sent, num_quiz)
  for sentence in sentences:
    doc = nlp(sentence)
    filter_choices = []

    # Iterate over the tokens again to filter keywords
    for token in doc:
      if filter_pos(token):
        filter_choices.append(token)

    correct_choice = random.choice(filter_choices)
    wrong_choices = get_wrong_choices(correct_choice,num_choice)
    bold_correct_choice = "**"+correct_choice.text+"**"
    sentence = doc.text
    question = sentence.replace(correct_choice.text, "____", 1)
    correct_sentence = sentence.replace(correct_choice.text, bold_correct_choice, 1)
    all_choices = [correct_choice.text] + wrong_choices
    random.shuffle(all_choices)
    quiz_question = {
          "question": question,
          "choices": all_choices,
          "correct_answer": correct_choice.text,
          "correct_sentence": correct_sentence
    }
    quiz_questions.append(quiz_question)

  return quiz_questions



@st.cache_data
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
          choice_order = chr(ord('A') + j)
          if c == correct_answer:
              correct_anwser = f"{choice_order}. {c}"
      with pdf.unbreakable() as doc:
          doc.set_font("THSarabun",  size=18)
          doc.write(8,f"{i}. {question}\n")
          doc.set_font("THSarabunB", size=18)
          doc.write(8,f"    {correct_anwser}\n")

  return bytes(pdf.output())