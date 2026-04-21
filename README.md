💳 Credit Card Fraud Detection System
📌 Problem Statement
Credit card fraud causes significant financial losses every year.
This project builds a machine learning system to detect fraudulent transactions from highly imbalanced credit card transaction data.
📊 Dataset
Property
Detail
Source
Kaggle – Credit Card Fraud Detection
Total Transactions
284,807
Fraud Cases
492 (0.17%)
Features
V1–V28 (PCA), Time, Amount, Class
🧠 Approach
Exploratory Data Analysis (EDA)
Handling class imbalance using class_weight
Feature scaling for Time and Amount
Model training: Logistic Regression, Random Forest
Evaluation: Precision, Recall, F1-score, ROC-AUC
Deployment using Streamlit
📈 Results
Model
ROC-AUC
Fraud Recall
Fraud Precision
Logistic Regression
0.97
0.92
0.06
Random Forest
0.95
0.74
0.96
Final Model Selected: Random Forest — best balance between fraud detection and false positives.
🛠 Tech Stack
Python | Pandas | NumPy | Scikit-learn | Matplotlib | Seaborn | Streamlit | Joblib
📂 Project Structure
Credit-Card-Fraud-Detection-System/
├── notebook/
│   └── fraud_eda.ipynb
├── src/
│   └── train_model.py
├── app.py
├── requirements.txt
└── README.md
⚙️ Installation
1. Clone the repository
git clone https://github.com/gumalwaddnyaneshwar/Credit-Card-Fraud-Detection-System.git
cd Credit-Card-Fraud-Detection-System
2. Install dependencies
pip install -r requirements.txt
▶️ Run the Application
streamlit run app.py
❓ Why PCA Features (V1–V28)?
To protect customer privacy, original transaction features were transformed using Principal Component Analysis (PCA):
Removes sensitive personal information
Preserves important variance in the data
Reduces feature correlation
Improves model performance
Only Time and Amount are original (non-PCA) features.
📌 Future Enhancements
Apply SMOTE for better imbalance handling
Try XGBoost / LightGBM models
Tune classification threshold for better recall
Deploy on Streamlit Cloud / AWS