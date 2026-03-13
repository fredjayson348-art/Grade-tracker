# Grade Tracker - Flask Backend + Frontend
# By Fred (fredjayson348-art)

from flask import Flask, jsonify, request, render_template
import json
import os

app = Flask(__name__)
FILENAME = os.path.join(os.path.dirname(__file__), "grades.json")

def load_grades():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as f:
            return json.load(f)
    return {}

def save_grades(grades):
    with open(FILENAME, "w") as f:
        json.dump(grades, f)

def get_letter(score):
    if score >= 80: return "A"
    elif score >= 70: return "B"
    elif score >= 60: return "C"
    elif score >= 50: return "D"
    else: return "F"

def get_gpa(score):
    if score >= 80: return 4.0
    elif score >= 70: return 3.0
    elif score >= 60: return 2.0
    elif score >= 50: return 1.0
    else: return 0.0

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/grades", methods=["GET"])
def get_grades():
    grades = load_grades()
    result = {}
    for subject, score in grades.items():
        result[subject] = {
            "score": score,
            "letter": get_letter(score),
            "gpa": get_gpa(score)
        }
    return jsonify(result)

@app.route("/grades", methods=["POST"])
def add_grade():
    data = request.get_json()
    subject = data.get("subject")
    score = data.get("score")
    if not subject or score is None:
        return jsonify({"error": "Subject and score required"}), 400
    if score < 0 or score > 100:
        return jsonify({"error": "Score must be between 0 and 100"}), 400
    grades = load_grades()
    grades[subject] = score
    save_grades(grades)
    return jsonify({"message": "Added!", "subject": subject, "score": score})

@app.route("/grades/<subject>", methods=["DELETE"])
def delete_grade(subject):
    grades = load_grades()
    if subject not in grades:
        return jsonify({"error": "Subject not found"}), 404
    del grades[subject]
    save_grades(grades)
    return jsonify({"message": "Deleted!", "subject": subject})

@app.route("/report", methods=["GET"])
def report():
    grades = load_grades()
    if not grades:
        return jsonify({"error": "No grades yet"})
    total_gpa = sum(get_gpa(s) for s in grades.values())
    average = sum(grades.values()) / len(grades)
    return jsonify({
        "average": round(average, 2),
        "gpa": round(total_gpa / len(grades), 2),
        "total_subjects": len(grades)
    })

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
