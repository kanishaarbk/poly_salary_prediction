import streamlit as st
import pickle

# Load Polynomial Transformer
with open("poly.pkl", "rb") as f:
    poly = pickle.load(f)

# Load Model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

st.set_page_config(page_title="Salary Prediction", page_icon="💰")

st.title("💰 Salary Prediction")
st.write("Enter the employee level to predict salary.")

level = st.number_input(
    "Employee Level",
    min_value=1.0,
    max_value=10.0,
    value=1.0,
    step=0.5
)

if st.button("Predict Salary"):
    level_poly = poly.transform([[level]])
    prediction = model.predict(level_poly)

    st.success(f"💰 Predicted Salary: ₹{prediction[0]:,.2f}")
