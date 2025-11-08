from fastapi import FastAPI
from app.services.student_client import get_students_summary

app = FastAPI(title="Report Service", version="1.0.0")

@app.get("/reports/summary")
def summary():
    """
    Generates a simple report summarizing student data
    retrieved from the student-service (Node.js microservice).
    """
    return get_students_summary()
