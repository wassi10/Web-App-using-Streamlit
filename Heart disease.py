# -*- coding: utf-8 -*-
"""
Created on Sun May 22 11:53:51 2022

@author: siddhardhan
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# loading the saved models

rf_model = pickle.load(open("D:\Research\pppppp\MLP_heart_disease_model.sav", "rb"))

heart_disease_model = pickle.load(open("D:\Research\pppppp\MLP_heart_disease_model.sav","rb"))




# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Heart Disease Prediction System',
                          
                          ['RF-HeartAttackDataset',
                           'MLP-PublicHealthDataset'],
                          icons=['activity','heart'],
                          default_index=0)
    
    
# Diabetes Prediction Page
if (selected == 'RF-HeartAttackDataset'):
    
    # page title
    st.title('Heart Disease Prediction using Random Forest')
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.number_input("Age", min_value=0, max_value=120)
        
    with col2:
        sex = st.selectbox("Sex", [0, 1])
        
    with col3:
        cp = st.selectbox("Chest Pain Type (Cp)", [0, 1, 2, 3])
        
    with col1:
        trestbps = st.number_input("Resting Blood Pressure (mm Hg) - (trestbps)", min_value=0)
        
    with col2:
        chol = st.number_input("Cholesterol (mg/dl) - (chol)", min_value=0)
        
    with col3:
        fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl (fbs)", [0, 1])
        
    with col1:
        restecg = st.selectbox("Resting Electrocardiographic Results (restecg)", [0, 1, 2])
        
    with col2:
        thalach = st.number_input("Maximum Heart Rate Achieved (thalach)", min_value=0)
        
    with col3:
        exang = st.selectbox("Exercise-Induced Angina (exang)", [0, 1])
        
    with col1:
        oldpeak = st.number_input("ST Depression Induced by Exercise Relative to Rest (oldpeak)", min_value=0.0)
        
    with col2:
        slope = st.selectbox("Slope of the Peak Exercise ST Segment (slope)", [0, 1, 2])
        
    with col3:
        ca = st.number_input("Number of Major Vessels (ca)", min_value=0)
        
    with col1:
        thal = st.selectbox("Thalassemia Type (thal)", [0, 1, 2, 3])
    
    
    # code for Prediction
    diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button("Predict"):
        # Check for non-numeric input
        if (not isinstance(age, (int, float)) or not isinstance(sex, int) or not isinstance(cp, int)
            or not isinstance(trestbps, (int, float)) or not isinstance(chol, (int, float))
            or not isinstance(fbs, int) or not isinstance(restecg, int) or not isinstance(thalach, (int, float))
            or not isinstance(exang, int) or not isinstance(oldpeak, (int, float)) or not isinstance(slope, int)
            or not isinstance(ca, (int, float)) or not isinstance(thal, int)):
            st.error("Invalid input data. Please enter numeric values.")
        else:
            heart_prediction = rf_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])                          
        
            if (heart_prediction[0] == 1):
                diagnosis = 'The person is having heart disease'
            else:
                diagnosis = 'The person does not have any heart disease'
        
    st.success(diagnosis)




# Heart Disease Prediction Page
if (selected == 'MLP-PublicHealthDataset'):
    
    # page title
    st.title('Heart Disease Prediction using MLP')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age1 = st.number_input("Age", min_value=0, max_value=120)
        
    with col2:
        sex1 = st.selectbox("Sex", [0, 1])
        
    with col3:
        cp1 = st.selectbox("Chest Pain Type (Cp)", [0, 1, 2, 3])
        
    with col1:
        trestbps1 = st.number_input("Resting Blood Pressure (mm Hg) - (trestbps)", min_value=0)
        
    with col2:
        chol1 = st.number_input("Cholesterol (mg/dl) - (chol)", min_value=0)
        
    with col3:
        fbs1 = st.selectbox("Fasting Blood Sugar > 120 mg/dl (fbs)", [0, 1])
        
    with col1:
        restecg1 = st.selectbox("Resting Electrocardiographic Results (restecg)", [0, 1, 2])
        
    with col2:
        thalach1 = st.number_input("Maximum Heart Rate Achieved (thalach)", min_value=0)
        
    with col3:
        exang1 = st.selectbox("Exercise-Induced Angina (exang)", [0, 1])
        
    with col1:
        oldpeak1 = st.number_input("ST Depression Induced by Exercise Relative to Rest (oldpeak)", min_value=0.0)
        
    with col2:
        slope1 = st.selectbox("Slope of the Peak Exercise ST Segment (slope)", [0, 1, 2])
        
    with col3:
        ca1 = st.number_input("Number of Major Vessels (ca)", min_value=0)
        
    with col1:
        thal1 = st.selectbox("Thalassemia Type (thal)", [0, 1, 2, 3])
        
        
     
     
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button("Predict"):
        # Check for non-numeric input
        if (not isinstance(age1, (int, float)) or not isinstance(sex1, int) or not isinstance(cp1, int)
            or not isinstance(trestbps1, (int, float)) or not isinstance(chol1, (int, float))
            or not isinstance(fbs1, int) or not isinstance(restecg1, int) or not isinstance(thalach1, (int, float))
            or not isinstance(exang1, int) or not isinstance(oldpeak1, (int, float)) or not isinstance(slope1, int)
            or not isinstance(ca1, (int, float)) or not isinstance(thal1, int)):
            st.error("Invalid input data. Please enter numeric values.")
        else:
            heart_prediction1 = heart_disease_model.predict([[age1, sex1, cp1, trestbps1, chol1, fbs1, restecg1,thalach1,exang1,oldpeak1,slope1,ca1,thal1]])                          
        
            if (heart_prediction1[0] == 1):
                heart_diagnosis = 'The person is having heart disease'
            else:
                heart_diagnosis = 'The person does not have any heart disease'
        
    st.success(heart_diagnosis)
        
    
    




