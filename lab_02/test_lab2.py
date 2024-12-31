import unittest
from lab_02 import students, addNewElement, deleteElement, updateElement, load_from_csv, save_to_csv

class TestStudentDirectory(unittest.TestCase):
    def setUp(self):
        global students
        students = [
            {"name": "Bob", "phone": "0631234567", "email": "bob@example.com", "age": 20},
            {"name": "Emma", "phone": "0631234567", "email": "emma@example.com", "age": 22},
        ]

    def test_add_new_element(self):
        students.append({"name": "Zak", "phone": "0631234567", "email": "zak@example.com", "age": 23})
        self.assertEqual(len(students), 3)

    def test_delete_element(self):
        deleteElement()
        self.assertEqual(len(students), 1)

    def test_update_element(self):
        updateElement()
        self.assertEqual(students[0]["name"], "UpdatedName")

    def test_load_from_csv(self):
        load_from_csv("lab2.csv")
        self.assertGreater(len(students), 0)

    def test_save_to_csv(self):
        save_to_csv("test_output.csv")
        with open("test_output.csv", mode='r', encoding='utf-8') as file:
            content = file.read()
            self.assertIn("Bob", content)

if __name__ == "__main__":
    unittest.main()
