#import streamlit as st
import pickle
import pandas as pd
import sklearn
import numpy as np
import lime
import lime.lime_tabular
from PIL import Image
import xgboost



modelLocation = '../models/adaboost_w_oversampling.sav'
data = pd.read_csv('..\\data\\bank-full.csv', sep = ';')

def get_predictions(data1, mdLoc, colName1, modelData, st):
    ## Loading saved model
    filename = mdLoc
    model = pickle.load(open(filename, 'rb'))
    dataCopy = pd.DataFrame(data1)
    dataCopy = pd.get_dummies(dataCopy)
   

    ## Data prep for model prediction
    missingFeatures = list(set(list(model.feature_names_in_)) - set(list(pd.get_dummies(dataCopy).columns)))

    ## Adding missing fields for prediction
    for i in missingFeatures:
        dataCopy[i] = 0

    #colName.write(model.best_estimator_.predict(dataCopy))
    colName1.markdown('<h4> Parameters Selected </h4>', unsafe_allow_html=True)
    colName1.dataframe(pd.DataFrame(data1))
    colName1.markdown('<h4> Recommendations </h4>', unsafe_allow_html=True)

    if model.best_estimator_.predict(dataCopy[list(model.feature_names_in_)]) == 1:
        image = Image.open('Success.png')
        colName1.image(image)
    else:
        image = Image.open('Fail.png')
        colName1.image(image)


    ## LIME Explaination

    predict_fn_xgb = lambda x: model.best_estimator_.predict_proba(x).astype(float)
    feature_names = list(model.best_estimator_.feature_names_in_)

    explainer = lime.lime_tabular.LimeTabularExplainer(np.array(pd.get_dummies(modelData)[feature_names]), feature_names=feature_names, class_names=['No', 'Yes'])
    exp = explainer.explain_instance(dataCopy[feature_names].iloc[0], predict_fn_xgb, num_features=15)


    ## Features Driving Recommendation

    colName1.markdown('<h7> Features Driving Recommendation (Should we Target Customer?) </h7>', unsafe_allow_html=True)
    with colName1:
        st.components.v1.html(exp.as_html())    

    return None

def load_plan_view_content(data, st):
    with st.form(key="form"):
        # sideCol1, sideCol2 = st.sidebar.columns(2)
        col1, col2 = st.columns([1, 3])

        # Sidebar Feature Selection

        ## Job
        job = col1.selectbox("Job", set(data['job']))
        ## Marital
        marital = col1.selectbox("Martial Status", set(data['marital']))
        ## education
        day = col1.selectbox("Day", set(data['day']))
        ## education
        education = col1.selectbox("Education", set(data['education']))
        ## poutcome
        poutcome = col1.selectbox("Poutcome", set(data['poutcome']))
         ## poutcome
        contact = col1.selectbox("Contact", set(data['contact']))
         ## campaign
        campaign = col1.selectbox("Campaign", set(data['campaign']))
        ## previous
        previous = col1.selectbox("Previous", set(data['previous']))
        ## Balance
        balance = int(col1.text_input("Account Balance (in $)", 1000))
        ## Duration
        duration = int(col1.text_input("Select Call Duration (in Sec)", 60))
        ## pdays
        pdays = int(col1.text_input("dpays?", 10))
        ## Housing
        housing = col1.radio("Has Own House?", set(data['housing']),  horizontal=True)
        ## Loan
        loan = col1.radio("Has Existing Loan?", set(data['loan']),  horizontal=True)
        ## default
        default = col1.radio( "Loan Default?", set(data['default']),  horizontal=True)
        ## Age
        age = col1.slider('Age', 0, 100, 25)

        inputObj = [{'job': job, 'marital': marital, 'day': day, 'poutcome': poutcome, 'campaign': campaign, 'previous': previous, 'contact':contact, 'education':education, 'balance': balance, 'duration': duration, 'pdays': pdays, 'housing': housing, 'loan': loan, 'default': default, 'age': age}]

        #col3, col4 = col2.columns([3, 1])

        #predictionValue = col2.button("Get Recommendation", on_click=get_predictions(inputObj, modelLocation, col2))

        col2.form_submit_button("Get Recommendation", on_click=get_predictions(inputObj, modelLocation, col2, data, st))

        ##col2.write(predictionValue)

