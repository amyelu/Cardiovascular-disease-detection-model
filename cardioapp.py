import streamlit as st
import joblib
import numpy as np

# Load the trained model
model = joblib.load("Cardiovascular_detection_model.pkl")

# Streamlit App
st.title("Cardiovascular Disease Prediction App")

# Input form
st.write("Enter patient details to predict the risk of cardiovascular disease:")
features = []
age = st.number_input("Age", min_value=0, max_value=120, step=1)
gender = st.selectbox("Gender", ["Male", "Female"])
bp = st.number_input("Blood Pressure", min_value=50, max_value=200, step=1)
cholesterol = st.number_input("Cholesterol Level", min_value=100, max_value=500, step=1)

# Convert input into features array
features.append(age)
features.append(1 if gender == "Male" else 0)  # Encode gender as 1 for Male, 0 for Female
features.append(bp)
features.append(cholesterol)

# Prediction button
if st.button("Predict"):
    features_array = np.array(features).reshape(1, -1)
    prediction_prob = model.predict_proba(features_array)[0][1]

    # Convert probability into a readable label
    if prediction_prob > 0.7:
        result = "High chance of Cardiovascular disease"
    elif prediction_prob > 0.4:
        result = "Moderate chance of Cardiovascular disease"
    else:
        result = "Low chance of Cardiovascular disease"

    st.success(f"Prediction: {result}")
    st.write(f"Probability: {prediction_prob:.2f}")
