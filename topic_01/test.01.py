input_string = "abcdefg123"

def transform_string(input_str, length=10):
    if len(input_str) > length:
        input_str = input_str[:length]
    elif len(input_str) < length:
        input_str = input_str.ljust(length, '0')
    
    return input_str[::-1]

transformed_string = transform_string(input_string)
print(transformed_string)