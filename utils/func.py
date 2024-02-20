import spacy
import random
import pandas as pd
from base64 import b64encode
from fpdf import FPDF
import streamlit as st
import lemminflect
from spacy.tokens import Token
nlp = spacy.load("en_core_web_sm")

def generate_quiz(num_quiz, num_choice, q_type_code, df_Sent, df_Word):

  def format_pos(token): #ปรับรูปแบบให้ตรงตามข้อมูลในตาราง
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


  def get_random_sentences(num_sentences): #สุ่มเลือกประโยคจากตาราง
    random_sentences = []

    if q_type_code == "1": #ประโยคสำหรับแบบทดสอบทั่วไป
      num_rows = len(df_Sent)
      random_indices = random.sample(range(num_rows), num_sentences)
      random_sentences = df_Sent.iloc[random_indices]['Sentence'].tolist()

    if q_type_code == "2": #ประโยคสำหรับแบบทดสอบ tense
      while len(random_sentences) < num_sentences:
        #สุ่ม 1 ประโยค จากตาราง
        text = df_Sent["Sentence"].sample().values[0]
        if text in random_sentences:
          continue #ข้ามประโยคซ้ำ

        doc = nlp(text)
        easy_tense = True #เช็คระดับ tense พื้นฐาน
        verb_num = 0 #เช็คจำนวนคำกริยาในประโยค

        for token in doc:
          if token.pos_ == "AUX" and token.lemma_ == "have":
            easy_tense = False
            break
          if token.text == "been":
            easy_tense = False
            break
          if token.lemma_ == "be" and "'" in token.text:
            verb_num -+ 0 #ไม่นับ verb to be ที่มีเครื่องหมาย '
          elif token.pos_ == "VERB":
            verb_num += 1
        if easy_tense and verb_num > 1:
          #เปลี่ยนคำย่อเป็นคำเต็ม
          text = text.replace("'m", " am")
          text = text.replace("'re", " are")
          text = text.replace("it's", " it is")
          text = text.replace("he's", " he is")
          text = text.replace("she's", " she is")
          text = text.replace("isn't", "is not")
          text = text.replace("aren't", "are not")
          text = text.replace("weren't", "were not")
          text = text.replace("wasn't", "was not")
          random_sentences.append(text)
    return random_sentences


  def get_verb_from_sentence(doc): #เลือกช้อยที่เป็น verb จากประโยค
    verbs = []
    first_word_skipped = False
    for i, token in enumerate(doc):

      if not first_word_skipped: #ข้ามคำแรกของประโยค
        first_word_skipped = True
        continue

      if token.pos_ == "VERB" and token.tag_ == "VBG":
        verbs.append(token) # เพิ่มคำกริยารูป Continuous
      elif token.lemma_ == "be":
        verbs.append(token) # เพิ่ม verb to be แบบไม่มี n't ลงท้าย
      elif token.pos_ == "VERB":
        verbs.append(token) # เพิ่มคำกริยาใส่ verbs

    random.shuffle(verbs)
    for token in verbs:
      if token.tag_ == "VBG":
        verb = token # สุ่ม 1 คำรูป Continuous จาก verbs
        break
      else:
        verb = random.choice(verbs)  # สุ่ม 1 คำจาก verbs
    return verb


  def get_choice_from_sentence(doc): #เลือกช้อยคำที่มีความหมายจากประโยค
    possible_choices = []
    first_word_skipped = False
    for token in doc:

      if not first_word_skipped: #ข้ามคำแรกของประโยค
        first_word_skipped = True
        continue

      if token.pos_ in ["VERB","NOUN","ADV","ADJ"] and (token.lemma_ != "do" or token.lemma_ != "be"):
      # เพิ่มคำที่มีความหมาย ที่ไม่ใช่ do, be
        possible_choices.append(token)

    choice = random.choice(possible_choices) # สุ่ม 1 คำ
    return choice


  def get_wrong_choices(token,num_choices):
  #สุ่มตัวเลือกหลอกสำหรับแบบทดสอบทั่วไป

    pos_list = ["noun", "verb", "adjective", "adverb"] #สุ่มเฉพาะ Part of speech ใน list
    pos_list.remove(format_pos(token)) #ลบ Part of speech ของ Token ออกจาก list
    #คัดเฉพาะชนิดคำที่อยู่ใน pos_list
    filtered_df = df_Word[(df_Word['Word'] != token.lemma_) & (df_Word['PartofSpeech'].isin(pos_list))]
    #สุ่มเลือกคำจากตารางคอลัมน์ word ลบหนึ่งตัวเลือกแยกเป็นคำตอบ
    choices = filtered_df.sample(num_choices-1)['Word'].values
    return choices.tolist()


  def get_wrong_verbs(token, num_choices):
  #สุ่มตัวเลือกหลอกสำหรับแบบทดสอบ tense

    #tag info https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html
    #https://universaldependencies.org/u/pos/
    forms_tag = ["VB", "VBD", "VBG", "VBN", "VBP", "VBD", "VBZ"]
    verb_list = [token.text]

    if token.tag_ == "VBD":  #คำกริยา past simple
      forms_tag = ["VBD", "VBG", "VBN", "VBD"] #เอาคำประเภท VB VBZ VBP ออก
      suffix = ["s", "ed",]
      for i in suffix: #เติม s ed ลงท้ายคำศัพท์
        verb_list.append(token._.inflect("VBD")+i)
        verb_list.append(token._.inflect("VBN")+i)

    for tag in forms_tag: # เพิ่มรูปคำกริยาตาม forms_tag ใส่ใน verb list
      verb_list.append(token._.inflect(tag))

    verb_list = list(set(verb_list)) #ลบคำที่ซ้ำกันออกจาก list
    verb_list.remove(token.text) #ลบ token คำตอบออกจาก list

    if len(verb_list) < num_choices-1:
      if token._.inflect("VB")[-1] == "e" or token._.inflect("VBD")[-1] == "e": #คำลงท้ายด้วย e
      #เติม d, ds, r ลงท้ายคำศัพท์
        verb_list.append(token._.inflect("VB")+"d")
        verb_list.append(token._.inflect("VB")+"ds")
        verb_list.append(token._.inflect("VB")+"r")
      else:
      #เติม ed, eds, er ลงท้ายคำศัพท์
        verb_list.append(token._.inflect("VB")+"ed")
        verb_list.append(token._.inflect("VB")+"eds")
        verb_list.append(token._.inflect("VB")+"er")

    if token.text == "am":
      verb_list = ["be", "being", "are", "is", "were"]
    if token.text == "is":
      verb_list = ["be", "being", "am", "are", "were"]
    if token.text == "was":
      verb_list = ["be", "being", "are", "were"]
    if token.text == "are" or token.text == "were":
      verb_list = ["be", "being", "am",  "is", "was"]

    verb_list = list(set(verb_list)) #ลบคำที่ซ้ำกันออกจาก list
    #สุ่มตัวเลือกตาม num_choices ลบหนึ่งตัวเลือกแยกเป็นคำตอบ
    verb_list = random.sample(verb_list, num_choices-1)
    return verb_list


  #เตรียมสร้างแบบทดสอบ
  quiz_list = []
  sentences = get_random_sentences(num_quiz) #สุ่มประโยคตามจำนวนที่ใส่

  for sentence in sentences:
    doc = nlp(sentence)
    sentence = doc.text
    while True: #สร้างคำถาม 1 ข้อ
        if q_type_code == "1": #แบบทดสอบทั่วไป 
            #print("sentence:",sentence)
            correct_choice = get_choice_from_sentence(doc) #หาคำตอบ
            #print("answer: ", correct_choice)
            wrong_choices = get_wrong_choices(correct_choice, num_choice) #หาตัวเลือกหลอก
            #print("wrong choices: ", wrong_choices)
        if q_type_code == "2": #แบบทดสอบ tense
            correct_choice = get_verb_from_sentence(doc) #หาคำตอบ
            wrong_choices = get_wrong_verbs(correct_choice,num_choice) #หาตัวเลือกหลอก
        
        #เช็คว่าคำถามไม่มีตัวอักษรติดช่อง ____
        question = sentence.replace(correct_choice.text, "____", 1)
        position = question.index("____")
        if len(question) > position + 4:
            if not question[position - 1].isalpha() and not question[position + 4].isalpha():
              break

    # เพิ่มสัญลักษณ์ฟ้อนตัวหนาใส่คำตอบ
    bold_correct_choice = "**"+correct_choice.text+"**"
    correct_sentence = sentence.replace(correct_choice.text, bold_correct_choice, 1)

    all_choices = [correct_choice.text] + wrong_choices
    random.shuffle(all_choices)

    quiz_question = {
          "question": question,
          "choices": all_choices,
          "correct_answer": correct_choice.text,
          "correct_sentence": correct_sentence
    }
    quiz_list.append(quiz_question)

  return quiz_list
  #return None



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