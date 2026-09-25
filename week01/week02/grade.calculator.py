students = []
scores = []

while True:
    name = input("Enter student name (or q to quit): ")

    if name == "q":
        break

    score = float(input("Enter score: "))

    if score < 0 or score > 100:
        print("Invalid score. Please enter a number between 0 and 100.")
        continue

    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"

    print(f"{name}: {score:g} -> {grade}")

    students.append(name)
    scores.append(score)

if len(students) == 0:
    print("No students entered.")
else:
    average = sum(scores) / len(scores)

    print(f"Total students: {len(students)}")
    print(f"Average score: {average:.2f}")
