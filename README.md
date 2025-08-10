# 🐧 Lab 3 - Penguins Classification with XGBoost and FastAPI

## 🔍 Overview

This project involves building a machine learning pipeline using the Seaborn Penguins dataset. The pipeline includes preprocessing, training an XGBoost classification model, saving the model, and deploying it via a FastAPI server with a `/predict` endpoint.

## 📁 Project Structure

Lab3_SatyaMohanReddy_Ginni/
│
├── app/
│ ├── main.py # FastAPI application with /predict endpoint
│ ├── data/
│ │ └── model.json # Saved XGBoost model and label encoder
│
├── train.py # Script to preprocess data and train model
├── requirements.txt # Python dependencies
└── README.md # Project documentation

---

## 📊 Model Details

- **Model:** XGBoost Classifier
- **Target Variable:** `species`
- **Input Features:**

  - `island`
  - `bill_length_mm`
  - `bill_depth_mm`
  - `flipper_length_mm`
  - `body_mass_g`
  - `sex`

- **Encodings:**
  - `island` and `sex` are label-encoded.
  - `species` is the prediction output encoded as one of: `Adelie`, `Chinstrap`, or `Gentoo`.

---

## 🧠 Training the Model

Run the following command to train and save the model:

```bash
python train.py
```
