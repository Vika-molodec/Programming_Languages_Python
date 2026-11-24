def validate_records(records):
    """Проверяет список, при ошибке вызывает ValueError."""
    if not isinstance(records, list):
        raise ValueError('Ожидался список')
    ids = set()
    for record in records:
        if not isinstance(record, dict):
            raise ValueError('Запись должна быть словарём')
        for key in ['id', 'title', 'category', 'amount', 'completed']:
            if key not in record:
                raise ValueError('Нет поля ' + key)
        if type(record['id']) is not int or record['id'] <= 0:
            raise ValueError('Некорректный ID')
        if record['id'] in ids:
            raise ValueError('Повторный ID')
        ids.add(record['id'])
        for key in ['title', 'category']:
            if not isinstance(record[key], str) or not record[key].strip():
                raise ValueError('Некорректное поле ' + key)
        if type(record['amount']) is not int or record['amount'] < 0:
            raise ValueError('Некорректное количество часов')
        if type(record['completed']) is not bool:
            raise ValueError('Некорректный статус')


def add_record(records, title, category, amount):
    """Добавляет запись в список и возвращает её."""
    new_id = 1
    for record in records:
        if record['id'] >= new_id:
            new_id = record['id'] + 1
    record = {'id': new_id, 'title': title.strip(), 'category': category.strip(),
              'amount': amount, 'completed': False}
    validate_records([record])
    records.append(record)
    return record


def find_records(records, query):
    """Возвращает найденные записи, не изменяя список."""
    query = query.strip().lower()
    if not query:
        raise ValueError('Пустой запрос')
    result = []
    for record in records:
        if query in record['title'].lower():
            result.append(record)
    return result


def set_completed(records, record_id, completed):
    """Меняет статус; возвращает False, если ID не найден."""
    if type(completed) is not bool:
        raise ValueError('Некорректный статус')
    for record in records:
        if record['id'] == record_id:
            record['completed'] = completed
            return True
    return False


def delete_record(records, record_id):
    """Удаляет запись; возвращает False, если ID не найден."""
    for record in records:
        if record['id'] == record_id:
            records.remove(record)
            return True
    return False


def statistics(records):
    """Возвращает статистику, не изменяя список."""
    completed = 0
    amount = 0
    categories = {}
    for record in records:
        if record['completed']:
            completed += 1
        amount += record['amount']
        category = record['category'].strip()
        categories[category] = categories.get(category, 0) + record['amount']
    return {'total': len(records), 'completed': completed,
            'not_completed': len(records) - completed, 'amount': amount,
            'categories': categories}
