from openai_client import llm_text

def _lang_instruction(lang: str) -> str:
    return "Respond entirely in Swedish." if (lang or "").lower().startswith("sv") else "Respond entirely in English."

def recruiter_match(cv: str, job_ad: str, role: str | None, lang: str) -> str:
    system = f"You are a senior recruiter. Be brutally honest and specific. No fluff. {_lang_instruction(lang)}"
    user = f"""
Role: {role or "N/A"}

Compare CV vs Job Ad. Return JSON ONLY:
{{
  "match_score": 0-100,
  "short_reason": "...",
  "top_5_gaps": ["...", "..."],
  "hireability_blockers": ["..."]
}}

CV:
{cv}

JOB AD:
{job_ad}
"""
    return llm_text(system, user)

def optimize_experience(cv: str, match_json: str, role: str | None, lang: str) -> str:
    system = f"You are a senior CV consultant. Use Google X-Y-Z. Never invent metrics. {_lang_instruction(lang)}"
    user = f"""
Role: {role or "N/A"}

Recruiter match JSON:
{match_json}

Rewrite ONLY the Professional Experience section (or equivalent).
- Integrate missing keywords naturally
- Use X-Y-Z bullets where possible
- If metrics missing, use [metric needed]

Return plain text only.

CV:
{cv}
"""
    return llm_text(system, user)

def ats_audit(cv_text: str, lang: str) -> str:
    system = f"You are an ATS (Workday/SuccessFactors). Focus on parsing risks and fixes. {_lang_instruction(lang)}"
    user = f"""
Return JSON ONLY:
{{
  "risks": [
    {{"issue":"...", "risk":"low|medium|high", "fix":"..."}}
  ]
}}

CV:
{cv_text}
"""
    return llm_text(system, user)

def ats_submission_cv(cv_text: str, lang: str) -> str:
    system = f"You generate ATS-maximized CVs. One column. Standard headings. No tables/icons. {_lang_instruction(lang)}"
    user = f"""
Create an ATS submission CV:
- One column
- Standard headings: Summary, Skills, Work Experience, Education, Certifications (if any)
- High keyword density without stuffing
- Functional over aesthetic (“ugly but deadly”)

Return plain text only.

CV:
{cv_text}
"""
    return llm_text(system, user)

def interview_pack(cv_text: str, job_ad: str, role: str | None, lang: str) -> str:
    system = f"You are a hiring manager + HR partner. Be concrete and role-specific. {_lang_instruction(lang)}"
    user = f"""
Role: {role or "N/A"}

Generate an interview pack with clear headings:

A) Technical (3):
- Question
- Perfect answer based on CV (no invented experience)
- What it tests

B) HR/Values (3):
- Question
- What HR assesses
- Strong answer tailored to CV

C) Candidate questions (3):
- Question
- Why it matters
- Green flags
- Red flags

Return plain text only.

CV:
{cv_text}

JOB AD:
{job_ad}
"""
    return llm_text(system, user)

def culture_reality_check(company_culture_text: str, employee_reviews_text: str, company_name: str | None, lang: str) -> str:
    system = f"You are a neutral culture analyst. Compare employer branding with employee reality. Be specific and balanced. {_lang_instruction(lang)}"
    user = f"""
Company: {company_name or "N/A"}

Compare:
1) Employer branding / official culture statements
2) Employee reviews (Glassdoor/Indeed style)

Return a structured report with:
- Claimed culture themes (from official text)
- Lived culture themes (from reviews)
- Alignments (where they match)
- Mismatches/contradictions (where they differ)
- Practical implications for a candidate (what to ask / watch for)
- Risk rating: low/medium/high (with justification)

If inputs are sparse, say what is missing and keep conclusions cautious.

Official culture text:
{company_culture_text}

Employee reviews:
{employee_reviews_text}
"""
    return llm_text(system, user)
