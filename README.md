# 💳 Credit Card Fraud Detection System

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
5. Model evaluation using:
   - Precision
   - Recall
   - F1-score
   - ROC-AUC
6. Deployment using Streamlit

---

## 📈 Results
| Model | ROC-AUC | Fraud Recall | Fraud Precision |
|-----|--------|-------------|----------------|
| Logistic Regression | 0.97 | 0.92 | 0.06 |
| Random Forest | 0.95 | 0.74 | 0.96 |

**Final Model Selected:** Random Forest  
Chosen due to better balance between fraud detection and false positives.

---

## 🚀 Application
A Streamlit web application allows users to input transaction features and predict whether a transaction is **fraudulent or legitimate**.

---

## 🛠 Tech Stack
- Python
- Pandas, NumPy
- Scikit-learn
- Matplotlib, Seaborn
- Streamlit
- Joblib

---

## 📂 Project Structure

CREDIT-CARD-FRAUD-DETECTION/
├── data/
│   └── creditcard.csv
│
├── notebook/
│   └── fraud_eda.ipynb
│
├── src/
│   └── train_model.py
│
├── models/
│   └── fraud_model.pkl
│
├── app.py
├── README.md
├── requirements.txt



## ⚙️ Installation

1. Clone the repository:
``` bash
git clone https://github.com/gumalwaddnyaneshwar/credit-card-fraud-detection.git
cd credit-card-fraud-detection

```
##  Install Dependencies

pip install -r requirments.txt



---

## ✍️ STEP 3: Add How to Run

```md
## ▶️ Run the Application

```bash
streamlit run app.py



```
## ✍️ STEP 4: Add PCA Explanation (VERY IMPORTANT FOR INTERVIEWS)

```md
## ❓ Why PCA Features (V1–V28)?
```
To protect customer privacy, original transaction features were transformed using
**Principal Component Analysis (PCA)**.

- Removes sensitive information
- Preserves important variance
- Reduces feature correlation
- Improves model performance

Only `Time` and `Amount` are original features.
```




## 📌 Future Enhancements

- Apply SMOTE for better imbalance handling
- Try XGBoost / LightGBM
- Tune classification threshold
- Deploy on Streamlit Cloud / AWS