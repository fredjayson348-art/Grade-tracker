# Grade Tracker - Session 2: Menu + Functions
# By Fred (fredjayson348-art)

subjects = []
scores = []

def add_subject():
    subject = input("Enter subject name: ")
    score = float(input("Enter score for " + subject + ": "))
    subjects.append(subject)
    scores.append(score)
    print("✓ Added!\n")

def show_grades():
    if len(subjects) == 0:
        print("No grades added yet!\n")
        return
    print("\n--- Your Grades ---")
    for i in range(len(subjects)):
        print(subjects[i], ":", scores[i])
    print()

def calculate_average():
    if len(scores) == 0:
        print("No scores yet!\n")
        return
    average = sum(scores) / len(scores)
    print("Average Score:", average, "\n")

def show_menu():
    print("=== Student Grade Tracker ===")
    print("1. Add subject")
    print("2. View grades")
    print("3. Calculate average")
    print("4. Quit")

# --- Main Program ---
while True:
    show_menu()
    choice = input("Choose an option (1-4): ")

    if choice == "1":
        add_subject()
    elif choice == "2":
        show_grades()
    elif choice == "3":
        calculate_average()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid option, try again!\n")
