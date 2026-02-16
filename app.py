from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd
import pickle

app = FastAPI(title="Loan Prediction API")


with open("final_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

with open("encoder.pkl", "rb") as f:
    encoder = pickle.load(f)


columns_num = [
    "ApplicantIncome",
    "CoapplicantIncome",
    "LoanAmount",
    "Loan_Amount_Term",
    "Credit_History"
]

columns_cat = [
    "Gender",
    "Married",
    "Dependents",
    "Education",
    "Self_Employed",
    "Property_Area"
]


class LoanInput(BaseModel):
    Gender: str
    Married: str
    Dependents: str
    Education: str
    Self_Employed: str
    ApplicantIncome: float
    CoapplicantIncome: float
    LoanAmount: float
    Loan_Amount_Term: float
    Credit_History: float
    Property_Area: str



@app.get("/")
def home():
    return {"message": "Loan Prediction API Running Successfully"}



@app.post("/predict")
def predict(data: LoanInput):

    input_dict = data.dict()

    

    input_dict["Gender"] = input_dict["Gender"].capitalize()
    input_dict["Self_Employed"] = input_dict["Self_Employed"].capitalize()
    input_dict["Property_Area"] = input_dict["Property_Area"].capitalize()

    
    if input_dict["Married"].lower() in ["unmarried", "no"]:
        input_dict["Married"] = "No"
    else:
        input_dict["Married"] = "Yes"

    
    if input_dict["Education"].lower() in ["under graduate", "not graduate"]:
        input_dict["Education"] = "Not Graduate"
    else:
        input_dict["Education"] = "Graduate"

    
    if input_dict["Dependents"] not in ["0", "1", "2", "3+"]:
        input_dict["Dependents"] = "3+"

  

    
    if input_dict["LoanAmount"] > 2000:
        raise HTTPException(
            status_code=400,
            detail="LoanAmount scale mismatch. Use dataset scale (e.g., 150 not 150000)."
        )

    
    if input_dict["Credit_History"] not in [0, 1]:
        raise HTTPException(
            status_code=400,
            detail="Credit_History must be 0 or 1."
        )

    

    df = pd.DataFrame([input_dict])

    
    df_num = scaler.transform(df[columns_num])

    
    df_cat = encoder.transform(df[columns_cat])

  
    df_final = pd.concat(
        [
            pd.DataFrame(df_num, columns=columns_num),
            pd.DataFrame(df_cat, columns=encoder.get_feature_names_out(columns_cat))
        ],
        axis=1
    )

    

    prediction = model.predict(df_final)[0]
    probability = model.predict_proba(df_final)[0][1]

    result = "Approved" if prediction == 1 else "Rejected"

    return {
        "Loan_Status": result,
        "Approval_Probability": round(float(probability), 3)
    }
