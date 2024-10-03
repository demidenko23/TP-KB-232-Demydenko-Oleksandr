def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b != 0:
        return a / b
    else:
        return "Помилка: ділення на нуль неможливе!"

def calculator():
    print("Оберіть операцію:")
    print("1. Додавання")
    print("2. Віднімання")
    print("3. Множення")
    print("4. Ділення")
    
    operation = input("Введіть номер операції (1/2/3/4): ")

    try:
        num1 = float(input("Введіть перше число: "))
        num2 = float(input("Введіть друге число: "))
    except ValueError:
        return "Помилка: введено нечислове значення!"

    if operation == '1':
        print(f"Результат: {add(num1, num2)}")
    elif operation == '2':
        print(f"Результат: {sub(num1, num2)}")
    elif operation == '3':
        print(f"Результат: {mul(num1, num2)}")
    elif operation == '4':
        print(f"Результат: {div(num1, num2)}")
    else:
        print("Помилка: недійсна операція!")

calculator()