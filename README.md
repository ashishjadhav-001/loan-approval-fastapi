# Loan Approval Prediction API (FastAPI + Machine Learning)

## Project Overview

This project builds a **Machine Learning model to predict whether a loan will be approved or not** based on applicant information.
The trained model is deployed as a **REST API using FastAPI** and hosted online using **Render**.

Users can send applicant data to the API and receive a prediction response.

---

## Tech Stack

* **Python**
* **FastAPI**
* **Scikit-learn**
* **XGBoost**
* **Pydantic**
* **Uvicorn**
* **Render (Cloud Deployment)**

---

## Project Workflow

1. Data preprocessing and analysis
2. Model training and evaluation
3. Model saving using `joblib`
4. API creation using FastAPI
5. Deployment to Render

---

## Project Structure

```
loan-approval-fastapi/
│
├── app.py                     # FastAPI application
├── Model.pkl                  # Trained ML model
├── requirements.txt           # Project dependencies
├── loan_approval.ipynb        # Model training notebook
└── README.md
```

---

## API Endpoint

### Predict Loan Approval

**POST /predict**

Input JSON:

```json
{
  "Age": 28,
  "Income": 52745,
  "Loan_Amount": 31356,
  "Credit_Score": 576,
  "Employment_Years": 11,
  "Owns_House": 0,
  "Married": 0
}
```

Example Response:

```json
{
  "result": "Loan Approved"
}
```

---

## Live API

You can access the deployed API here:

```
https://loan-approval-fastapi.onrender.com
```

Swagger documentation:

```
https://loan-approval-fastapi.onrender.com/docs
```

---

## How to Run Locally

### 1. Clone Repository

```
git clone https://github.com/ashishjadhav-001/loan-approval-fastapi.git
cd loan-approval-fastapi
```

### 2. Install Dependencies

```
pip install -r requirements.txt
```

### 3. Run FastAPI Server

```
uvicorn app:app --reload
```

### 4. Open Swagger UI

```
http://127.0.0.1:8000/docs
```

---

## Example Python Request

```python
import requests

url = "https://loan-approval-fastapi.onrender.com/predict"

data = {
    "Age": 28,
    "Income": 52745,
    "Loan_Amount": 31356,
    "Credit_Score": 576,
    "Employment_Years": 11,
    "Owns_House": 0,
    "Married": 0
}

response = requests.post(url, json=data)

print(response.json())
```

---

## Future Improvements

* Add model probability output
* Build frontend UI using Streamlit
* Add Docker containerization
* Implement authentication

---

## Author

Ashish Jadhav
