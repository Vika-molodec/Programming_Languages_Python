# Лабораторная работа №9. Вариант 1 — таблицы.(функции без ввода и вывода)

# Задание 1. Суммы строк
def row_sums(matrix):
    result = []
    for row in matrix:
        result.append(sum(row))
    return result

# Задание 2. Суммы столбцов
def column_sums(matrix):
    if not matrix:
        return []
    result = []
    for column in range(len(matrix[0])):
        total = 0
        for row in matrix:
            total += row[column]
        result.append(total)
    return result

# Задание 3. Диагональный узор
def diagonal_pattern(size):
    matrix = []
    for row in range(size):
        new_row = []
        for column in range(size):
            if row == column:
                new_row.append(0)
            elif row < column:
                new_row.append(1)
            else:
                new_row.append(2)
        matrix.append(new_row)
    return matrix

# Индивидуальный вариант 1. Отрицательные заменить нулями
def transform(matrix):
    result = []
    for row in matrix:
        new_row = []
        for number in row:
            if number < 0:
                new_row.append(0)
            else:
                new_row.append(number)
        result.append(new_row)
    return result
