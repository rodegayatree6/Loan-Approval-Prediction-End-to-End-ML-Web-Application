# Loan-Approval-Prediction-End-to-End-ML-Web-Application
This project is a complete end-to-end Machine Learning based web application developed using FastAPI (Backend) and Streamlit (Frontend).  
The system allows users to:  
Train a model using a custom dataset  
Test the model using test data  
Predict loan approval for a single applicant  
View model evaluation metrics

 Problem Statement

The objective of this project is to predict whether a loan application will be approved or not based on applicant details such as:

Gender
Marital Status
Education
Income
Loan Amount
Credit History
Property Area
etc.

Tech Stack Used

Python
Machine Learning (Scikit-learn)
FastAPI
Uvicorn
Streamlit
Pandas & NumPy
Joblib
Postman

Git & GitHub
Project Structure
Loan-Prediction-System/
│
├── backend/
│   ├── app.py
│   ├── loan_prediction system.ipynb
│
├── frontend/
│   └── frontend.py
│
├── dataset/
│   ├── loan_data.csv
│   
│
├── models/
│   └── encoder.pkl
|   └── final_model.pkl
|   └── scaler.pkl
│
├──
└── README.md

API Endpoints
1️/train

Upload training dataset (CSV)

Trains ML model

Saves best performing model

Returns training accuracy

2️/test

Upload testing dataset

Evaluates trained model

Returns evaluation metrics

3️/predict

Accepts JSON input

Returns loan approval prediction

Example JSON:

{
  "Gender": "Male",
  "Married": "Yes",
  "Dependents": "0",
  "Education": "Graduate",
  "Self_Employed": "No",
  "ApplicantIncome": 5000,
  "CoapplicantIncome": 0,
  "LoanAmount": 150,
  "Loan_Amount_Term": 360,
  "Credit_History": 1,
  "Property_Area": "Urban"
}
