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
inputstartingout=print(input)
inputpage = st.sidebar.text_input("الصفحة")
st.markdown(remove_menu_footer, unsafe_allow_html=True)

if "load_state" not in st.session_state:
     st.session_state.load_state = False
if 'count' not in st.session_state:
    st.session_state.count =0
    print (st.session_state.count)
#st.session_state.count += 1
if st.session_state.count == 0:
    st.session_state.count = 1
    print (st.session_state.count)




if input=="":
    req = requests.get(f"https://dorar-hadith-api.herokuapp.com/api/search?value=انما الاعمال بنيات")
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
        

pagenum = st.session_state.count
print(pagenum)
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

if st.button("next",kwargs=dict(increment_value=1)) and inputstartingout !="":
    increment_value = 1
    st.session_state.count += increment_value
    print ("def"+str(st.session_state.count))

decrement_button = st.button("previous",kwargs=dict(decrement_value=1))

if decrement_button and inputstartingout !="":
    decrement_value = 1
    st.session_state.count -= decrement_value
    print ("def"+str(st.session_state.count))    

align_left = f"<p style='text-align:right;'>{decrement_button}</p>"
#st.button("next",on_click=button_hadith(),kwargs=dict(increment_value=1))   
#st.markdown(f"<p style='text-align:right;'>< button  onclick = ""  > Search  </ button ></p>",unsafe_allow_html=True)

#color = f"<p style='color:red;'>{source}</p>"

#st.markdown(color,unsafe_allow_html=True)
