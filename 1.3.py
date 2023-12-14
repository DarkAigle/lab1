def sum_positive_elements(lst):

    positive_sum = sum(x for x in lst if x > 0)
    return positive_sum

def sum_between_zeros(lst):

    try:
        first_zero_index = lst.index(0)
        second_zero_index = lst.index(0, first_zero_index + 1)
        sum_between = sum(lst[first_zero_index + 1:second_zero_index])
        return sum_between
    except ValueError:
        return 0


my_list = [1, 52, 33, -14, 0, 55, 26, 0, 17, 81, 39]
positive_sum_result = sum_positive_elements(my_list)
sum_between_zeros_result = sum_between_zeros(my_list)

print(f"Сумма положительных элементов: {positive_sum_result}")
print(f"Сумма элементов между двумя первыми нулями: {sum_between_zeros_result}")