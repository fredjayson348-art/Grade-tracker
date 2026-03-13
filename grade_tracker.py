# Grade Tracker - Session 5: Exception Handling
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

def show_grades(grades):
    if len(grades) == 0:
        print("No grades added yet!\n")
        return
    print("\n--- Your Grades ---")
    for subject, score in grades.items():
        print(subject, ":", score)
    print()

def calculate_average(grades):
    if len(grades) == 0:
        print("No scores yet!\n")
        return
    average = sum(grades.values()) / len(grades)
    print("Average Score:", round(average, 2), "\n")

def show_menu():
    print("=== Student Grade Tracker ===")
    print("1. Add subject")
    print("2. View grades")
    print("3. Calculate average")
    print("4. Quit")

# --- Main Program ---
grades = load_grades()

while True:
    show_menu()
    choice = input("Choose an option (1-4): ")
    if choice == "1":
        add_subject(grades)
    elif choice == "2":
        show_grades(grades)
    elif choice == "3":
        calculate_average(grades)
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("❌ Invalid option, try again!\n")# Grade Tracker - Session 5: Exception Handling
