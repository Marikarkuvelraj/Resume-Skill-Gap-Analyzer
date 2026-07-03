# Resume Gap Analyzer

Simple full-stack app (Flask + Bootstrap) to analyze skill gaps between a resume and job roles listed in `job_roles.csv`.

## What’s new

- Web-based resume analysis interface
- Upload or paste resume text
- Select a job role and view required skills
- See matched skills, missing skills, gap percentage, and recommendations
- Download the analysis report as JSON

## Quick start (Windows)

1. Create and activate a virtual environment (recommended):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

3. Run the app:

```powershell
python app.py
```

4. Open http://127.0.0.1:5000 in your browser.

## Notes

- Keep `job_roles.csv` in the project root.
- You can still use the CLI analyzer with `python skill_gap_analyzer.py`.
