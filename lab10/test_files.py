from pathlib import Path
from tempfile import TemporaryDirectory
from unittest.mock import patch

from files_lab import read_matrix, selected_sum
from main import create_report, read_positive_integer
from table import row_sums, column_sums

def check_invalid(path, content, line_number=None):
    path.write_text(content, encoding='utf-8')
    try:
        read_matrix(path)
    except ValueError as error:
        if line_number is not None:
            assert f'Строка {line_number}' in str(error), str(error)
    else:
        assert False, 'Ошибка не обнаружена'


def run_tests():
    with TemporaryDirectory() as directory:
        path = Path(directory) / 'matrix.txt'
        report = Path(directory) / 'report.txt'

        path.write_text('1 2\n7 -1\n', encoding='utf-8')
        assert read_matrix(path) == [[7, -1]]
        path.write_text('1 1\n0\n', encoding='utf-8')
        assert read_matrix(path) == [[0]]
        check_invalid(path, '')
        check_invalid(path, '0 3\n')
        check_invalid(path, '1 2\n1\n', 2)
        check_invalid(path, '1 2\n1 x\n', 2)
        check_invalid(path, '1 1\n7\n8\n', 3)
        check_invalid(path, '1 1\n7\n\n', 3)
        check_invalid(path, '2 1\n1\n', 3)
        check_invalid(path, 'a b\n1\n', 1)
        check_invalid(path, '1 1\n\n', 2)
        path.unlink()
        try:
            read_matrix(path)
        except FileNotFoundError:
            pass
        else:
            assert False, 'Не обнаружен отсутствующий файл'

        # Проверяем сохранность старого отчёта при неверном входе.
        report.write_text('Старый отчёт\n', encoding='utf-8')
        path.write_text('1 2\n1 x\n', encoding='utf-8')
        try:
            create_report(path, report)
        except ValueError:
            pass
        else:
            assert False, 'Ошибка не обнаружена'
        assert report.read_text(encoding='utf-8') == 'Старый отчёт\n'

        path.write_text('2 3\n1 -2 3\n4 0 -6\n', encoding='utf-8')
        create_report(path, report)
        assert report.read_text(encoding='utf-8') == (
            'Суммы строк: 2 -2\n'
            'Суммы столбцов: 5 -2 -3\n'
            'Результат варианта: 8\n'
        )
        matrix = read_matrix(path)
        assert row_sums(matrix) == [2, -2]
        assert column_sums(matrix) == [5, -2, -3]
        assert selected_sum(matrix) == 8
        assert selected_sum([[0, -1], [-2, 0]]) == 0
        assert selected_sum([[4]]) == 4
        assert selected_sum([[1, 2, -3]]) == 3

    with patch('builtins.input', side_effect=['abc', '0', '-2', '3']):
        assert read_positive_integer() == 3
    print('Все проверки пройдены')


if __name__ == '__main__':
    run_tests()
