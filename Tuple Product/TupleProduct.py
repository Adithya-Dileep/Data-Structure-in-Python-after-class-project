def multiply_tuple_elements(tuple)
    result = 1
    for i in tuple:
        result = result * i
    return result
my_tuple = (2,  3,  4,  5)
print(multiply_tuple_elements(my_tuple))