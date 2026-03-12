# Grade Tracker - Session 1 (Extended)
# By Fred (fredjayson348-art)

subjects = []
scores = []

print("=== Student Grade Tracker ===")
print("Enter your subjects and scores.")
print("Type 'done' when finished.\n")

# Loop to collect multiple subjects
while True:
    subject = input("Enter subject name (or 'done' to stop): ")
    
    if subject.lower() == "done":
        break
    
    score = float(input("Enter score for " + subject + ": "))
    
    subjects.append(subject)
    scores.append(score)
    print("✓ Added!\n")

# Display all grades
print("\n--- Your Grades ---")
for i in range(len(subjects)):
    print(subjects[i], ":", scores[i])

# Calculate average
total = sum(scores)
average = total / len(scores)
print("\nAverage Score:", average)
