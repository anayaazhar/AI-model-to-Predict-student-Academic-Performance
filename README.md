**🎓 AI-Powered Student Study Tracker**

A smart and interactive web application that predicts a student's final grade based on their Math, Reading, and Writing scores using a trained machine learning model.

**It uses:**

🧠 FastAPI for the backend (ML model & prediction API)

🎨 Streamlit for a modern and beautiful frontend

📊 Matplotlib for visualizations

📁 A real-world dataset (StudentsPerformance.csv) for training

**📌 Features**

🔢 Enter scores through sliders

🤖 Predict final grade (A / B / C) using ML

📊 Bar chart showing your score comparison

🥧 Pie chart for class grade distribution

⚡ Fast, responsive, and user-friendly UI

💻 Runs fully locally with no external dependencies

**📁 Folder Structure**

STUDENT/
├── app.py                  # Streamlit frontend
├── main.py                 # FastAPI backend
├── train_model.py          # ML training script
├── requirements.txt        # Dependencies
├── StudentsPerformance.csv # Dataset
├── ml_model/
│   └── model.joblib        # Trained model
└── database/               # Reserved for future use

**🚀 Getting Started**

1. Clone the repository

git clone https://github.com/your-username/student-study-tracker.git
cd student-study-tracker

2. Install Dependencies

pip install -r requirements.txt

3. Train the Model (if not already done)

python train_model.py

4. Start the Backend (FastAPI)

uvicorn main:app --reload

5. Launch the Frontend (Streamlit)

streamlit run app.py



**📚 Dataset**

The dataset used is StudentsPerformance.csv, containing:

Math, Reading, Writing scores

Additional features (e.g., gender, parental education)

**🎯 Grade Classification Logic**

Grades are predicted based on the average of the 3 scores:

A: 85 and above

B: 70–84

C: Below 70

**✨ Future Enhancements**

🔐 Add login/signup to track user sessions

💾 Export results as PDF or CSV

📈 Track score trends over time

🎯 Personalized study suggestions

**🧠 Tech Stack**

Python

FastAPI

Streamlit

Scikit-learn

Matplotlib

**🙌 Author**

Anaya Azhar📍 Islamabad, Pakistan
