numbers = [1.5, -9.0, 3.3, -3.7, 5.2, 6.1, -7.5, 8.0, 9.6, -10.4]

sum_of_negatives = 0

for number in numbers:
    if number < 0:
        sum_of_negatives += number

print("Сумма отрицательных элементов:", sum_of_negatives)