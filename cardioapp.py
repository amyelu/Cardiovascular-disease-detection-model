import streamlit as st
import joblib
import numpy as np

# Load the trained model
model = joblib.load("Cardiovascular_detection_model.pkl")

# Streamlit App
st.title("💖 Cardiovascular Disease Prediction App")
st.write("Provide patient details to predict the risk of cardiovascular disease.")

# User Inputs
age = st.number_input("📅 Age (in years)", min_value=1, max_value=120, step=1)

# Dropdowns for categorical features
cholesterol = st.selectbox("🩸 Cholesterol Level", ["Normal", "Above Normal", "Well Above Normal"])
glucose = st.selectbox("🍬 Glucose Level", ["Normal", "Above Normal", "Well Above Normal"])
alcoholic_status = st.selectbox("🍷 Alcohol Consumption", ["Non-Drinker", "Drinker"])
physically_active = st.selectbox("🏃‍♂️ Physical Activity", ["No", "Yes"])

# Numerical Inputs for Blood Pressure
sys_bp = st.number_input("💓 Systolic Blood Pressure (ap_hi)", min_value=50, max_value=250, step=1)
dia_bp = st.number_input("💓 Diastolic Blood Pressure (ap_lo)", min_value=30, max_value=150, step=1)

# --- HEIGHT INPUT ---
height_unit = st.selectbox("📏 Height Unit", ["cm", "feet & inches", "inches"])
if height_unit == "cm":
    height = st.number_input("📏 Height (cm)", min_value=30.0, max_value=250.0, step=0.1)
elif height_unit == "feet & inches":
    feet = st.number_input("👣 Feet", min_value=1, max_value=8, step=1)
    inches = st.number_input("📏 Inches", min_value=0, max_value=11, step=1)
    height = round((feet * 30.48) + (inches * 2.54), 2)  # Convert feet & inches to cm
else:  # Inches only
    inches = st.number_input("📏 Height (inches)", min_value=12.0, max_value=100.0, step=0.1)
    height = round(inches * 2.54, 2)  # Convert inches to cm

# --- WEIGHT INPUT ---
weight_unit = st.selectbox("⚖️ Weight Unit", ["kg", "lbs"])
weight_input = st.number_input(f"⚖️ Weight ({weight_unit})", min_value=30.0, max_value=500.0, step=0.1)

# Convert lbs to kg if needed
if weight_unit == "lbs":
    weight = round(weight_input * 0.453592, 2)  # 1 lb = 0.453592 kg
else:
    weight = weight_input

# BMI Calculation
bmi = round(weight / ((height / 100) ** 2), 2)
st.write(f"📊 **Calculated BMI**: {bmi}")

# Systolic/Diastolic Ratio
sys_dia_ratio = round(sys_bp / dia_bp, 2)
st.write(f"📉 **Systolic/Diastolic Ratio**: {sys_dia_ratio}")

# Blood Pressure Category Assignment
if sys_bp < 120 and dia_bp < 80:
    bp_category = "Normal"
elif 120 <= sys_bp <= 129 and dia_bp < 80:
    bp_category = "Elevated"
elif 130 <= sys_bp <= 139 or 80 <= dia_bp <= 89:
    bp_category = "Hypertension Stage 1"
elif 140 <= sys_bp <= 180 or 90 <= dia_bp <= 120:
    bp_category = "Hypertension Stage 2"
else:
    bp_category = "Hypertensive Crisis"

st.write(f"🩺 **Assigned Blood Pressure Category**: {bp_category}")

# Encoding categorical values
cholesterol_map = {"Normal": 1, "Above Normal": 2, "Well Above Normal": 3}
glucose_map = {"Normal": 1, "Above Normal": 2, "Well Above Normal": 3}
bp_category_map = {"Normal": 4, "Elevated": 0, "Hypertension Stage 1": 2, "Hypertension Stage 2": 3, "Hypertensive Crisis": 1}
alcoholic_status_map = {"Non-Drinker": 0, "Drinker": 1}
physically_active_map = {"No": 0, "Yes": 1}

# Prepare feature array
features = np.array([
    sys_bp, age, cholesterol_map[cholesterol], bmi, weight, bp_category_map[bp_category],
    dia_bp, glucose_map[glucose], physically_active_map[physically_active],
    sys_dia_ratio, height, alcoholic_status_map[alcoholic_status]
]).reshape(1, -1)

# Prediction Button
if st.button("🔮 Predict Cardiovascular Risk"):
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
