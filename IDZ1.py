# Ввод списка А из 10 элементов
A = []
for i in range(10):
    element = int(input(f"Введите элемент {i + 1}: "))
    A.append(element)

# Находим наибольший элемент
max_element = max(A)

# Находим индекс наибольшего элемента
max_index = A.index(max_element)

# Переставляем наибольший элемент с первым
A[0], A[max_index] = A[max_index], A[0]

# Выводим преобразованный список
print("Преобразованный список:")
print(A)
