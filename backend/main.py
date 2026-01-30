# main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from matcher import calculate_match_score

app = FastAPI(title="AI Resume Matcher")

class MatchRequest(BaseModel):
    resume_text: str
    job_text: str

class MatchResponse(BaseModel):
    match_score: float


@app.post("/match", response_model=MatchResponse)
def match_resume(request: MatchRequest):
    if not request.resume_text or not request.job_text:
        raise HTTPException(status_code=400, detail="Both resume and job text required")

    score = calculate_match_score(request.resume_text, request.job_text)
    return {"match_score": score}


@app.get("/")
def root():
    return {"message": "AI Resume Matcher backend is running!"}
