# 🎓 AI-Powered Student Study Tracker (Real Dataset Version)
# Full project code with all components using StudentsPerformance.csv

# ------------------------------------------
# ✅ 1. ML MODEL TRAINING (Real Data)
# ------------------------------------------
# File: ml_model/train_model.py

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib
import os
import pickle

# Load real dataset
df = pd.read_csv("StudentsPerformance.csv")
df["average_score"] = df[["math score", "reading score", "writing score"]].mean(axis=1)

def grade_classifier(avg):
    if avg >= 85:
        return "A"
    elif avg >= 70:
        return "B"
    else:
        return "C"

df["Final_Grade"] = df["average_score"].apply(grade_classifier)
data = df[["math score", "reading score", "writing score", "Final_Grade"]]

X = data.drop('Final_Grade', axis=1)
y = data['Final_Grade']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier()
model.fit(X_train, y_train)

print("Model trained on real dataset successfully")
print(classification_report(y_test, model.predict(X_test)))
'''
os.makedirs("ml_model", exist_ok=True)
joblib.dump(model, "ml_model/model.joblib")
'''
with open("student_model.pkl", "wb") as f:
    pickle.dump(model, f)


