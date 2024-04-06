import pickle
import streamlit as st

model = pickle.load(open('model.pkl', 'rb'))
st.title("Breast Cancer Prediction using ML")

col1, col2 = st.columns(2)

with col1:
    mean_radius = st.text_input('Mean radius')

with col2:
    mean_texture = st.text_input('Mean texture')

with col1:
    mean_perimeter = st.text_input('Mean perimeter')

with col2:
    mean_area = st.text_input('Mean area')

with col1:
    mean_smoothness = st.text_input('Mean smoothness')

# code for Prediction
diagnosis = ''

# creating a button for Prediction
if st.button("Breast Cancer Test Result"):
    prediction = model.predict([[mean_radius, mean_texture, mean_perimeter, mean_area, mean_smoothness]])

    if prediction[0] == 1:
        diagnosis = "The Women has Breast Cancer disease"
    else:
        diagnosis = "The Women does not have Breast Cancer disease"

st.success(diagnosis)

