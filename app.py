from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib

app=FastAPI()


class model_input(BaseModel):
    Age:int
    Income:int
    Loan_Amount:int
    Credit_Score:int
    Employment_Years:int
    Owns_House:int
    Married:int
    
model=joblib.load("Model.pkl")


@app.get("/")
def home():
    return {"message": "Loan Approval API Running"}

@app.post("/Predicted")
def predict_loan(input_parameters:model_input):
    # input_data=input_parameters.json()
    # input_dictionary=json.loads(input_data)
    
    # age=input_dictionary["Age"]
    # income=input_dictionary["Income"]
    # loan_amt=input_dictionary["Loan_Amount"]
    # credit_sc=input_dictionary["Credit_Score"]
    # enp_year=input_dictionary["Employment_Years"]
    # own_house=input_dictionary["Owns_House"]
    # married=input_dictionary["Married"]
    
    # input_list=[age,income,loan_amt,credit_sc,enp_year,own_house,married]
    input_list = [
        input_parameters.Age,
        input_parameters.Income,
        input_parameters.Loan_Amount,
        input_parameters.Credit_Score,
        input_parameters.Employment_Years,
        input_parameters.Owns_House,
        input_parameters.Married
    ]
    
    prediction=model.predict([input_list])
    
    if prediction[0]==0:
        return {"Result": "Loan is NOT approved"}
    else:
        return {"Result": "Loan is approved"}
    
    
    
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=10000)