# 💻 Laptop Price Prediction

This repository contains an **end-to-end machine learning project** using a dataset **(laptops.csv)** scraped from [Smartprix](https://www.smartprix.com) with **Selenium**.  
The dataset is extracted and shared **for research and educational purposes only**.  

It provides structured tabular data, making it ideal for:
- 📈 Regression tasks (predicting laptop price from specifications)  
- 🧩 Feature engineering & preprocessing  
- 📊 Data visualization & market analysis  

---

## 📊 Dataset Highlights
- **Source**: [Smartprix](https://www.smartprix.com)  
- **Format**: CSV (tabular)  
- **Target Variable**: `Price`  
- **Features**: Brand, Processor, Cores, RAM, Storage, GPU, Display, OS, Weight, etc.  
- ✅ Dataset has been **cleaned** (handling duplicates, missing values, formatting)  
- 🔍 **Exploratory Data Analysis (EDA)** performed to generate the cleaned dataset  

---

## 🛠 Tools & Libraries
- **Python**  
- **NumPy**, **Pandas** → Data handling  
- **Matplotlib**, **Seaborn** → Data visualization & EDA  
- **Scikit-Learn / TensorFlow** → Machine learning & regression  
- **Selenium** → Web scraping  

---

## 🚀 Workflow (End-to-End)
1. **Data Collection** → Scraped laptop data using Selenium  
2. **Data Cleaning** → Removed duplicates, handled nulls, formatted features  
3. **EDA** → Visualized distributions & relationships  
4. **Feature Engineering** → Converted categorical columns using **One-Hot Encoding**
5. **Modeling** → Regression models are used predict price  
6. **Evaluation** → Metrics like RMSE, R², MSE  


