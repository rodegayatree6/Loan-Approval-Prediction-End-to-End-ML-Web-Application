import streamlit as st
import requests

st.set_page_config(page_title="Loan Prediction App", layout="centered")

st.title("Loan Approval Prediction System")

st.write("Fill the details below to check loan approval status.")



Gender = st.selectbox("Gender", ["Male", "Female"])
Married = st.selectbox("Married", ["Yes", "No"])
Dependents = st.selectbox("Dependents", ["0", "1", "2", "3+"])
Education = st.selectbox("Education", ["Graduate", "Not Graduate"])
Self_Employed = st.selectbox("Self Employed", ["Yes", "No"])

ApplicantIncome = st.number_input("Applicant Income", min_value=0.0)
CoapplicantIncome = st.number_input("Coapplicant Income", min_value=0.0)
LoanAmount = st.number_input("Loan Amount", min_value=0.0)
Loan_Amount_Term = st.number_input("Loan Amount Term (in days)", min_value=0.0)
Credit_History = st.selectbox("Credit History", [1.0, 0.0])

Property_Area = st.selectbox("Property Area", ["Urban", "Rural", "Semiurban"])


if st.button("Predict Loan Status"):

    input_data = {
        "Gender": Gender,
        "Married": Married,
        "Dependents": Dependents,
        "Education": Education,
        "Self_Employed": Self_Employed,
        "ApplicantIncome": ApplicantIncome,
        "CoapplicantIncome": CoapplicantIncome,
        "LoanAmount": LoanAmount,
        "Loan_Amount_Term": Loan_Amount_Term,
        "Credit_History": Credit_History,
        "Property_Area": Property_Area
    }

    try:
        response = requests.post(
            "http://127.0.0.1:8000/predict",
            json=input_data
        )

        result = response.json()

        if result["Loan_Status"] == "Approved":
            st.success("✅ Loan Approved")
        else:
            st.error("❌ Loan Rejected")

    except:
        st.error("⚠️ Backend not running. Please start FastAPI server.")
