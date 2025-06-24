# 🎬 Movie Success Predictor

A Machine Learning project that predicts whether a movie will be a **Hit** or **Flop** based on various features such as **budget**, **revenue**, **genre**, **language**, and **country**. The model is trained on a combined dataset of Bollywood and Hollywood movies and fine-tuned using hyperparameter optimization.

---

## 📊 Project Overview

This project aims to analyze and predict the commercial success of movies using supervised classification. The target variable is `Success_Status`, which is binary:  
- `1` = Hit  
- `0` = Flop  

The project performs extensive preprocessing, feature engineering, and applies Logistic Regression with `RandomizedSearchCV` to achieve a high accuracy.

---

## 🗂️ Dataset Description

Two datasets were used:
- `Final Bollywood.csv`
- `Final Hollywood.csv`

Each contains:
- `Title`: Movie name  
- `Date`: Release date  
- `Genre`: One or more genres  
- `orig_lang`: Original language  
- `Revenue($)`: Box office revenue  
- `Budget($)`: Production budget  
- `country`: Country of production  
- `score`: External score (e.g., IMDb or critic)

---

## ⚙️ Workflow

1. **Data Cleaning & Merging**
   - Merged Bollywood & Hollywood data.
   - Filled missing genres with `'Unknown'`.
   - Cleaned and standardized `Genre`, `Language`, and `Country`.

2. **Feature Engineering**
   - Multi-label genre encoding (`MultiLabelBinarizer`)
   - One-hot encoding for:
     - Top 10 languages and countries
     - Industry (`Bollywood`, `Hollywood`)

3. **Target Variable Creation**
   - A movie is classified as `Hit` if `Revenue ≥ Budget`.

4. **Modeling**
   - Logistic Regression
   - Hyperparameter tuning via `RandomizedSearchCV`
   - Evaluation using:
     - Accuracy
     - Classification Report
     - Confusion Matrix

5. **Model Performance**
   - 🔥 **Accuracy**: 94.39%
   - **Precision (Flop class)**: 80%
   - **Recall (Hit class)**: 94%

6. **Model Deployment**
   - Exported model: `movie_success_prediction.pkl`
   - Exported scaler: `scaler.pkl`


---


## 🙋‍♀️ About Me

This project is created by **Sneha Gupta**, a final-year Engineering student specializing in **Artificial Intelligence and Data Science**.  
Connect with me on [LinkedIn](https://www.linkedin.com/in/sneha-gupta17).
