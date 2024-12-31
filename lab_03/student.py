class Student:
    def __init__(self, name, phone, email, age):
        self.name = name
        self.phone = phone
        self.email = email
        self.age = int(age)

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}, Age: {self.age}"
