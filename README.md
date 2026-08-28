# Customer Churn Prediction

An end-to-end Machine Learning project that predicts whether a telecom customer is likely to churn and assigns a risk level based on the predicted churn probability.

## Overview

Customer churn is a major challenge for subscription-based businesses. This project uses the Telco Customer Churn dataset to analyze customer behavior, train machine learning models, optimize the prediction threshold, and deploy the final model using FastAPI.

## Project Workflow

- Data Cleaning & Preprocessing
- Exploratory Data Analysis
- Feature Analysis
- Model Training & Comparison
- Threshold Optimization
- Model Evaluation
- Churn Risk Analysis
- FastAPI Deployment

## Dataset

The project uses the Telco Customer Churn dataset containing information about customer demographics, services, contracts, payment methods, and billing.

**Total Customers:** 7,043

**Target Variable:** `Churn`

- `No` → Customer retained
- `Yes` → Customer churned

## Exploratory Analysis

### Churn Rate by Contract Type

| Contract Type | Churn Rate |
|---|---:|
| Month-to-month | 42.71% |
| One year | 11.27% |
| Two year | 2.83% |

### Churn Rate by Tenure

| Tenure Group | Churn Rate |
|---|---:|
| 0–6 months | 52.94% |
| 7–12 months | 35.89% |
| 13–24 months | 28.71% |
| 25–48 months | 20.39% |
| 49–72 months | 9.51% |

The highest churn occurs among customers with short tenure and month-to-month contracts.

## Machine Learning Models

The following models were evaluated:

- Logistic Regression
- Random Forest
- Gradient Boosting

| Model | Accuracy | Precision | Recall | F1-Score | ROC-AUC |
|---|---:|---:|---:|---:|---:|
| Logistic Regression | 80.55% | 65.72% | 55.88% | 60.40% | 84.21% |
| Random Forest | 78.35% | 62.11% | 47.33% | 53.72% | 82.27% |
| Gradient Boosting | 80.48% | 66.89% | 52.41% | 58.77% | 84.41% |

Logistic Regression was selected as the final model because of its strong performance and interpretability.

## Threshold Optimization

The classification threshold was reduced from `0.50` to `0.33` to improve the detection of customers likely to churn.

**Best Threshold:** `0.33`

**Best Cross-Validation F1-Score:** `0.6375`

This increases churn recall while accepting more false positives.

## Final Model Performance

| Metric | Result |
|---|---:|
| Decision Threshold | 0.33 |
| Accuracy | 76.15% |
| Precision | 53.80% |
| Recall | 71.93% |
| F1-Score | 61.56% |
| ROC-AUC | 84.21% |
| Average Precision | 63.43% |

### Confusion Matrix
                 Predicted
                 No     Yes

Actual No        804    231
Actual Yes       105    269
The optimized model identifies 71.93% of actual churn customers, making it useful for customer-retention analysis.

Important Churn Factors

Features associated with higher churn include:

Month-to-month contracts
Fiber optic Internet Service
Short customer tenure
Electronic check payment
No Online Security
No Tech Support
Streaming services

Features associated with lower churn include:

Long customer tenure
Two-year contracts
DSL Internet Service
Dependents
API

The trained model is deployed using FastAPI.

API Endpoints
Method	Endpoint	Description
GET	/	API status
GET	/health	Health check
POST	/predict	Predict customer churn

Interactive API documentation is available at:

http://127.0.0.1:8000/docs
Example Prediction
{
  "churn_probability": 0.8113,
  "prediction": 1,
  "risk_level": "High"
}

Where:

0 = No Churn
1 = Churn
Project Structure
Customer Churn Prediction/
│
├── app/
│   └── main.py
│
├── data/
│   └── raw/
│       └── Telco-Customer-Churn.csv
│
├── models/
│   └── churn_model.joblib
│
├── notebooks/
│   └── churn_analysis.ipynb
│
├── src/
│   ├── predict.py
│   └── test_prediction.py
│
├── .gitignore
├── README.md
└── requirements.txt
Technologies Used
Python
Pandas
NumPy
Scikit-learn
Matplotlib
Seaborn
Statsmodels
Joblib
FastAPI
Uvicorn
Jupyter Notebook
Installation
git clone https://github.com/Debankumardas/customer-churn-prediction.git
cd customer-churn-prediction

Create and activate a virtual environment:

python -m venv .venv
.venv\Scripts\Activate.ps1

Install dependencies:

pip install -r requirements.txt
Run the API
python -m uvicorn app.main:app --reload

Open the API documentation:

http://127.0.0.1:8000/docs
Limitations
The model is trained on historical telecom customer data.
The optimized threshold improves recall at the cost of precision.
Predictions should support business decisions rather than replace them.
The current API is intended as a project/demo deployment.
Future Improvements
Hyperparameter tuning
Probability calibration
Model monitoring
Automated model retraining
Cloud deployment
Customer retention recommendation system
CRM integration
Author

Deban Kumar Das D
BCA – Data Science

### Then scroll to the bottom
For the commit message, enter:
Add project documentation
