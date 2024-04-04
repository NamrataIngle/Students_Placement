# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 12:22:23 2024

@author: Dell
"""

# Import necessary libraries
import streamlit as st
import pickle

# Load the trained model from the pickle file
with open('lr.pkl', 'rb') as file:
    model = pickle.load(file)

# Define prediction function
def predict(cgpa, iq, profile_score):
    # Make prediction
    prediction = model.predict([[cgpa, iq, profile_score]])[0]
    return prediction

# Streamlit app
def main():
    # Set app title
    st.title('Student Placement Prediction')

    # Add input fields
    cgpa = st.number_input('CGPA', min_value=0.0, max_value=10.0, value=7.0, step=0.1)
    iq = st.number_input('IQ', min_value=0, max_value=200, value=100, step=1)
    profile_score = st.number_input('Profile Score', min_value=0, max_value=100, value=50, step=1)

    # Make prediction when button is clicked
    if st.button('Predict Placement'):
        prediction = predict(cgpa, iq, profile_score)
        st.write(f'Prediction: {"Placed" if prediction == 1 else "Not Placed"}')

if __name__ == '__main__':
    main()
