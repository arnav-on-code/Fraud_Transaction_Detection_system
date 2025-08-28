Fraud Transaction Detection Project

Overview

This project aims to build a robust machine learning system to detect fraudulent credit card transactions. Using a real-world anonymized dataset, we explore data preprocessing, class imbalance handling, model building, evaluation, and explainability to deliver a high-accuracy fraud detection pipeline.

Dataset
The dataset contains 284,807 transactions and 34 features including anonymized principal components (V1–V28), transaction Time, and Amount.

Fraudulent transactions account for approximately 0.17% of all samples.

No missing values; 1,081 duplicate entries are removed during preprocessing.

===Project Structure===

financial-fraud-detection/
 ├── data/
 │    ├── raw/                  # Original raw data files (not included in repo)
 │    ├── processed/            # Cleaned and preprocessed data files
 ├── reports/                   # EDA insights, plots, and evaluation reports
 ├── src/                      # Source code files (training, evaluation, explainability)
 │    ├── train_baseline.py     # Training baseline models (Logistic Regression, RF)
 ├── notebooks/                 # Jupyter notebooks (optional)
 ├── README.md                  # Project overview and instructions
 └── requirements.txt           # Python dependencies

 
===Key Steps===


1. Data Preprocessing


Removed duplicates.
Handled class imbalance using SMOTE synthetic oversampling.
Performed feature selection guided by correlation with the target.

2. Model Building

   
Baseline models: Logistic Regression and Random Forest.
Balanced class weights used to handle imbalance.
Train/test split was stratified to maintain class distribution.

4. Model Evaluation

   
Metrics reported: Precision, Recall, F1-Score, Confusion Matrix, ROC-AUC, and Precision-Recall AUC.
Random Forest achieved near-perfect performance (ROC-AUC: 1.0).
Logistic Regression offers an interpretable baseline with ROC-AUC ~0.995.

4. Model Explainability

   
Used SHAP for feature importance and transparent insights.
Identified top features influencing fraud prediction to assist domain experts.

===How to Run===

Setup Environment

bash
conda create -n fraud-detection python=3.9
conda activate fraud-detection
pip install -r requirements.txt

Train Models
bash
python src/train_baseline.py

Explain Model Predictions
bash
Requirements
Python 3.9+

===Packages===
pandas, scikit-learn, imblearn, matplotlib, shap, joblib


===Results Summary===


Model	Accuracy	Fraud Precision	Fraud Recall	ROC-AUC
Logistic Regression	97.42%	98.22%	96.58%	0.9953
Random Forest	99.98%	99.97%	100.00%	1.0000



===Future Work===

Incorporate more advanced models such as XGBoost or LightGBM.

Deploy the model as an API for real-time fraud detection.

Extend the feature engineering with temporal/spatial patterns.

Conduct rigorous testing on unseen real-world data.

===References===

Kaggle Credit Card Fraud Detection Dataset

SMOTE Paper

SHAP: A Unified Approach to Interpreting Model Predictions (Lundberg & Lee, 2017)
