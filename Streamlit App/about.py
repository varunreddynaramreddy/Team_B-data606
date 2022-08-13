#import streamlit as st
from PIL import Image

def load_about(st):
    col1, col2 = st.columns([1, 1])

    col1.markdown('''
    <ul>
        <li> <b><span style = "font-size: x-large;">M</span></b>arketing is a great tool for most of the businesses for boosting sales. It is an important function in any business as production and distribution largely depend on marketing success </li>
        <li> With the growth of technology and digital marketing, traditional marketing channels like direct telemarketing etc., are failing to capture business attention
            <ul>
            <li>One the major reason for this is the swift change in business operations as well as customer needs</li>
            </ul> 
        </li>
        <li> Advent of Covid in 2020 is demanding more returns from marketing activities with limited or reduced budget across businesses
            <ul><li> Data driven campaign management is the only option for business under these circumstances for Optimizing revenue generated from marketing campaigns</li></ul>
        
    </ul>
    ''', unsafe_allow_html=True)

    image = Image.open('About.png')
    col2.image(image)

    st.info('''

    This tool enables agents to maximized their performace by enabling them with call prioritization based on customer's term-deposit subscription propability

    ''')
