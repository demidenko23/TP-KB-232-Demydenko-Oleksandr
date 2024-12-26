import logging

class Calculator:
    @staticmethod
    def add(a, b):
        result = a + b
        logging.info(f'Операція: додавання, Числа: {a}, {b}, Результат: {result}')
        return result

    @staticmethod
    def sub(a, b):
        result = a - b
        logging.info(f'Операція: віднімання, Числа: {a}, {b}, Результат: {result}')
        return result

    @staticmethod
    def mul(a, b):
        result = a * b
        logging.info(f'Операція: множення, Числа: {a}, {b}, Результат: {result}')
        return result

    @staticmethod
    def div(a, b):
        try:
            if b == 0:
                raise ZeroDivisionError("Помилка: ділення на нуль неможливе!")
            result = a / b
            logging.info(f'Операція: ділення, Числа: {a}, {b}, Результат: {result}')
            return result
        except ZeroDivisionError as e:
            logging.error(f'Операція: ділення, Числа: {a}, {b}, Помилка: {e}')
            return str(e)

