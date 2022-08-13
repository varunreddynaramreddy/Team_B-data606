#import streamlit as st
from PIL import Image
import codecs

def load_reco_driver(st):
    file = codecs.open("Telemarketing_Prediction.html", "r", "utf-8")

    st.components.v1.html(file.read(), height = 500, scrolling=True) 
    
   # st.markdown('''<iframe src='Telemarketing Prediction.html' style='width: 00px;height: 200px'> </iframe>''', unsafe_allow_html=True)