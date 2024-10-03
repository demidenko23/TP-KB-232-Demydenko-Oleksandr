import math

def discriminant(a, b, c):
    result = b**2 - 4*a*c
    return result

def solve_quadratic_equation(a, b, c):
    D = discriminant(a, b, c)  
    
    if D > 0:
        x1 = (-b + math.sqrt(D)) / (2 * a)
        x2 = (-b - math.sqrt(D)) / (2 * a)
        return f"Два дійсних корені: x1 = {x1}, x2 = {x2}"
    elif D == 0:
        x = -b / (2 * a)
        return f"Один дійсний корінь: x = {x}"
    else:
        return "Немає дійсних коренів."

a = float(input("Введіть коефіцієнт a: "))
b = float(input("Введіть коефіцієнт b: "))
c = float(input("Введіть коефіцієнт c: "))

result = solve_quadratic_equation(a, b, c)

print(f"Результати для рівняння {a}x^2 + {b}x + {c} = 0: {result}")
