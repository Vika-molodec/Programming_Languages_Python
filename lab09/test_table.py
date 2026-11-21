from table import*

# Задание 1. Суммы строк
assert row_sums([[1, 2, 3], [4, 5, 6]]) == [6, 15]
assert row_sums([[7]]) == [7]
assert row_sums([[1], [-1], [0]]) == [1, -1, 0]
assert row_sums([]) == []

# Задание 2. Суммы столбцов
assert column_sums([[1, 2, 3], [4, 5, 6]]) == [5, 7, 9]
assert column_sums([[7]]) == [7]
assert column_sums([[1], [-1], [0]]) == [0]
assert column_sums([]) == []

# Задание 3. Диагональный узор
assert diagonal_pattern(1) == [[0]]
assert diagonal_pattern(3) == [[0, 1, 1], [2, 0, 1], [2, 2, 0]]

# Индивидуальный вариант 1. Отрицательные заменить нулями
matrix = [[-2, 0, 3], [4, -5, 6]]
result = transform(matrix)
assert result == [[0, 0, 3], [4, 0, 6]]
assert transform([]) == []
assert matrix == [[-2, 0, 3], [4, -5, 6]]

# Новая таблица не должна разделять строки с исходной
result[0][0] = 100
assert matrix[0][0] == -2
assert result[0][0] == 100

# Входная матрица не меняется при расчёте сумм
original = [[1, 2, 3], [4, 5, 6]]
row_sums(original)
column_sums(original)
assert original == [[1, 2, 3], [4, 5, 6]]

print('Все проверки пройдены!')
