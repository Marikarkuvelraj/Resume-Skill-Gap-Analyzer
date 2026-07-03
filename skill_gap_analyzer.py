import pandas as pd
import re
from typing import Dict, List, Set


def load_job_roles(csv_path: str = "job_roles.csv") -> pd.DataFrame:
    rows = []
    with open(csv_path, encoding="utf-8") as f:
        for line in f:
            text = line.strip().strip('"').strip("'")
            if not text:
                continue
            if text.lower().startswith("jobrole,") or text.lower().startswith("job_role,"):
                continue
            if "," in text:
                role_part, skills_part = text.split(",", 1)
            else:
                role_part, skills_part = text, ""
            role = role_part.strip().lower()
            skills = skills_part.strip()
            rows.append({"JobRole": role, "Skills": skills})
    df = pd.DataFrame(rows)
    return df


def list_job_roles(csv_path: str = "job_roles.csv") -> List[str]:
    try:
        df = load_job_roles(csv_path)
    except FileNotFoundError:
        return []
    roles = df["JobRole"].dropna().unique().tolist()
    return [r.title() for r in roles if isinstance(r, str)]


def get_role_skills(job_role: str, csv_path: str = "job_roles.csv") -> List[str]:
    df = load_job_roles(csv_path)
    jr = job_role.strip().lower()
    if jr not in df["JobRole"].tolist():
        raise ValueError(f"Job role '{job_role}' not found.")
    skills_raw = df.loc[df["JobRole"] == jr, "Skills"].iloc[0]
    return sorted(parse_skills(skills_raw))


def parse_skills(skills_raw: str) -> Set[str]:
    return {s.strip().lower() for s in str(skills_raw).split(",") if s.strip()}


def tokenize_resume(resume_text: str) -> Set[str]:
    tokens = re.findall(r"[A-Za-z0-9+#]+(?:\s*[A-Za-z0-9+#]+)*", resume_text.lower())
    words = set()
    for t in tokens:
        for w in t.replace("-", " ").split():
            words.add(w.strip())
    return words


def analyze_resume(resume_text: str, job_role: str, csv_path: str = "job_roles.csv") -> Dict:
    job_skills = set(get_role_skills(job_role, csv_path))
    resume_words = tokenize_resume(resume_text)
    matched = sorted(resume_words & job_skills)
    missing = sorted(job_skills - resume_words)
    total_required = len(job_skills)
    matched_count = len(matched)
    missing_count = len(missing)
    gap_percentage = round((missing_count / max(1, total_required)) * 100, 2)
    recommendations = [f"Learn {skill}" for skill in missing]
    if total_required == 0:
        tips = "No skills are defined for this role."
    elif gap_percentage == 0:
        tips = "Excellent! Your resume already covers all required skills."
    elif gap_percentage <= 30:
        tips = "Strong fit. Add a few more keywords and project details."
    else:
        tips = "Focus on the missing skills and add related experience."
    return {
        "job_role": job_role.strip().title(),
        "job_skills": sorted(job_skills),
        "total_required_skills": total_required,
        "matched_skills": matched,
        "missing_skills": missing,
        "matched_count": matched_count,
        "missing_count": missing_count,
        "gap_percentage": gap_percentage,
        "recommendations": recommendations,
        "tips": tips,
    }


if __name__ == "__main__":
    resume_text = "Python SQL Pandas Linux"
    print("Job Roles:", list_job_roles())
    job_role = input("Enter job role: ")
    result = analyze_resume(resume_text, job_role)
    print("\nOUTPUT")
    print(result)
