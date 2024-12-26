
def find_insert_position(sorted_list, new_element):
    left, right = 0, len(sorted_list)
    while left < right:
        mid = (left + right) // 2
        if sorted_list[mid] < new_element:
            left = mid + 1
        else:
            right = mid
    return left

sorted_list = [1, 3, 5, 7, 9]
new_element = 0
position = find_insert_position(sorted_list, new_element)
print(f"Позиція для вставки елементу {new_element}: {position}")

sorted_list.insert(position, new_element)
print(f"Список після вставки: {sorted_list}")
