import requests
# import json

url='http://127.0.0.1:8000/Predicted'
# 42,102074,31790,847,3,1,1
#28,52745,31256,576,11,0,0
# 41,43093,45262,802,12,1,0
input_data_from_model={
    "Age":41,
    "Income":43093,
    "Loan_Amount":45262,
    "Credit_Score":802,
    "Employment_Years":12,
    "Owns_House":1,
    "Married":0
}

response = requests.post(url, json=input_data_from_model)

print("Status Code:", response.status_code)
print("Response:", response.json())