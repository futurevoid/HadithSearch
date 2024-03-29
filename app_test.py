#import base64
#import pathlib
from re import sub
import streamlit as st
from streamlit.components.v1 import html
import requests
from math import *

st.set_page_config(
         page_title="احاديث الدرر السنيه",
     page_icon="📖",
     initial_sidebar_state="collapsed",
 )



remove_menu_footer = """
<style>
#MainMenu {visibility: hidden;}
footer { visibility:hidden; }
</style>
"""

#def img_to_bytes(img_path):
#    img_bytes = pathlib.Path(img_path).read_bytes()
#    encoded = base64.b64encode(img_bytes).decode()
#    return encoded
#font-size: 18px;
#header_html = "<img src='data:image/png;base64,{}' class='img-fluid'>".format(
#    img_to_bytes("hadith.png")
#)
#st.markdown(
#    header_html, unsafe_allow_html=True,
#)

st.markdown(
     """
     <style>
     [data-testid="stSidebar"][aria-expanded="true"] > div:first-child {
         width: 300px;
       }
        </style>
        """,
        unsafe_allow_html=True)

title = """
<p align=right style=vertical-align: top;>احاديث الرسول ﷺ من الدرر السنيه</p>
"""
#st.markdown(title,unsafe_allow_html=True)

content = """<style>
@import url(https://fonts.googleapis.com/earlyaccess/amiri.css);


#container {
    position: relative;
    text-align: right;
    letter-spacing: -1.6px;
}
#intro{
    float:right;
    line-height: 90px;
    
}
h1{
    font-family: 'amiri', serif;
}
</style>
<html>
<div id="container">
<div id="intro" >  <h1>هذا الموقع يعرض أحاديث رسول الله  ﷺ<br>(محتوى الحديث)مصنفه بالمتن<br>و الأحاديث جميعها مصحوبه<br> بالراوي و المحدث و كتابه و رقم<br> الحديث او الصفحه و درجة الصحة</h1></div>
</div>
</html>"""

logo = """
<style>
#container {
    position: relative;
    text-align: right;
    letter-spacing: -1.6px;
    
}

#content{
    position: fixed;
    top:20px;
    right:25px
}

html body div#root div div.withScreencast div div.stApp.css-ffhzg2.eczokvf1 header.css-hy8qiv.e8zbici2{
    visibility:hidden;

}
.css-1avcm0n{
    visibility:hidden;
   
}
#root > div:nth-child(1) > div.withScreencast > div > div > header{
    visibility:hidden;
}
 a, a:hover, a:focus, a:active , a:link , a:visited {
      text-decoration: none !important;
      color: inherit;
 }
</style>
<html>
<div id="container">
<div id=content><a target="_self" href=>حديث  سيرش <br> hadith search</a></div>
</div>
</html>"""


st.markdown(logo,unsafe_allow_html=True)
with st.sidebar.form(key="sideform",clear_on_submit=True):
        input = st.text_input("ابحث عن حديث",key="sideinput")
        subbutton = st.form_submit_button("ابحث")
        sidehide = """
    <!DOCTYPE html>
    <html>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
    .css-wq85zr{
        javascript:document.getElementsByClassName('css-1rs6os edgvbvh3')[1].click();
    }</style>
    </html>"""
        st.markdown(sidehide,unsafe_allow_html=True)

if subbutton == True:
    st.session_state.clear()
    js = """
    document.getElementsByClassName('css-1rs6os edgvbvh3')[1].click();
    """
    mhtml = f'''
    <script>{js}</script>
    '''
    #html(mhtml)



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
        st.write("\n")
        st.markdown(content,unsafe_allow_html=True)
        #definput = st.text_input("",key="definput")
        with st.form(key="defform"):
            input = st.text_input("ابحث عن حديث",key="definput")
            st.form_submit_button("ابحث")
                    

if input!="":
    default_page.empty()
    

with st.spinner("جاري التحميل"):
    #input=definput
    req = requests.get(f"https://dorar-hadith-api.herokuapp.com/api/hadith/search?value={input}&page={st.session_state.count}")

    res = req.json()
    data = res["data"]

    data_len = len(data)

    for i in range(data_len):
        number = i

        hadith_uncleaned = data[number]["hadith"]
        hadith = hadith_uncleaned.replace(".", "")
        book = data[number]["book"]
        rawi = data[number]["rawi"]
        mohdith = data[number]["mohdith"]
        numpage = data[number]["numberOrPage"]
        grade = data[number]["grade"]
        space ="\n"
        st.markdown(f"<p style='text-align:right;'>الحديث: {hadith}</p>", unsafe_allow_html=True)

        align_right = f"<p style='text-align:right;'>الراوي: {rawi}  |المحدث: {mohdith}  |الكتاب: {book}</p>"

        st.markdown(align_right,unsafe_allow_html=True)
        st.markdown(f"<p style='text-align:right;'>خلاصة حكم المحدث: {grade}  | الصفحة أو الرقم: {numpage}  </p>",unsafe_allow_html=True)
        st.markdown("<br>",unsafe_allow_html=True)
    if input!="":
        increment_button = st.button("next", on_click=increment_button)
        decrement_button = st.button("previous", on_click=decrement_button)
       



#st.button("next",on_click=button_hadith(),kwargs=dict(increment_value=1))   
#st.markdown(f"<p style='text-align:right;'>< button  onclick = ""  > Search  </ button ></p>",unsafe_allow_html=True)

