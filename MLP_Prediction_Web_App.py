# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 21:57:59 2023

@author: Khadiza
"""

import numpy as np
import pickle
import streamlit as st


# loading the saved model
loaded_model = pickle.load(open("D:\Research\WEB-Based\WEB App\MLP_heart_disease_model.sav", "rb"))


# creating a function for Prediction

def heart_prediction(input_data):
    

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      return 'The person dose not has Heart Disease'
    else:
      return 'The person has Heart Disease'
  
    
  
# Define your Streamlit app
def main():
    st.title("Heart Disease Prediction Web App")

     # Collect user input using Streamlit widgets
    age = st.number_input("Age", min_value=0, max_value=120)
    
    sex = st.selectbox("Sex", [0, 1])
    
    cp = st.selectbox("Chest Pain Type (Cp)", [0, 1, 2, 3])
    
    trestbps = st.number_input("Resting Blood Pressure (mm Hg) - (trestbps)", min_value=0)
    
    chol = st.number_input("Cholesterol (mg/dl) - (chol)", min_value=0)
    
    fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl (fbs)", [0, 1])
    
    restecg = st.selectbox("Resting Electrocardiographic Results (restecg)", [0, 1, 2])
    
    thalach = st.number_input("Maximum Heart Rate Achieved (thalach)", min_value=0)
    
    exang = st.selectbox("Exercise-Induced Angina (exang)", [0, 1])
    
    oldpeak = st.number_input("ST Depression Induced by Exercise Relative to Rest (oldpeak)", min_value=0.0)
    
    slope = st.selectbox("Slope of the Peak Exercise ST Segment (slope)", [0, 1, 2])
    
    ca = st.number_input("Number of Major Vessels (ca)", min_value=0)
    
    thal = st.selectbox("Thalassemia Type (thal)", [0, 1, 2, 3])
    
    
    
    diagnosis = ''
   
    
   
    # Add a submit button
    if st.button("Predict"):
        # Check for non-numeric input
        if (not isinstance(age, (int, float)) or not isinstance(sex, int) or not isinstance(cp, int)
            or not isinstance(trestbps, (int, float)) or not isinstance(chol, (int, float))
            or not isinstance(fbs, int) or not isinstance(restecg, int) or not isinstance(thalach, (int, float))
            or not isinstance(exang, int) or not isinstance(oldpeak, (int, float)) or not isinstance(slope, int)
            or not isinstance(ca, (int, float)) or not isinstance(thal, int)):
            st.error("Invalid input data. Please enter numeric values.")
        else:
            # Continue with your model prediction
            diagnosis = heart_prediction([age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal])


       
    st.success(diagnosis)
    
    
    
if __name__ == '__main__':
    main()