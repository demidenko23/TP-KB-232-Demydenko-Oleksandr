def test_dict_functions():
    print("Тестування функцій словників")

    my_dict = {"a": 1, "b": 2, "c": 3}
    print(f"Початковий словник: {my_dict}")

    my_dict.update({"d": 4, "e": 5})
    print(f"Після оновлення : {my_dict}")

    if "b" in my_dict:
        del my_dict["b"]
        print(f"Після видалення ключа 'b' : {my_dict}")
    else:
        print("Ключ 'b' відсутній у словнику, тому його не можна видалити.")

    copy_of_dict = my_dict.copy()  
    my_dict.clear()
    print(f"Після очищення : {my_dict}")

    print(f"Ключі словника : {copy_of_dict.keys()}")

    print(f"Значення словника : {copy_of_dict.values()}")

    print(f"Пари ключ-значення : {copy_of_dict.items()}")

test_dict_functions()