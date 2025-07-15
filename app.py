# ------------------------------------------
# ✅ 3. FRONTEND (Streamlit)
# ------------------------------------------
# File: app.py

import streamlit as st
import requests
import matplotlib.pyplot as plt
import pandas as pd

st.set_page_config(page_title="🎓 AI-Powered Student Study Tracker", layout="centered")

# ---------- Custom CSS ----------
st.markdown("""
    <style>
    body {
        background-color: #f5f5f5;
    }
    .main {
        background-color: #ffffff;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 2px 2px 15px rgba(0, 0, 0, 0.1);
    }
    .css-1d391kg {
        padding-top: 2rem;
    }
    </style>
""", unsafe_allow_html=True)

# ---------- Title & Intro ----------
st.markdown("<h1 style='text-align: center; color: #1F4E79;'>🎓 AI-Powered Student Study Tracker</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>📥 Enter your test scores below to predict your final grade using machine learning!</p>", unsafe_allow_html=True)

# ---------- Input Form ----------
st.markdown("### 📐 Math Score")
math_score = st.slider("Math Score", 0, 100, 50)

st.markdown("### 📖 Reading Score")
reading_score = st.slider("Reading Score", 0, 100, 50)

st.markdown("### ✍️ Writing Score")
writing_score = st.slider("Writing Score", 0, 100, 50)

# ---------- Submit Button ----------
if st.button("🚀 Predict Final Grade"):
    with st.spinner('Predicting your grade...'):
        input_data = {
            "math_score": math_score,
            "reading_score": reading_score,
            "writing_score": writing_score
        }

        try:
            response = requests.post("http://127.0.0.1:8000/submit-form", json=input_data)
            result = response.json()
            st.success(f"🎉 Predicted Final Grade: **{result['prediction']}**")

            # ---------- User Score Bar Chart ----------
            st.markdown("### 📊 Your Score Comparison")
            fig, ax = plt.subplots()
            ax.bar(["Math", "Reading", "Writing"],
                   [math_score, reading_score, writing_score],
                   color=["#1F77B4", "#FF7F0E", "#2CA02C"])
            ax.set_ylim(0, 100)
            ax.set_ylabel("Score")
            st.pyplot(fig)

            # ---------- Class Grade Distribution Pie Chart ----------
            df = pd.read_csv("StudentsPerformance.csv")
            df["average_score"] = df[["math score", "reading score", "writing score"]].mean(axis=1)

            def classify_grade(avg):
                if avg >= 85:
                    return "A"
                elif avg >= 70:
                    return "B"
                else:
                    return "C"

            df["Final_Grade"] = df["average_score"].apply(classify_grade)
            grade_counts = df["Final_Grade"].value_counts()

            st.markdown("### 🧮 Class Grade Distribution")
            fig2, ax2 = plt.subplots()
            ax2.pie(grade_counts.values, labels=grade_counts.index,
                    autopct='%1.1f%%', startangle=90,
                    colors=["#4CAF50", "#FFC107", "#F44336"])
            ax2.axis('equal')
            st.pyplot(fig2)

        except Exception as e:
            st.error("❌ Couldn't connect to backend. Make sure FastAPI is running.")
