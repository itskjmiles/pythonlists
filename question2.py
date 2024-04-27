submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

# Task 1
both_submitted_and_attended = [student for student in submitted if student in attended]
print("Students who both submitted assignments and attended the class:", both_submitted_and_attended)

# Task 2
are_identical = sorted(submitted) == sorted(attended)
print("Are the two lists identical?:", are_identical)

# Task 3
attended = [student for student in attended if student in submitted]
print("Attendee list", attended)
