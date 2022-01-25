import streamlit as st
import pickle
import numpy as np

# Import the model
pipe = pickle.load(open('lr_model.pkl','rb'))
data = pickle.load(open('df.pkl','rb'))
st.title('House Price Predictor')

# Location
location = st.selectbox('Choose the Location', data['location'].unique())

# Sqft Area
total_sqft = st.number_input('Enter the total sqft area you want', step=100)

# Number of Bathrooms
bath = st.number_input('Enter the number of bathrooms you want', step=1)

# BHK 
bhk = st.number_input('Enter BHK', step=1)

if st.button('Predict Price'):
    query = np.array([location, total_sqft, bath, bhk])
    query = query.reshape(1,4)

    st.title('This House can cost you approximately ', int(pipe.predict(query)[0]))
