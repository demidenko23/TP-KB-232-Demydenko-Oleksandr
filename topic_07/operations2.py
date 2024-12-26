import logging
from functions2 import Calculator

logging.basicConfig(filename='calculator.log', level=logging.INFO, format='%(asctime)s - %(message)s')

class CalculatorApp:
    def __init__(self):
        logging.info("Запуск калькулятора")
    
    @staticmethod
    def get_number(prompt):
        while True:
            try:
                number = float(input(prompt))
                logging.info(f'Введено число: {number}')
                return number
            except ValueError:
                print("Помилка: введено нечислове значення! Спробуйте ще раз.")
                logging.error('Введено нечислове значення')

    def run(self):
        while True:
            print("\n Обери операцію:")
            print("1. Додавання")
            print("2. Віднімання")
            print("3. Множення")
            print("4. Ділення")
            print("5. Вихід")

            operation = input("Введіть номер операції (1/2/3/4/5): ")
            logging.info(f'Користувач вибрав операцію: {operation}')

            if operation == '5':
                print("Програма завершена.")
                logging.info("Програма завершена")
                break

            num1 = self.get_number("Введіть перше число: ")
            num2 = self.get_number("Введіть друге число: ")

            match operation:
                case '1':
                    print(f"Результат: {Calculator.add(num1, num2)}")
                case '2':
                    print(f"Результат: {Calculator.sub(num1, num2)}")
                case '3':
                    print(f"Результат: {Calculator.mul(num1, num2)}")
                case '4':
                    print(f"Результат: {Calculator.div(num1, num2)}")
                case _:
                    print("Помилка: недійсна операція!")
                    logging.error(f'Невірний номер операції: {operation}')
