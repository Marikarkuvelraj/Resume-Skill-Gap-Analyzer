from flask import Flask, jsonify, render_template, request
import skill_gap_analyzer as sga

app = Flask(__name__, static_folder="static", template_folder="templates")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/job_roles")
def job_roles():
    return jsonify(sga.list_job_roles())


@app.route("/api/job_role")
def job_role_details():
    job_role = request.args.get("job_role", "").strip()
    if not job_role:
        return jsonify({"error": "job_role is required."}), 400
    try:
        skills = sga.get_role_skills(job_role)
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    return jsonify({"job_role": job_role.title(), "skills": skills})


@app.route("/api/analyze", methods=["POST"])
def analyze():
    data = request.get_json() or {}
    resume_text = data.get("resume_text", "").strip()
    job_role = data.get("job_role", "").strip()
    if not resume_text or not job_role:
        return jsonify({"error": "Both resume_text and job_role are required."}), 400
    try:
        report = sga.analyze_resume(resume_text, job_role)
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    return jsonify(report)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
