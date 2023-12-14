number = input("Введите число: ")

even_count = 0
odd_count = 0

for digit in number:

    digit = int(digit)

    if digit % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Количество четных цифр:", even_count)
print("Количество нечетных цифр:", odd_count)