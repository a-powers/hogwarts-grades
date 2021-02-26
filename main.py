student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}


all_grades = {}

for i in student_scores:
    grades = student_scores[i]
    if grades > 90:
        all_grades[i] = "Outstanding"
    elif grades > 80:
        all_grades[i] = "Exceeds Expectations"
    elif grades > 70:
        all_grades[i] = "Average"
    elif grades <= 70:
        all_grades[i] = "Not Passing"
print(all_grades)