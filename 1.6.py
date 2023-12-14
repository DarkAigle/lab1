def find_min_even_element(tuple):
    min_even = None
    for element in tuple:
        if element % 2 == 0:
            if min_even is None or element < min_even:
                min_even = element
    if min_even is not None:
        return min_even
    else:
        return tuple[0]
my_tuple = (3, 7, 2, 8, 5, 10)
result = find_min_even_element(my_tuple)
print("Наименьший чётный элемент", result)