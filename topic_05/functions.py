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
