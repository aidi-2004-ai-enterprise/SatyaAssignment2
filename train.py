import pandas as pd
from sklearn.preprocessing import LabelEncoder
from xgboost import XGBClassifier
from sklearn.metrics import f1_score
from sklearn.model_selection import train_test_split
import joblib
import os
import seaborn as sns

# Load dataset
df = sns.load_dataset("penguins")
df.dropna(inplace=True)

# Encode categorical features
df["island"] = df["island"].astype("category").cat.codes
df["sex"] = df["sex"].astype("category").cat.codes

# Encode target
label_encoder = LabelEncoder()
df["species"] = label_encoder.fit_transform(df["species"])

# Split features and target
X = df.drop(columns=["species"])
y = df["species"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train XGBoost model
model = XGBClassifier(use_label_encoder=False, eval_metric="mlogloss", random_state=42)
model.fit(X_train, y_train)

# Evaluate
train_preds = model.predict(X_train)
test_preds = model.predict(X_test)

train_f1 = f1_score(y_train, train_preds, average="weighted")
test_f1 = f1_score(y_test, test_preds, average="weighted")

print(f"Train F1-score: {train_f1:.4f}")
print(f"Test F1-score: {test_f1:.4f}")

# Save model + encoder
os.makedirs("app/data", exist_ok=True)
model_bundle = {
    "model": model,
    "encoder": label_encoder
}
joblib.dump(model_bundle, "app/data/model.joblib")
print("✅ Model and encoder saved to app/data/model.joblib")
