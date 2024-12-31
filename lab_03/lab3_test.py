import unittest
from student import Student
from student_list import StudentList

class TestStudentList(unittest.TestCase):
    def setUp(self):
        self.student_list = StudentList()
        self.student1 = Student("Alice", "0631234567", "alice@example.com", 20)
        self.student2 = Student("Bob", "0637654321", "bob@example.com", 22)
        self.student_list.add_student(self.student1)
        self.student_list.add_student(self.student2)

    def test_add_student(self):
        self.assertEqual(len(self.student_list.list_students()), 2)

    def test_delete_student(self):
        self.assertTrue(self.student_list.delete_student("Alice"))
        self.assertEqual(len(self.student_list.list_students()), 1)

    def test_update_student(self):
        updated_student = Student("Alice", "0639876543", "alice_new@example.com", 21)
        self.assertTrue(self.student_list.update_student("Alice", updated_student))
        self.assertEqual(self.student_list.list_students()[0].email, "alice_new@example.com")

if __name__ == "__main__":
    unittest.main()
