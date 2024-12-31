import sys
from student_list import StudentList
from Utils import Utils

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <filename>")
        return

    file_name = sys.argv[1]
    student_list = StudentList()

    # Завантаження даних
    Utils.load_from_csv(file_name, student_list)

    while True:
        print("\nOptions: [C]reate, [U]pdate, [D]elete, [P]rint, [X] Exit")
        choice = input("Choose an option: ").upper()
        if choice == 'C':
            student_list.add_student()
        elif choice == 'U':
            student_list.update_student()
        elif choice == 'D':
            student_list.delete_student()
        elif choice == 'P':
            student_list.print_all()
        elif choice == 'X':
            Utils.save_to_csv(file_name, student_list)
            print("Exiting...")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
