import streamlit as st
import joblib
import numpy as np

# Load trained model
model = joblib.load("models/fraud_model.pkl")

st.set_page_config(page_title="Credit Card Fraud Detection", layout="centered")

st.title("💳 Credit Card Fraud Detection")
st.write("Enter transaction details to predict fraud")

# -------- INPUTS -------- #

# Time feature (seconds since first transaction)
time = st.number_input(
    "Transaction Time (seconds since first transaction)",
    min_value=0.0,
    value=0.0
)

# PCA Features V1–V28
st.subheader("PCA Features (V1 to V28)")
v_features = []
for i in range(1, 29):
    v_features.append(
        st.number_input(f"V{i}", value=0.0)
    )

# Amount
amount = st.number_input(
    "Transaction Amount",
    min_value=0.0,
    value=0.0
)

# -------- PREDICTION -------- #

if st.button("Predict Fraud"):
    # IMPORTANT: Order must match training
    # [Time, V1, V2, ..., V28, Amount]
    input_data = np.array([[time] + v_features + [amount]])

    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.error("🚨 Fraudulent Transaction Detected")
    else:
        st.success("✅ Legitimate Transaction")