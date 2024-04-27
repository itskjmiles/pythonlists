students = ["John", "Doe", "Jane", "Smith"]
grades = [85, 90, 78, 88]
activity = ["Football", "Music", "Art", "Dance"]

# Task 1: 
for student, grade, activity in zip(students, grades, activity):
    if grade < 80:
        print(f"{student}, {grade}, {activity}")

# Task 2:
students_approved = [student for student, grade in zip(students, grades) if grade >= 80]

# Task 3: 
print("Students approved:", students_approved)
