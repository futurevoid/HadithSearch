# import base64
# import pathlib
# from urllib import request
import streamlit as st
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


# def img_to_bytes(img_path):
#    img_bytes = pathlib.Path(img_path).read_bytes()
#    encoded = base64.b64encode(img_bytes).decode()
#    return encoded
# font-size: 18px;
# header_html = "<img src='data:image/png;base64,{}' class='img-fluid'>".format(
#    img_to_bytes("hadith.png")
# )from django.http import HttpRequest
# st.markdown(
#    header_html, unsafe_allow_html=True,
# )
# "text-decoration: none !important;"

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


st.markdown(logo, unsafe_allow_html=True)
with st.sidebar.form(key="sideform", clear_on_submit=True):
    input = st.text_input("ابحث عن حديث", key="sideinput")
    subbutton = st.form_submit_button("ابحث")
    sidehide = '''
        <a id=stjava href="javascript:document.getElementsByClassName('css-1rs6os edgvbvh3')[1].click();" target="_self"> 
        <button kind="header" class="butcss"><svg viewBox="0 0 24 24" aria-hidden="true" focusable="false" fill="currentColor" xmlns="http://www.w3.org/2000/svg" color="inherit" class="e1fb0mya1 css-fblp2m ex0cdmw0"><path fill="none" d="M0 0h24v24H0V0z"></path><path d="M19 6.41L17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12 19 6.41z"></path></svg></button>
        </a>
        '''
    sidehidecss = """<style> #stjava, #stjava:hover, #stjava:focus, #stjava:active {
        color: inherit;
        }  
        #sidebut{background: #15d798;
        border: 2px solid #15d798;

        border-radius: 11px;

        padding: 18px 35px;

        color: #ffffff;

        display: inline-block;

        font: normal bold 20px/1 "Open Sans", sans-serif;

        height:30px;
        
        }
        #rstxt{
        font: normal bold 16px/1 "Open Sans", sans-serif;
        position: fixed;
        top: 262px;
        right: 1272px
        
        }
        .butcss{display: inline-flex;
        -moz-box-align: center;
        align-items: center;
        -moz-box-pack: center;
        justify-content: center;
        font-weight: 400;
        border-radius: 0.25rem;
        margin: 0px 0.125rem;
        color: inherit;
        width: auto;
        user-select: none;
        background-color: transparent;
        border: medium none;
        padding: 0.5rem;
        font-size: 14px;
        line-height: 1;
        position: absolute;
        top: -200px;
        right: -30px
        }
        .css-renyox > button:nth-child(1){
            visibility:hidden;
        }
        .css-12oz5g7 > div:nth-child(1) > div:nth-child(1){
           visiblility:hidden; 
        }
        </style>"""
    st.markdown(sidehide, unsafe_allow_html=True)

    st.markdown(sidehidecss, unsafe_allow_html=True)


if subbutton == True:
    st.session_state.clear()


inputstartingout = print(input)
st.markdown(remove_menu_footer, unsafe_allow_html=True)

if "load_state" not in st.session_state:
    st.session_state.load_state = False

if 'count' not in st.session_state:
    st.session_state.count = 0


if st.session_state.count == 0:
    st.session_state.count = 1
    print(st.session_state.count)


def decrement_button():
    decrement_value = 1
    st.session_state.count -= decrement_value


def increment_button():
    increment_value = 1
    st.session_state.count += increment_value


default_page = st.empty()
if input == "":
    with default_page.container():
        st.write("\n")
        st.write("\n")
        st.markdown(content, unsafe_allow_html=True)
        with st.form(key="defform"):
            input = st.text_input("ابحث عن حديث", key="definput")
            st.form_submit_button("ابحث")


if input != "":
    default_page.empty()
    with st.spinner("جاري التحميل"):
        req = requests.get(
            f"https://dorar-hadith-api.cyclic.app/api/search?value={input}&page={st.session_state.count}")

        data = req.json()
        data_len = len(data)

        for number in range(data_len):
            hadith_uncleaned = data[number]["hadith"]
            hadith = hadith_uncleaned.replace(".", "")
            source = data[number]["source"]
            rawi = data[number]["el_rawi"]
            mohdith = data[number]["el_mohdith"]
            numpage = data[number]["number_or_page"]
            grade = data[number]["grade"]
            space = "\n"
            st.markdown(
                f"<p style='text-align:right;'>الحديث: {hadith}</p>", unsafe_allow_html=True)

            align_right = f"<p style='text-align:right;'>الراوي: {rawi}  |المحدث: {mohdith}  |المصدر: {source}</p>"

            st.markdown(align_right, unsafe_allow_html=True)
            st.markdown(
                f"<p style='text-align:right;'>خلاصة حكم الحديث: {grade}  | الصفحة أو الرقم: {numpage}  </p>", unsafe_allow_html=True)
            st.markdown("<br>", unsafe_allow_html=True)
        if input != "":
            increment_button = st.button("next", on_click=increment_button)
            decrement_button = st.button("previous", on_click=decrement_button)