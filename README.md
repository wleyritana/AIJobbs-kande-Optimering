# AI Job Hunt (Lite) — English / Swedish + Module 6
A lightweight, **no-database**, **no-user-login** Flask web app that runs an AI-driven job hunting pipeline (Modules 1–8) with **language selection (English / Swedish)**, a **shared password gate**, **IP rate limiting**, and a **daily global cap**.

It is designed to be deployed publicly (e.g., Railway) without any persistence requirements.

---

## What this app does
This app helps a candidate improve their job application by:
- Scoring their CV against a job ad (recruiter lens)
- Rewriting experience (X–Y–Z bullets, without inventing metrics)
- Producing ATS risks + ATS submission CV
- Generating interview preparation
- (Optional) Comparing company branding vs employee reviews (Module 6)
- Supporting **English or Swedish** output

---

## Modules covered (1–8)
- **Module 1**: Recruiter match scoring (CV vs Job Ad)
- **Module 2**: CV optimization (experience rewrite using X–Y–Z)
- **Module 3**: ATS audit (parsing/format risks)
- **Module 4**: ATS submission CV (“ugly but deadly”)
- **Module 5**: Technical interview questions (in interview pack)
- **Module 6**: Company culture (reality vs image) *(optional inputs)*
- **Module 7**: HR/Values interview questions (in interview pack)
- **Module 8**: Candidate questions to ask employer (in interview pack)

---

## Key features
- ✅ No database dependency
- ✅ No account/login system
- ✅ Shared password “unlock” gate (cookie session)
- ✅ IP rate limiting
- ✅ Daily run cap (default 20/day per instance)
- ✅ Language output selection: **English / Swedish**
- ✅ Railway-ready (`Procfile`, `railway.json`, `runtime.txt`)

---

## Environment variables
Set these in Railway (or `.env` locally):

- `OPENAI_API_KEY` **(required)**
- `OPENAI_MODEL` *(optional)* default: `gpt-4.1-mini`
- `SECRET_KEY` **(required)** for Flask session signing
- `ACCESS_PASSWORD` **(required)** shared unlock password
- `DAILY_CAP` *(optional)* default: `20`

A template is provided in `.env.example`.

---

## Run locally
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt

cp .env.example .env
# edit .env and set OPENAI_API_KEY, SECRET_KEY, ACCESS_PASSWORD

flask --app app run
