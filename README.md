# 🤖 AI Resume Matcher

[![Python](https://img.shields.io/badge/Python-3.11-blue)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.111.1-green)](https://fastapi.tiangolo.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)

AI-powered application that analyzes resumes and matches them with job descriptions using NLP and semantic similarity.

---

## 🚀 Features

- Upload or paste your **resume text** (PDF or TXT)
- Paste a **job description**
- AI calculates **match score** (0–100%) between resume & job
- Highlights missing skills (via embeddings)
- Mobile-friendly **frontend**
- Clean API backend with **FastAPI**
- Containerized with **Docker + Docker Compose**

---

## 💻 Tech Stack

| Layer      | Technology |
|-----------|------------|
| Backend   | Python, FastAPI, Uvicorn |
| AI / NLP  | Sentence Transformers, scikit-learn |
| Resume Parsing | PyPDF2 |
| Frontend  | HTML, CSS, JavaScript |
| Containerization | Docker, Docker Compose |

---

 📂 Repository Structure
ai-resume-matcher/
├── backend/
│   ├── main.py
│   ├── matcher.py
│   ├── resume_parser.py
│   └── requirements.txt
├── frontend/
│   ├── index.html
│   ├── app.js
│   └── style.css
├── examples/
│   ├── sample_resume.txt
│   └── job_description.txt
├── .gitignore
├── docker-compose.yml
└── README.md

---
---

## ⚡ Quick Start

### 1️⃣ Locally (Python)
bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload

•	Visit http://127.0.0.1:8000 → backend running
	•	Open frontend/index.html in browser → interact with frontend

With Dockers
docker-compose up --build
Backend → http://localhost:8000		
Frontend → http://localhost:8080

📝 Future Improvements
	•	GPT-based resume improvement suggestions
	•	Skill gap highlighting in frontend
	•	User authentication & dashboard
	•	Real PDF upload support in frontend
	•	Deploy as SaaS with CI/CD
Contact

Built by Your Name –
GitHub: https://github.com/Westbuddy1
