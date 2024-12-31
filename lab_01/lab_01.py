students = [
    {"name": "Bob", "phone": "0631234567", "email": "bob@example.com", "age": 20},
    {"name": "Emma", "phone": "0631234567", "email": "emma@example.com", "age": 22},
    {"name": "Jon", "phone": "0631234567", "email": "jon@example.com", "age": 21},
    {"name": "Zak", "phone": "0631234567", "email": "zak@example.com", "age": 23}
]

def printAllList():
    for student in students:
        strForPrint = (
            f"Student name: {student['name']}, Phone: {student['phone']}, "
            f"Email: {student['email']}, Age: {student['age']}"
        )
        print(strForPrint)
    return

def addNewElement():
    name = input("Please enter student name: ")
    phone = input("Please enter student phone: ")
    email = input("Please enter student email: ")
    age = int(input("Please enter student age: "))

    newItem = {"name": name, "phone": phone, "email": email, "age": age}
    insertPosition = 0
    for student in students:
        if name > student["name"]:
            insertPosition += 1
        else:
            break
    students.insert(insertPosition, newItem)
    print("New element has been added.")
    return

def deleteElement():
    name = input("Please enter name to be deleted: ")
    deletePosition = -1
    for student in students:
        if name == student["name"]:
            deletePosition = students.index(student)
            break
    if deletePosition == -1:
        print("Element was not found.")
    else:
        del students[deletePosition]
        print(f"Student '{name}' has been deleted.")
    return

def updateElement():
    name = input("Please enter the name of the student to be updated: ")
    for student in students:
        if name == student["name"]:
            print(f"Current data: {student}")
            new_name = input("Enter new name (or press Enter to keep the current): ") or student["name"]
            new_phone = input("Enter new phone (or press Enter to keep the current): ") or student["phone"]
            new_email = input("Enter new email (or press Enter to keep the current): ") or student["email"]
            new_age = input("Enter new age (or press Enter to keep the current): ")
            new_age = int(new_age) if new_age else student["age"]

            students.remove(student)
            updated_student = {"name": new_name, "phone": new_phone, "email": new_email, "age": new_age}
            insertPosition = 0
            for s in students:
                if new_name > s["name"]:
                    insertPosition += 1
                else:
                    break
            students.insert(insertPosition, updated_student)
            print("Student information has been updated.")
            return

    print("Student not found.")
    return

def main():
    while True:
        choice = input("Please specify the action [C create, U update, D delete, P print, X exit]: ")
        match choice:
            case "C" | "c":
                print("New element will be created:")
                addNewElement()
                printAllList()
            case "U" | "u":
                print("Existing element will be updated.")
                updateElement()
                printAllList()
            case "D" | "d":
                print("Element will be deleted.")
                deleteElement()
                printAllList()
            case "P" | "p":
                print("List will be printed.")
                printAllList()
            case "X" | "x":
                print("Exiting...")
                break
            case _:
                print("Wrong choice.")

main()
