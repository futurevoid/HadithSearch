import streamlit as st
import requests
from math import *

st.set_page_config(
         page_title="احاديث الدرر السنيه",
     page_icon="📖",
     initial_sidebar_state="expanded"
     
 )
title =st.title("احاديث الدرر السنيه")
remove_menu_footer = """
<style>
#MainMenu {visibility: hidden;}
footer { visibility:hidden; }
</style>
"""
input = st.sidebar.text_input("اكتب حديث")
inputpage = st.sidebar.text_input("الصفحة")
st.markdown(remove_menu_footer, unsafe_allow_html=True)

if "load_state" not in st.session_state:
     st.session_state.load_state = False
if 'count' not in st.session_state:
    st.session_state.count =0
st.session_state.count += 1

def button_hadith(increment_value=1):
    st.session_state.count += increment_value
    print (st.session_state.count)


# def button_hadith():
#     pagenum = st.session_state.count
#     pagenum=pagenum+1
#     req = requests.get(f"https://dorar-hadith-api.herokuapp.com/api/search?value={input}&page={pagenum}")
#     data = req.json()
#     data_len=len(data)
#     print(pagenum)
#     for i in range(data_len):
#         number = i
#         hadith_uncleaned = data[number]["hadith"]
#         hadith = hadith_uncleaned.replace(".", "")
#         source = data[number]["source"]
#         rawi = data[number]["el_rawi"]
#         mohdith = data[number]["el_mohdith"]
#         numpage = data[number]["number_or_page"]
#         grade = data[number]["grade"]
#         align_right_i = f"<p style='text-align:right;'>{i+1}</p>"
#         st.markdown(align_right_i, unsafe_allow_html=True)
#         st.markdown(f"<p style='text-align:right;'>الحديث: {hadith}</p>", unsafe_allow_html=True)
#         align_right = f"<p style='text-align:right;'>الراوي: {rawi}  |المحدث: {mohdith}  |المصدر: {source}</p>"
#         st.markdown(align_right,unsafe_allow_html=True)
#         st.markdown(f"<p style='text-align:right;'>خلاصة حكم الحديث: {grade}  | الصفحة أو الرقم: {numpage}  </p>",unsafe_allow_html=True)
#         st.markdown("<br>",unsafe_allow_html=True)
        

pagenum = st.session_state.count
req = requests.get(f"https://dorar-hadith-api.herokuapp.com/api/search?value={input}&page={pagenum}")
data = req.json()
data_len=len(data)
for i in range(data_len):
    number = i
    hadith_uncleaned = data[number]["hadith"]
    hadith = hadith_uncleaned.replace(".", "")
    source = data[number]["source"]
    rawi = data[number]["el_rawi"]
    mohdith = data[number]["el_mohdith"]
    numpage = data[number]["number_or_page"]
    grade = data[number]["grade"]
    align_right_i = f"<p style='text-align:right;'>{i+1}</p>"
    st.markdown(align_right_i, unsafe_allow_html=True)
    st.markdown(f"<p style='text-align:right;'>الحديث: {hadith}</p>", unsafe_allow_html=True)
    align_right = f"<p style='text-align:right;'>الراوي: {rawi}  |المحدث: {mohdith}  |المصدر: {source}</p>"
    st.markdown(align_right,unsafe_allow_html=True)
    st.markdown(f"<p style='text-align:right;'>خلاصة حكم الحديث: {grade}  | الصفحة أو الرقم: {numpage}  </p>",unsafe_allow_html=True)
    st.markdown("<br>",unsafe_allow_html=True)
st.button("next",on_click=button_hadith(),kwargs=dict(increment_value=1))   
#st.markdown(f"<p style='text-align:right;'>< button  onclick = ""  > Search  </ button ></p>",unsafe_allow_html=True)

#color = f"<p style='color:red;'>{source}</p>"

#st.markdown(color,unsafe_allow_html=True)
