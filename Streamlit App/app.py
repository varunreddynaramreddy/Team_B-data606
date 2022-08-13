import streamlit as st
from streamlit_option_menu import option_menu

## Loading View
from call_plan_prediction import *
from recommendation_drivers import *
from about import *


import pandas as pd

st.set_page_config(layout="wide")

data = pd.read_csv('..\\data\\bank-full.csv', sep = ';')

def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("style.css")



st.markdown('<div style = "background-color: black; text-align: center;"> <h3 style = "color: white; padding: 5px;"> Customer Term Insurance Purchase Propensity Prediction </h3> </div>', unsafe_allow_html=True)

with st.container():
    selected = option_menu(None, ["About", "Data Summary", "Plan Calls - Predict Customer's Propensity"], 
        icons=['patch-question-fill', 'bar-chart-line', "graph-up-arrow"], 
        menu_icon="cast", default_index=0, orientation="horizontal",
        styles={
        "container": {"margin": "0px"}})


if selected == "Plan Calls - Predict Customer's Propensity":
    with st.spinner('Wait for it...'):
        load_plan_view_content(data, st)
    
elif selected == "Data Summary":
    with st.spinner('Wait for it...'):
        load_reco_driver(st)
else:
    with st.spinner('Wait for it...'):
        load_about(st)


def main():
    return None


if __name__ == '__main__':
    main()