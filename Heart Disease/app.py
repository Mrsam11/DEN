import streamlit as st
import pandas as pd
import numpy as np
import joblib

model = joblib.load('random_forest_model.pkl')

# Streamlit UI
st.title("Heart Disease Prediction")

# Input fields for the selected features
Age = st.number_input("Age", min_value=0)
Cholesterol = st.number_input("Cholesterol", min_value=0)
Heart_Rate = st.number_input("Heart Rate", min_value=0)
Alcohol_Intake_Moderate = st.selectbox("Alcohol Intake (Moderate)", ["No", "Yes"])
Stress_Level = st.number_input("Stress Level", min_value=0)
chest_pain_typical_angina = st.selectbox("Chest Pain Type (Typical Angina)", ["No", "Yes"])

#converting to binary values
Alcohol_Intake_Moderate = 1 if Alcohol_Intake_Moderate == "Yes" else 0
chest_pain_typical_angina = 1 if chest_pain_typical_angina == "Yes" else 0

# Prediction button
if st.button("Predict"):
    input_data = np.array([[Age, Cholesterol, Heart_Rate,
                            Alcohol_Intake_Moderate, Stress_Level,
                            chest_pain_typical_angina]])
    
    # Predict
    prediction = model.predict(input_data)
    prediction_proba = model.predict_proba(input_data)

    # Display results
    if prediction[0] == 1:
        st.success("The model predicts: **Heart Disease Present**")
    else:
        st.success("The model predicts: **No Heart Disease**")

    st.write("Prediction Probability (Heart Disease): {:.2f}%".format(prediction_proba[0][1] * 100))
    st.write("Prediction Probability (No Heart Disease): {:.2f}%".format(prediction_proba[0][0] * 100))
