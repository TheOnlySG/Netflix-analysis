# 🎬 Netflix Data Analysis & Interactive Dashboard

> 📊 An end-to-end data analysis project exploring Netflix content trends, enhanced with an interactive dashboard built using Streamlit.

---

## 🧠 Overview

This project analyzes Netflix’s dataset to uncover patterns in:

* Content distribution (Movies vs TV Shows)
* Growth trends over time
* Genre popularity
* Country-wise production

It follows a complete workflow:
➡️ Data Cleaning → EDA → Insights → Interactive Dashboard

---

## 📊 Key Insights

* 🎥 **Movies dominate** Netflix’s catalog compared to TV Shows
* 📈 **Content growth surged** in recent years
* 🎭 **Drama, Comedy, and International genres** are most frequent
* 🌍 **Content production is concentrated** in a few countries

---

## ⚙️ Features

* 🧹 Data cleaning and preprocessing
* 🏗️ Feature engineering (`year_added`, duration split, genres)
* 📊 Exploratory Data Analysis (EDA)
* 🌐 Interactive dashboard with filters

---

## 🖥️ Dashboard

Run the Streamlit app locally:

```bash
streamlit run app.py
```

---

## 🛠️ Tech Stack

* 🐍 Python
* 📊 Pandas
* 🔢 NumPy
* 📈 Matplotlib
* 🌐 Streamlit

---

## 📁 Project Structure

```bash
Netflix-analysis/
│
├── app.py              # Streamlit dashboard
├── requirements.txt    # Project dependencies
├── data/               # Dataset (CSV)
├── notebooks/          # Jupyter notebooks (EDA)
└── README.md
```

---

## 🚀 Setup & Run

### 1️⃣ Clone the repository

```bash
git clone https://github.com/TheOnlySG/Netflix-analysis.git
cd Netflix-analysis
```

### 2️⃣ Activate virtual environment

```bash
source ../venv/bin/activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the dashboard

```bash
streamlit run app.py
```
---
