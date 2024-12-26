def test_list_functions():
    print("Тестування функцій списків")

    my_list = [1, 5, 3, 4, 8]
    print(f"Початковий список: {my_list}")

    my_list.append(10)
    print(f"Після додавання (10): {my_list}")

    my_list.extend([4, 9])
    print(f"Після розширення ([4, 9]): {my_list}")

    my_list.insert(2, 6)
    print(f"Після вставки (2, 6): {my_list}")

    if 9 in my_list:
        my_list.remove(9)
        print(f"Після видалення (9): {my_list}")
    else:
        print("Елемент 9 відсутній у списку, тому його не можна видалити.")

    copy_of_list = my_list.copy()  
    my_list.clear()
    print(f"Після очищення(): {my_list}")

    copy_of_list.sort()
    print(f"Після сортування (): {copy_of_list}")

    copy_of_list.reverse()
    print(f"Після реверсу (): {copy_of_list}")

    new_list = copy_of_list.copy()
    print(f"Копія списку: {new_list}")

test_list_functions()
