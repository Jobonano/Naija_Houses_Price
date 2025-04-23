import streamlit as st
import pandas as pd
import numpy as np
import xgboost as xgb
import joblib

# Load trained model (assume saved as model.pkl)
model = joblib.load("model.pkl")
# Load the feature column names
#columns = joblib.load("columns.pkl")

# Title
st.title("🏠 Nigeria House Price Predictor")

# Inputs
bedrooms = st.number_input("Bedrooms", 1, 10, 3)
bathrooms = st.number_input("Bathrooms", 1, 10, 2)
toilets = st.number_input("Toilets", 1, 10, 3)
parking = st.number_input("Parking Space", 0, 10, 1)
title = st.selectbox("Title", ['Detached Duplex', 'Semi Detached Duplex', 'Block of Flats', 'Terraced Duplexes'])
town = st.selectbox("Town", ['Lekki', 'Ajah', 'Katampe', 'Mabushi', 'Victoria Island (VI)', ...])  # Fill in real towns
state = st.selectbox("State", ['Lagos', 'Abuja', 'Ogun', 'Oyo', 'Rivers', ...])  # Fill in real states

# Feature Engineering
bed_bath_ratio = bedrooms / (bathrooms + 1e-5)
bath_toilet_ratio = bathrooms / (toilets + 1e-5)
room_total = bedrooms + bathrooms + toilets
parking_per_room = parking / (room_total + 1e-5)

# Construct dataframe
input_dict = {
    "bedrooms": bedrooms,
    "bathrooms": bathrooms,
    "toilets": toilets,
    "parking_space": parking,
    "bed_bath_ratio": bed_bath_ratio,
    "bath_toilet_ratio": bath_toilet_ratio,
    "room_total": room_total,
    "parking_per_room": parking_per_room,
    f"title_{title}": 1,
    f"town_{town}": 1,
    f"state_{state}": 1,
}
# Fill missing columns with 0
all_columns = joblib.load("columns.pkl")  # Saved column list from training
for col in all_columns:
    input_dict.setdefault(col, 0)

df_input = pd.DataFrame([input_dict])[all_columns]

# Predict
if st.button("Predict Price"):
    log_price = model.predict(df_input)[0]
    predicted_price = np.expm1(log_price)
    st.success(f"Estimated Price: ₦{predicted_price:,.0f}")

import joblib
joblib.dump(model, "model.pkl")