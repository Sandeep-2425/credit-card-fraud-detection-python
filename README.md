# 💳 Credit Card Fraud Detection

A Machine Learning-based web application designed to detect potentially fraudulent credit card transactions by analyzing transaction features and classifying them as **legitimate or fraudulent**.

## 📌 Overview

Credit card fraud is a major challenge in the financial sector due to the large volume of transactions and constantly evolving fraud patterns.

This project uses Machine Learning techniques to identify potentially fraudulent transactions. The project includes data preprocessing, feature scaling, model training, evaluation, and a Flask-based web interface for making predictions.

## 🚀 Key Features

- Data preprocessing and cleaning
- Handling transaction data
- Feature scaling using `StandardScaler`
- Machine Learning-based fraud classification
- Model training using Logistic Regression
- Model evaluation using classification metrics
- Flask web application for fraud prediction
- User-friendly prediction interface
- Saved trained model and scalers for prediction

## 🛠️ Technologies Used

- **Python**
- **NumPy**
- **Pandas**
- **Scikit-learn**
- **Flask**
- **Pickle**
- **HTML/CSS**

## 🤖 Machine Learning

The project uses **Logistic Regression** for classifying credit card transactions.

The transaction features are processed and scaled before being passed to the trained model.

### Model Pipeline

```text
Transaction Data
       ↓
Data Preprocessing
       ↓
Feature Selection
       ↓
Feature Scaling
       ↓
Logistic Regression
       ↓
Fraud Prediction
       ↓
Legitimate / Fraudulent
```

The trained model and preprocessing scalers are stored as `.pkl` files and loaded by the Flask application during prediction.

## 🌐 Web Application

The project includes a Flask-based web application that allows users to enter transaction details and receive a fraud prediction.

### Application Flow

```text
User
 ↓
Flask Web Interface
 ↓
Transaction Details
 ↓
Feature Preprocessing
 ↓
Trained ML Model
 ↓
Prediction
 ↓
Legitimate / Fraudulent
```

## 📁 Project Structure

```text
Credit-Card-Fraud-Detection/
│
├── data/
│   └── miniproject.csv
│
├── models/
│   ├── amount.pkl
│   ├── model.pkl
│   └── time.pkl
│
├── src/
│   └── miniproject.py
│
├── static/
│   └── many-credit-cards-on-blurred-600nw-2478118299.jpg
│
├── templates/
│   └── index.html
│
├── .gitignore
├── app.py
├── README.md
└── requirements.txt
```

## 📊 Dataset

The project uses a credit card transaction dataset containing transaction-related features used to train the fraud detection model.

The dataset is stored in:

```text
data/miniproject.csv
```

## 📈 Model Evaluation

The Machine Learning model can be evaluated using classification metrics such as:

- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix

For fraud detection, **precision and recall** are particularly important because both false positives and false negatives can have significant consequences.

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/Sandeep-2425/Credit-Card-Fraud-Detection.git
```

### 2. Navigate to the project directory

```bash
cd Credit-Card-Fraud-Detection
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

#### Windows

```bash
venv\Scripts\activate
```

#### macOS/Linux

```bash
source venv/bin/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

## ▶️ Running the Application

Start the Flask application:

```bash
python app.py
```

The application will run locally.

Open the displayed local URL in your web browser.

## 🎯 Objective

The primary objective of this project is to develop a Machine Learning-based fraud detection system capable of identifying potentially fraudulent credit card transactions.

The project also demonstrates how a trained Machine Learning model can be integrated into a Flask web application for real-world prediction.

## 🔮 Future Improvements

- Hyperparameter optimization
- Experiment with advanced classification algorithms
- Improve handling of class imbalance
- Model performance optimization
- Real-time fraud detection
- Deployment using cloud platforms
- Interactive analytics dashboard
- Integration with real-time transaction streams
- REST API deployment using Flask/FastAPI

## 👨‍💻 Author

**Sandeep Bisht**

MCA | Artificial Intelligence & Machine Learning

📧 **Email:** ssandeepbisht@gmail.com