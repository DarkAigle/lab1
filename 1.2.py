def count_case_pairs(word):
    upper_pairs = 0
    lower_pairs = 0
    in_upper = False
    in_lower = False

    for char in word:
        if char.isupper():
            if not in_upper:
                upper_pairs += 1
            in_upper = not in_upper
        elif char.islower():
            if not in_lower:
                lower_pairs += 1
            in_lower = not in_lower

    total_letters = sum(c.isalpha() for c in word)

    return upper_pairs, lower_pairs, total_letters

word = input("Введите слово: ")

#Подсчитываем пары и общее колво букв
upper_pairs, lower_pairs, total_letters = count_case_pairs(word)

#Выводим результаты
print("Пар верхнего регистра:", upper_pairs)
print("Пар нижнего регистра:", lower_pairs)
print("Общее количество букв:", total_letters)