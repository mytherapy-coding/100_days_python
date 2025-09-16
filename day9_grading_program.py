student_scores = {"Harry": 88, "Ron": 78, "Hermione": 95, "Draco": 75, "Neville": 60}

student_grades = {}

for s, score in student_scores.items():
    if 91 <= score <= 100:
        student_grades[s] = "Outstanding"
    elif 81 <= score <= 90:
        student_grades[s] = "Exceeds Expectations"
    elif 71 <= score <= 80:
        student_grades[s] = "Acceptable"
    else:  # anything <= 70
        student_grades[s] = "Fail"

print(student_grades)
