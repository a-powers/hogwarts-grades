student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

new_grades = {}

for student in student_scores:
    score = student_scores[student]
    if score > 90:
        new_grades[student] = "Outstanding"
    elif score > 80:
        new_grades[student] = "Exceeds Average"
    elif score > 70:
        new_grades[student] = "Averge"
    elif score <= 70:
        new_grades[student] = "Below Average"

print(new_grades)