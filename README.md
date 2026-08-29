# 💳 AI Finance Controller

An AI-powered financial transaction reconciliation and exception management system built with Python and Streamlit.

## 🚀 Overview

AI Finance Controller analyzes payment transactions, compares transaction amounts with settlement amounts, identifies financial exceptions, and provides AI-generated explanations and recommended actions.

## ✨ Features

* 📊 Financial transaction dashboard
* 🔎 Transaction ID search
* ⚠️ Exception detection
* 🤖 AI-generated explanations
* 🚨 Exception priority classification
* 💰 Transaction and settlement amount comparison
* 📈 Transaction and exception charts
* 🔍 AI transaction investigation
* 📥 CSV exception report download

## 🛠️ Tech Stack

* Python
* Pandas
* Streamlit
* Git
* GitHub

## 📂 Project Structure

```text
razorpay-finance-ai/
│
├── dashboard.py
├── ai_explanation.py
├── generate_dataset.py
├── reconcile.py
├── synthetic_transactions.csv
├── exceptions.csv
├── ai_report.csv
├── requirements.txt
├── .gitignore
└── README.md
```

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/Kamalrenu143/razorpay-finance-ai.git
```

Open the project folder:

```bash
cd razorpay-finance-ai
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment on Windows:

```bash
.venv\Scripts\activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

## ▶️ Run the Dashboard

Start the Streamlit application:

```bash
python -m streamlit run dashboard.py
```

The dashboard will open in your browser.

## 🔄 How It Works

```text
Transaction Data
       ↓
Reconciliation Engine
       ↓
Exception Detection
       ↓
AI Analysis
       ↓
Priority Classification
       ↓
Dashboard Investigation
       ↓
Recommended Action
```

## 🎯 Use Case

The system demonstrates how payment transaction data can be automatically reconciled and analyzed to identify financial exceptions and help prioritize investigation.

## 📌 Project Status

Completed prototype with an interactive dashboard, transaction reconciliation, AI exception analysis, filtering, investigation, and CSV report export.

## 👨‍💻 Author

**Kamal Renu**
