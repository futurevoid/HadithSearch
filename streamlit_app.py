from this import d
import streamlit as st
import requests
from math import *

st.set_page_config(
         page_title="احاديث الدرر السنيه",
     page_icon="📖",
     initial_sidebar_state="collapsed",
 )

title =st.title("احاديث الرسول ص من الدرر السنيه")

remove_menu_footer = """
<style>
#MainMenu {visibility: hidden;}
footer { visibility:hidden; }
</style>
"""

st.markdown(
     """
     <style>
     [data-testid="stSidebar"][aria-expanded="true"] > div:first-child {
         width: 300px;
       }
        </style>
        """,
        unsafe_allow_html=True)

input = st.sidebar.text_input("اكتب حديث")
inputstartingout=print(input)
st.markdown(remove_menu_footer, unsafe_allow_html=True)

if "load_state" not in st.session_state:
     st.session_state.load_state = False

if 'count' not in st.session_state:
    st.session_state.count =0


if st.session_state.count == 0:
    st.session_state.count = 1
    print (st.session_state.count)

def decrement_button():
    decrement_value = 1
    st.session_state.count -= decrement_value
    print ("def"+str(st.session_state.count)) 

def increment_button():
    increment_value = 1
    st.session_state.count += increment_value
    print ("def"+str(st.session_state.count))



default_page = st.empty()
default_input = st.empty()
if input=="":
    with default_page.container():    
        st.write("\n")
        #st.markdown("<h5>هذا الموقع يعرض احاديث الرسول الله صلى الله عليه و سلم\n\n <h5>(محتوى الحديث) مصنفه بالمتن\n\n</h5></h5>", unsafe_allow_html=True)
        #st.markdown("<h5>و الاحاديث جميعها مصحوبه بالراوي و كتابه و رقم الحديث او الصفحه و درجة الصحه</h5>", unsafe_allow_html=True)
        #st.write("\n")
        #st.write("\n")
        #st.markdown("<h5>للبحث</h5>", unsafe_allow_html=True)
        
        definput = st.text_input("للبحث",key="definput")

if definput!="":
    default_page.empty()
    

with st.spinner("جاري التحميل"):
    input=definput
    req = requests.get(f"https://dorar-hadith-api.herokuapp.com/api/search?value={input}&page={st.session_state.count}")
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
        space ="\n"
        st.markdown(f"<p style='text-align:right;'>الحديث: {hadith}</p>", unsafe_allow_html=True)

        align_right = f"<p style='text-align:right;'>الراوي: {rawi}  |المحدث: {mohdith}  |المصدر: {source}</p>"

        st.markdown(align_right,unsafe_allow_html=True)
        st.markdown(f"<p style='text-align:right;'>خلاصة حكم الحديث: {grade}  | الصفحة أو الرقم: {numpage}  </p>",unsafe_allow_html=True)
        st.markdown("<br>",unsafe_allow_html=True)
    if input!="":
        increment_button = st.button("next", on_click=increment_button)
        decrement_button = st.button("previous", on_click=decrement_button)
       



#st.button("next",on_click=button_hadith(),kwargs=dict(increment_value=1))   
#st.markdown(f"<p style='text-align:right;'>< button  onclick = ""  > Search  </ button ></p>",unsafe_allow_html=True)

