import streamlit as st
import numpy as np
import pandas as pd  
import joblib

# Load the trained model (this includes the pipeline with preprocessing)
model = joblib.load('tuned_model.pkl')

# Streamlit UI
st.title("Heart Disease Prediction")

# Input fields for the selected features
Age = st.number_input("Age", min_value=0)
Cholesterol = st.number_input("Cholesterol", min_value=0)
Heart_Rate = st.number_input("Heart Rate", min_value=0)
Blood_Pressure = st.number_input("Blood Pressure", min_value=0)
Stress_Level = st.number_input("Stress Level", min_value=0)
Blood_Sugar = st.number_input("Blood Sugar", min_value=0)

# Categorical Inputs
Smoking = st.selectbox("Smoking", ["Never", "Current", "Former"])
Chest_Pain_Type = st.selectbox("Chest Pain Type", ["Typical Angina", "Atypical Angina", "Non-anginal Pain", "Asymptomatic"])
Alcohol_Intake = st.selectbox("Alcohol Intake", ["None", "Moderate", "Heavy"])

# Prepare input data for prediction
input_data = np.array([[Age, Cholesterol, Heart_Rate, Blood_Pressure, Stress_Level, Blood_Sugar,
                        Smoking, Chest_Pain_Type, Alcohol_Intake]])

# Define column names for the input data
columns = ['Age', 'Cholesterol', 'Heart_Rate', 'Blood_Pressure', 'Stress_Level', 'Blood_Sugar',
           'Smoking', 'Chest_Pain_Type', 'Alcohol_Intake']

# Convert input_data to a pandas DataFrame
input_df = pd.DataFrame(input_data, columns=columns)

# Prediction button
if st.button("Predict"):
    try:
        prediction = model.predict(input_df)
        prediction_proba = model.predict_proba(input_df)

        # Display results
        if prediction[0] == 1:
            st.success("The model predicts: **Heart Disease Present**")
        else:
            st.success("The model predicts: **No Heart Disease**")

        st.write("Positive Probability (Heart Disease):", prediction_proba[0][1])
        st.write("Negative Probability (No Heart Disease):", prediction_proba[0][0])

    except Exception as e:
        st.error(f"Error during prediction: {e}")
