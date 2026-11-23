from pathlib import*
from files_lab import*
from table import*

#Задание 1 
def read_positive_integer():
    while True:
        try:
            number = int(input('Введите положительное целое число: '))
        except ValueError:
            print('Ошибка: не целое число')
            continue
        if number <= 0:
            print('Ошибка: должно быть больше нуля')
            continue
        return number

#Задание 3
def create_report(source, destination):
    # Сначала полностью читаем и проверяем входной файл.
    matrix = read_matrix(source)
    rows = row_sums(matrix)
    columns = column_sums(matrix)
    result = selected_sum(matrix)

    report = (
        'Суммы строк: ' + ' '.join(map(str, rows)) + '\n'
        + 'Суммы столбцов: ' + ' '.join(map(str, columns)) + '\n'
        + f'Результат варианта: {result}\n'
    )
    # Запись начинается только после успешной проверки данных.
    with open(destination, 'w', encoding='utf-8') as file:
        file.write(report)
    return report


def main():
    print('Задание 1. Надёжный ввод размера')
    size = read_positive_integer()
    print('Введённое число:', size)

    print('\nЗадания 2–3. Чтение таблицы и создание отчёта')
    folder = Path(__file__).resolve().parent
    try:
        create_report(folder / 'matrix.txt', folder / 'report.txt')
    except FileNotFoundError:
        print('Ошибка: файл matrix.txt не найден')
    except ValueError as error:
        print('Ошибка формата:', error)
    except UnicodeError:
        print('Ошибка: файл имеет неверную кодировку')
    except OSError as error:
        print('Ошибка доступа к файлу:', error)
    else:
        print('Отчёт успешно записан в report.txt')


if __name__ == '__main__':
    main()
