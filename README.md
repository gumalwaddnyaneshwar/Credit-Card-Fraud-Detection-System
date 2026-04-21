💳 Credit Card Fraud Detection System

## 📌 Problem Statement

Credit card fraud causes significant financial losses every year.  
This project builds a machine learning system to detect **fraudulent transactions** from highly imbalanced credit card transaction data.

---

## 📊 Dataset

- **Source:** Kaggle – Credit Card Fraud Detection
- **Transactions:** 284,807
- **Fraud Cases:** 492 (0.17%)
- **Features:**
  - `V1`–`V28`: PCA-transformed features (privacy-protected)
  - `Time`: Seconds since first transaction
  - `Amount`: Transaction amount
  - `Class`: Target (0 = Legit, 1 = Fraud)

---

## 🧠 Approach

1. Exploratory Data Analysis (EDA)
2. Handling highly imbalanced data using `class_weight`
3. Feature scaling for `Time` and `Amount`
4. Model training and comparison:
   - Logistic Regression
   - Random Forest
5. Model evaluation using Precision, Recall, F1-score, ROC-AUC
6. Deployment using Streamlit

---

## 📈 Results

| Model | ROC-AUC | Fraud Recall | Fraud Precision |
|---|---|---|---|
| Logistic Regression | 0.97 | 0.92 | 0.06 |
| Random Forest | 0.95 | 0.74 | 0.96 |

**Final Model Selected:** Random Forest — chosen for best balance between fraud detection and false positives.

---

## 🛠 Tech Stack

- Python, Pandas, NumPy
- Scikit-learn, Matplotlib, Seaborn
- Streamlit, Joblib

---

## 📂 Project Structure
Credit-Card-Fraud-Detection-System/
├── notebook/
│   └── fraud_eda.ipynb
├── src/
│   └── train_model.py
├── app.py
├── requirements.txt
└── README.md
---

## ⚙️ Installation

1. Clone the repository:
```bash
git clone https://github.com/gumalwaddnyaneshwar/Credit-Card-Fraud-Detection-System.git
cd Credit-Card-Fraud-Detection-System
Install dependencies:
pip install -r requirements.txt
▶️ Run the Application
streamlit run app.py
❓ Why PCA Features (V1–V28)?
To protect customer privacy, original transaction features were transformed using Principal Component Analysis (PCA):
Removes sensitive information
Preserves important variance
Reduces feature correlation
Only Time and Amount are original features.
📌 Future Enhancements
Apply SMOTE for better imbalance handling
Try XGBoost / LightGBM
Tune classification threshold
Deploy on Streamlit Cloud / AWS
---
