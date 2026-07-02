import streamlit as st
import pickle

with open("poly.pkl", "rb") as f:
    poly = pickle.load(f)

with open("model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("💰 Salary Prediction")

level = st.number_input("Employee Level", 1.0, 10.0, 6.5, 0.1)

if st.button("Predict"):
    x = poly.transform([[level]])
    pred = model.predict(x)
    st.success(f"Predicted Salary: ₹{pred[0]:,.2f}")
