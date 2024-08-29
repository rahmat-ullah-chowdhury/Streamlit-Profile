from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title = "My Webpage", page_icon =":tada:", layout = "wide")
def lottieurl(url):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()
lottie_coding =lottieurl("https://lottie.host/f6799b07-1fe7-409e-b170-d84874a333b7/GhwxLEe9NJ.json")
image_1 = image_1 = Image.open("C:\\Users\\Rahat Chowdhury\\Desktop\\app\\images\\46.jpg")

image_2 = Image.open("C:\\Users\\Rahat Chowdhury\\Desktop\\app\\images\\48.jpg")

#HEADER SECTION
with st.container():
   st.subheader("HI THIS IS MY FIRST TRY :wave:")
   st.title("A DATA ANALYST FROM BANGLADESH")
   st.write("I AM TRYING TO BE A GOOD DEVELOPER ")
   st.write("Rahat is the best ")
   st.write("[learn more>](https://www.google.com/)")
   
#what I do
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
      st.header("What I Do")
      st.write("##")
      st.write('''
               There's no need to spend days or weeks building a website anymore. In this video, I'm going to show you how to build a website with a blog and a contact page in only 12 minutes using Python, Streamlit and other open-source tools.''')
      st.write("[Youtube Link>](https://www.youtube.com/watch?v=VqgUkExPvLY)")
    with right_column:
        st_lottie(lottie_coding, height=300,key ="coding")
        
with st.container():
    st.write("---")
    st.write("My Projects")
    st.write("##")
    image_column,text_column = st.columns((1,2))
    with image_column:
        st.image(image_1)
        
    with text_column:
        st.subheader("Intregate lottie Animations inside your Stremlit App")
        st.write(
            '''This tutorial is shorter than others but rich with information! I'm just getting started with Python as a language, only knowing the basics, but this is getting me excited to learn and do more. Thanks, Rahat!!!!'''
        )
        st.markdown("[Watch Video>](https://www.youtube.com/watch?v=VqgUkExPvLY)")
with st.container():
    image_column,text_column = st.columns((1,2))
    
    with image_column:
        st.image(image_2)
    with text_column:
     st.subheader("How is the Walpaper")
     st.write(
            ''' Thank You!!!!'''
        )
     st.markdown("[Watch Video>](https://www.youtube.com/watch?v=VqgUkExPvLY)")
           
