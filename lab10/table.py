# Функции для работы с таблицами (аналог функций из лабораторной №9).
def row_sums(matrix):
    return [sum(row) for row in matrix]
def column_sums(matrix):
    if not matrix:
        return []
    return [sum(row[column] for row in matrix) for column in range(len(matrix[0]))]
