from student import Student

class StudentList:
    def __init__(self):
        self.students = []

    def add_student(self):
        name = input("Enter name: ")
        phone = input("Enter phone: ")
        email = input("Enter email: ")
        age = input("Enter age: ")
        self.students.append(Student(name, phone, email, age))
        print("Student added successfully.")

    def update_student(self):
        name = input("Enter the name of the student to update: ")
        for student in self.students:
            if student.name == name:
                print(f"Current data: {student}")
                student.name = input("New name (or press Enter to keep): ") or student.name
                student.phone = input("New phone (or press Enter to keep): ") or student.phone
                student.email = input("New email (or press Enter to keep): ") or student.email
                new_age = input("New age (or press Enter to keep): ")
                student.age = int(new_age) if new_age else student.age
                print("Student updated successfully.")
                return
        print("Student not found.")

    def delete_student(self):
        name = input("Enter the name of the student to delete: ")
        for student in self.students:
            if student.name == name:
                self.students.remove(student)
                print(f"Student {name} deleted successfully.")
                return
        print("Student not found.")

    def print_all(self):
        if not self.students:
            print("No students in the list.")
        else:
            for student in self.students:
                print(student)
