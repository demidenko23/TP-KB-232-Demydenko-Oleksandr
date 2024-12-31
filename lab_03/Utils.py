import csv
from student import Student

class Utils:
    @staticmethod
    def load_from_csv(file_name, student_list):
        try:
            with open(file_name, mode='r', newline='') as file:
                reader = csv.reader(file)
                next(reader)  # Пропускаємо заголовки
                for row in reader:
                    student_list.students.append(Student(*row))
            print("Data loaded successfully.")
        except FileNotFoundError:
            print(f"File {file_name} not found. Starting with an empty list.")

    @staticmethod
    def save_to_csv(file_name, student_list):
        with open(file_name, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["name", "phone", "email", "age"])
            for student in student_list.students:
                writer.writerow([student.name, student.phone, student.email, student.age])
        print("Data saved successfully.")
