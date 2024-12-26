import logging

# Налаштування логування
logging.basicConfig(filename='calculator.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def add(a, b):
    result = a + b
    logging.info(f'Операція: додавання, Числа: {a}, {b}, Результат: {result}')
    return result

def sub(a, b):
    result = a - b
    logging.info(f'Операція: віднімання, Числа: {a}, {b}, Результат: {result}')
    return result

def mul(a, b):
    result = a * b
    logging.info(f'Операція: множення, Числа: {a}, {b}, Результат: {result}')
    return result

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
