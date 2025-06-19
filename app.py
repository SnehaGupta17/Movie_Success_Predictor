import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load your trained model and scaler
model = joblib.load('movie_success_prediction.pkl')
scaler = joblib.load('scaler.pkl')

st.title("🎬 Movie Success Prediction App")
st.write("Fill the details below to predict whether your movie will be a HIT or a FLOP!")

# --- User Inputs ---
title = st.text_input("Movie Title")
date = st.date_input("Release Date")

revenue = st.number_input("Revenue ($)", value=1000000.0)
budget = st.number_input("Budget ($)", value=500000.0)
score = st.slider("Score", min_value=0, max_value=100, value=70)

# --- Genre Selection ---
st.subheader("Genres")
genre_list = ['drama', 'comedy', 'action', 'thriller', 'romance', 'horror', 'crime',
              'sciencefiction', 'mystery', 'history', 'war', 'music', 'documentary',
              'tvmovie', 'western', 'unknown']
genres = st.multiselect("Select applicable genres", genre_list)

# --- Country Selection ---
st.subheader("Country")
country_options = ['country_IND', 'country_US', 'country_GB', 'country_JP', 'country_KR', 'country_IT', 'country_HK', 'country_other']
country = st.selectbox("Select production country", country_options)

# --- Industry ---
st.subheader("Industry")
industry = st.radio("Select Industry", ['Industry_Bollywood', 'Industry_Hollywood'])

# --- Button ---
if st.button("Predict"):
    # --- Prepare input data ---
    input_data = {
        'Revenue($)': revenue,
        'Budget($)': budget,
        'score': score
    }

    # Add genre columns
    for g in genre_list:
        input_data[g] = 1 if g in genres else 0

    # Add country columns
    for c in country_options:
        input_data[c] = 1 if c == country else 0

    # Add industry columns
    input_data['Industry_Bollywood'] = 1 if industry == 'Industry_Bollywood' else 0
    input_data['Industry_Hollywood'] = 1 if industry == 'Industry_Hollywood' else 0

    # Convert to DataFrame
    input_df = pd.DataFrame([input_data])

    # Scale the numeric columns
    input_df[['Revenue($)', 'Budget($)', 'score']] = scaler.transform(input_df[['Revenue($)', 'Budget($)', 'score']])

    # Make prediction
    prediction = model.predict(input_df)[0]
    result = "🎉 Hit Movie!" if prediction == 1 else "💔 Flop Movie."

    st.success(f"Prediction: **{result}**")

