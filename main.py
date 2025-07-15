
# ------------------------------------------
# ✅ 2. BACKEND (FastAPI)
# ------------------------------------------
# File: backend/main.py
import numpy as np

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import joblib
import pandas as pd
from sqlalchemy import create_engine, Column, Integer, Float, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import pickle



with open("student_model.pkl", "rb") as f:
    model = pickle.load(f)
    
app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For dev; in production, restrict to your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Database setup
SQLALCHEMY_DATABASE_URL = "sqlite:///./database/student_data.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
Base = declarative_base()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class StudentData(BaseModel):  # ✅ Must inherit from BaseModel
    math_score: int
    reading_score: int
    writing_score: int
'''
class StudentData(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    math_score = Column(Float)
    reading_score = Column(Float)
    writing_score = Column(Float)
    Predicted_Grade = Column(String)

Base.metadata.create_all(bind=engine)
'''
# Load model
model = joblib.load("ml_model/model.joblib")

# Input schema
class StudentInput(BaseModel):
    math_score: float
    reading_score: float
    writing_score: float
'''
@app.post("/submit-form")
def submit_data(data: StudentInput):
    df = pd.DataFrame([data.dict()])
    prediction = model.predict(df)[0]

    db = SessionLocal()
    student = StudentData(**data.dict(), Predicted_Grade=prediction)
    db.add(student)
    db.commit()
    db.refresh(student)
    db.close()

    return {"prediction": prediction}
'''
@app.post("/submit-form")
async def submit_form(data: StudentData):
    try:
        features = np.array([[data.math_score, data.reading_score, data.writing_score]])
        prediction = model.predict(features)[0]
        return {"prediction": prediction}
    except Exception as e:
        import traceback
        traceback.print_exc()  # 🔥 Show full error in terminal
        return {"error": str(e)}

@app.get("/")
def root():
    return {"message": "Student Study Tracker API"}
