students = [
    {"name": "Олександр", "grade": 85},
    {"name": "Марія", "grade": 55},
    {"name": "Іван", "grade": 78},
    {"name": "Катерина", "grade": 88},
]

sorted_by_name = sorted(students, key=lambda student: student["name"])

sorted_by_grade = sorted(students, key=lambda student: student["grade"])

print("Сортування за ім'ям:")
for student in sorted_by_name:
    print(student)

print("\nСортування за оцінкою:")
for student in sorted_by_grade:
    print(student)
