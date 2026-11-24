from pathlib import Path
from logic import *
from storage import load_records, save_records

PATH = Path(__file__).resolve().parent / 'data.json'

def read_text(message):
    while True:
        value = input(message).strip()
        if value:
            return value
        print('Строка не должна быть пустой')

def read_number(message, minimum=0):
    while True:
        try:
            value = int(input(message))
            if value >= minimum:
                return value
        except ValueError:
            pass
        print('Введите целое число не меньше', minimum)

def show_records(records):
    if not records:
        print('Нет записей')
    for record in sorted(records, key=lambda record: record['id']):
        status = 'выполнено' if record['completed'] else 'не выполнено'
        print(f"ID {record['id']} | {record['title']} | {record['category']} | {record['amount']} ч. | {status}")

def save(records):
    try:
        save_records(PATH, records)
    except (OSError, ValueError) as error:
        print('Ошибка сохранения:', error)
        return False
    print('Данные сохранены')
    return True

def main():
    try:
        records = load_records(PATH)
    except FileNotFoundError:
        print('Файл не найден. Создан пустой список')
        records = []
    except (OSError, ValueError) as error:
        print('Ошибка загрузки:', error)
        return
    while True:
        print('\nПлан учебных занятий')
        print('1. Показать записи\n2. Добавить запись\n3. Найти записи')
        print('4. Изменить статус\n5. Удалить запись\n6. Статистика')
        print('7. Сохранить данные\n8. Выйти')
        command = input('Команда: ').strip()
        if command == '1':
            show_records(records)
        elif command == '2':
            title = read_text('Название: ')
            category = read_text('Категория: ')
            amount = read_number('Количество часов: ')
            add_record(records, title, category, amount)
            print('Запись добавлена')
        elif command == '3':
            result = find_records(records, read_text('Поиск: '))
            if result:
                show_records(result)
            else:
                print('Ничего не найдено')
        elif command == '4':
            record_id = read_number('ID: ', 1)
            if not any(record['id'] == record_id for record in records):
                print('ID не найден')
                continue
            status = input('1 — выполнено, 0 — не выполнено: ').strip()
            while status not in ('1', '0'):
                status = input('Введите 1 или 0: ').strip()
            set_completed(records, record_id, status == '1')
            print('Статус изменён')
        elif command == '5':
            record_id = read_number('ID: ', 1)
            if not any(record['id'] == record_id for record in records):
                print('ID не найден')
            elif input('Удалить? (да/нет): ').strip().lower() == 'да':
                delete_record(records, record_id)
                print('Запись удалена')
            else:
                print('Удаление отменено')
        elif command == '6':
            result = statistics(records)
            print('Всего:', result['total'])
            print('Выполнено:', result['completed'])
            print('Не выполнено:', result['not_completed'])
            print('Всего часов:', result['amount'])
            for category in sorted(result['categories']):
                print(category, ':', result['categories'][category], 'ч.')
        elif command == '7':
            save(records)
        elif command == '8':
            answer = input('Сохранить? (да/нет): ').strip().lower()
            while answer not in ('да', 'нет'):
                answer = input('Введите да или нет: ').strip().lower()
            if answer == 'нет' or save(records):
                break
        else:
            print('Неизвестная команда')


if __name__ == '__main__':
    main()
