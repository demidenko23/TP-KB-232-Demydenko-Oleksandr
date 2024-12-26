class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Student(name={self.name}, age={self.age})"


students = [
    Student("Олександр", 19),
    Student("Іван", 20),
    Student("Катерина", 18),
    Student("Дмитро", 21),
]

sorted_students = sorted(students, key=lambda student: student.age)

print("Список студентів, відсортований за віком:")
for student in sorted_students:
    print(student)
