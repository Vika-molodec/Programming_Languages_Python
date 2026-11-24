import json
from pathlib import Path
from analysis import *

BASE = Path(__file__).resolve().parent

def read_user_id():
    while True:
        try:
            user_id = int(input('Введите положительный user_id: '))
            if user_id > 0:
                return user_id
        except ValueError:
            pass
        print('Ошибка: введите целое число больше нуля')


def save_json(path, data):
    with open(path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=2)


def main():
    try:
        with open(BASE / 'todos.json', 'r', encoding='utf-8') as file:
            todos = json.load(file)
        validate_todos(todos)
    except FileNotFoundError:
        print('Ошибка: файл todos.json не найден')
        return
    except UnicodeError as error:
        print(f'Ошибка кодировки входного файла: {error}')
        return
    except json.JSONDecodeError as error:
        print(f'Ошибка формата JSON: {error}')
        return
    except ValueError as error:
        print(f'Ошибка структуры данных: {error}')
        return
    except OSError as error:
        print(f'Ошибка чтения файла: {error}')
        return

    counts = completion_counts(todos)
    leaders = top_users(counts)
    selected_leaders = leader_tasks(todos, leaders)
    print('Количество выполненных задач:', counts)
    print('Лидеры:', leaders)
    print('ID завершённых задач лидеров:', [task['id'] for task in selected_leaders])
    user_id = read_user_id()
    selected = select_tasks(todos, user_id)
    print(f'Задачи пользователя {user_id}:', [task['id'] for task in selected])
    try:
        save_json(BASE / 'leaders.json', selected_leaders)
        save_json(BASE / 'selected.json', selected)
        print('Результаты записаны в leaders.json и selected.json')
    except (OSError, UnicodeError, TypeError, ValueError) as error:
        print(f'Ошибка сохранения результатов: {error}')


if __name__ == '__main__':
    main()
