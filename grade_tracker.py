# Grade Tracker - Session 6: Final Version
# By Fred (fredjayson348-art)

import json

FILENAME = "grades.json"

def load_grades():
    try:
        with open(FILENAME, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_grades(grades):
    with open(FILENAME, "w") as f:
        json.dump(grades, f)

def get_letter(score):
    if score >= 80:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 60:
        return "C"
    elif score >= 50:
        return "D"
    else:
        return "F"

def get_gpa(score):
    if score >= 80:
        return 4.0
    elif score >= 70:
        return 3.0
    elif score >= 60:
        return 2.0
    elif score >= 50:
        return 1.0
    else:
        return 0.0

def add_subject(grades):
    subject = input("Enter subject name: ")
    if subject.strip() == "":
        print("❌ Subject name cannot be empty!\n")
        return
    try:
        score = float(input("Enter score for " + subject + ": "))
        if score < 0 or score > 100:
            print("❌ Score must be between 0 and 100!\n")
            return
        grades[subject] = score
        save_grades(grades)
        print("✓ Added and saved!\n")
    except ValueError:
        print("❌ Invalid score! Please enter a number.\n")

def delete_subject(grades):
    if len(grades) == 0:
        print("No grades to delete!\n")
        return
    show_grades(grades)
    subject = input("Enter subject name to delete: ")
    if subject in grades:
        del grades[subject]
        save_grades(grades)
        print("✓ Deleted successfully!\n")
    else:
        print("❌ Subject not found!\n")

def show_grades(grades):
    if len(grades) == 0:
        print("No grades added yet!\n")
        return
    print("\n--- Your Grades ---")
    for subject, score in grades.items():
        letter = get_letter(score)
        print(subject, ":", score, "("+letter+")")
    print()

def show_report(grades):
    if len(grades) == 0:
        print("No grades yet!\n")
        return
    print("\n====== FULL REPORT ======")
    total_gpa = 0
    for subject, score in grades.items():
        letter = get_letter(score)
        gpa = get_gpa(score)
        total_gpa += gpa
        print(subject, ":", score, "| Grade:", letter, "| GPA:", gpa)
    average = sum(grades.values()) / len(grades)
    final_gpa = round(total_gpa / len(grades), 2)
    print("-------------------------")
    print("Average Score :", round(average, 2))
    print("Final GPA     :", final_gpa)
    print("=========================\n")

def show_menu():
    print("=== Student Grade Tracker ===")
    print("1. Add subject")
    print("2. View grades")
    print("3. Calculate average")
    print("4. Delete subject")
    print("5. Full report")
    print("6. Quit")

# --- Main Program ---
grades = load_grades()

while True:
    show_menu()
    choice = input("Choose an option (1-6): ")
    if choice == "1":
        add_subject(grades)
    elif choice == "2":
        show_grades(grades)
    elif choice == "3":
        average = sum(grades.values()) / len(grades) if grades else 0
        print("Average Score:", round(average, 2), "\n")
    elif choice == "4":
        delete_subject(grades)
    elif choice == "5":
        show_report(grades)
    elif choice == "6":
        print("Goodbye! Keep studying hard! 📚")
        break
    else:
        print("❌ Invalid option, try again!\n")
