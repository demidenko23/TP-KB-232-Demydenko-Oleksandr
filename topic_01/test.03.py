def discriminant(a, b, c):
    result = b**2 - 4*a*c
    return result

# Введення коефіцієнтів від користувача
a = float(input("Введіть коефіцієнт a: "))
b = float(input("Введіть коефіцієнт b: "))
c = float(input("Введіть коефіцієнт c: "))

result = discriminant(a, b, c)


print(f"Дискримінант рівняння {a}x^2 + {b}x + {c} = 0 дорівнює {result}")
