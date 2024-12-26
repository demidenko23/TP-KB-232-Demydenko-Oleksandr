def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    try:
        if b == 0:
            raise ZeroDivisionError("Помилка: ділення на нуль неможливе!")
        return a / b
    except ZeroDivisionError as e:
        return str(e)

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Помилка: введено нечислове значення! Спробуйте ще раз.")

def calculator():
    while True:
        print("\nОбери операцію:")
        print("1. Додавання")
        print("2. Віднімання")
        print("3. Множення")
        print("4. Ділення")
        print("5. Вихід")
        
        operation = input("Введіть номер операції (1/2/3/4/5): ")

        if operation == '5':
            print("Програма завершена.")
            break

        num1 = get_number("Введіть перше число: ")
        num2 = get_number("Введіть друге число: ")

        match operation:
            case '1':
                print(f"Результат: {add(num1, num2)}")
            case '2':
                print(f"Результат: {sub(num1, num2)}")
            case '3':
                print(f"Результат: {mul(num1, num2)}")
            case '4':
                print(f"Результат: {div(num1, num2)}")
            case _:
                print("Помилка: недійсна операція!")

calculator()
