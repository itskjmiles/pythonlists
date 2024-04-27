grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]

# Task 1: 
grades = sorted(grades, reverse=True)
print("Sorted Grades:", grades)

# Task 2: 
average_grade = sum(grades) / len(grades)
print("Average Grade:", average_grade)

# Task 3: 
updated_grades = ["Failed" if grade < 80 else grade for grade in grades]
print("Updated Grades:", updated_grades)
