import streamlit as st
import joblib
import numpy as np

# Load the trained model
model = joblib.load("Cardiovascular_detection_model.pkl")

# Streamlit App
st.title("💖 Cardiovascular Disease Prediction App")
st.write("Provide patient details to predict the risk of cardiovascular disease.")

# --- USER INPUTS ---

# Age
age = st.number_input("📅 Age (in years)", min_value=1, max_value=120, step=1)

# Dropdowns for categorical features
cholesterol = st.selectbox("🩸 Cholesterol Level", ["Normal", "Above Normal", "Well Above Normal"])
glucose_level = st.selectbox("🍬 Glucose Level", ["Normal", "Above Normal", "Well Above Normal"])
Alcoholic_status = st.selectbox("🍷 Alcohol Consumption", ["Non-Drinker", "Drinker"])
Physically_Active = st.selectbox("🏃‍♂️ Physical Activity", ["No", "Yes"])

# Blood Pressure Inputs
ap_hi = st.number_input("💓 Systolic Blood Pressure (ap_hi)", min_value=50, max_value=250, step=1)
ap_lo = st.number_input("💓 Diastolic Blood Pressure (ap_lo)", min_value=30, max_value=150, step=1)

# --- HEIGHT INPUT ---
height_unit = st.selectbox("📏 Height Unit", ["cm", "feet & inches", "inches"])
if height_unit == "cm":
    height_cm = st.number_input("📏 Height (cm)", min_value=30.0, max_value=250.0, step=0.1)
elif height_unit == "feet & inches":
    feet = st.number_input("👣 Feet", min_value=1, max_value=8, step=1)
    inches = st.number_input("📏 Inches", min_value=0, max_value=11, step=1)
    height_cm = round((feet * 30.48) + (inches * 2.54), 2)  # Convert feet & inches to cm
else:  # Inches only
    inches = st.number_input("📏 Height (inches)", min_value=12.0, max_value=100.0, step=0.1)
    height_cm = round(inches * 2.54, 2)  # Convert inches to cm

# --- WEIGHT INPUT ---
weight_unit = st.selectbox("⚖️ Weight Unit", ["kg", "lbs"])
weight_input = st.number_input(f"⚖️ Weight ({weight_unit})", min_value=30.0, max_value=500.0, step=0.1)

# Convert lbs to kg if needed
if weight_unit == "lbs":
    weight_kg = round(weight_input * 0.453592, 2)  # Convert lbs to kg
else:
    weight_kg = weight_input

# --- BMI CALCULATION ---
BMI = round(weight_kg / ((height_cm / 100) ** 2), 2)
st.write(f"📊 **Calculated BMI**: {BMI}")

# --- SYSTOLIC/DIASTOLIC RATIO ---
sys_dsys_ratio = round(ap_hi / ap_lo, 2)
st.write(f"📉 **Systolic/Diastolic Ratio**: {sys_dsys_ratio}")

# --- BLOOD PRESSURE CATEGORY ASSIGNMENT ---
if ap_hi < 120 and ap_lo < 80:
    Bp_category = "Normal"
elif 120 <= ap_hi <= 129 and ap_lo < 80:
    Bp_category = "Elevated"
elif 130 <= ap_hi <= 139 or 80 <= ap_lo <= 89:
    Bp_category = "Hypertension Stage 1"
elif 140 <= ap_hi <= 180 or 90 <= ap_lo <= 120:
    Bp_category = "Hypertension Stage 2"
else:
    Bp_category = "Hypertensive Crisis"

st.write(f"🩺 **Assigned Blood Pressure Category**: {Bp_category}")

# --- FEATURE ENCODING ---
cholesterol_map = {"Normal": 1, "Above Normal": 2, "Well Above Normal": 3}
glucose_map = {"Normal": 1, "Above Normal": 2, "Well Above Normal": 3}
Bp_category_map = {"Normal": 4, "Elevated": 0, "Hypertension Stage 1": 2, "Hypertension Stage 2": 3, "Hypertensive Crisis": 1}
Alcoholic_status_map = {"Non-Drinker": 0, "Drinker": 1}
Physically_Active_map = {"No": 0, "Yes": 1}

# --- FEATURE ARRAY (ORDER MATCHES MODEL TRAINING) ---
features = np.array([
    ap_hi, ap_lo, age, Physically_Active_map[Physically_Active], 
    Alcoholic_status_map[Alcoholic_status], Bp_category_map[Bp_category], 
    cholesterol_map[cholesterol], BMI, weight_kg, glucose_map[glucose_level], 
    sys_dsys_ratio, height_cm
]).reshape(1, -1)

# --- PREDICTION ---
if st.button("Predict Cardiovascular Risk"):
    prediction_prob = model.predict_proba(features)[0][1]

    # Convert probability into a readable label
    if prediction_prob > 0.7:
        result = "⚠️ High Risk of Cardiovascular Disease"
    elif prediction_prob > 0.4:
        result = "⚠️ Moderate Risk of Cardiovascular Disease"
    else:
        result = "✅ Low Risk of Cardiovascular Disease"

    st.success(f"**Prediction: {result}**")
    st.write(f"🧬 **Probability of Cardiovascular Disease**: {prediction_prob:.2f}")
