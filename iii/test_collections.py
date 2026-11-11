from collections_lab import*

# Задание 1. Частоты слов
assert word_counts('Python, python! SQL') == {'python': 2, 'sql': 1}
assert word_counts('!!!') == {}
assert word_counts('') == {}
assert word_counts('  ,!   ') == {}
assert word_counts('Hi: \nHI;\tSql?') == {'hi': 2, 'sql': 1}

# Задание 2. Учебные интересы
first = ['python', 'sql', 'python']
second = ['sql', 'git']
assert common_topics(first, second) == ['sql']
assert all_topics(first, second) == ['git', 'python', 'sql']
assert common_topics([], second) == []
assert all_topics([], second) == ['git', 'sql']
assert common_topics(first, []) == []
assert all_topics(first, []) == ['python', 'sql']
assert all_topics([], []) == []

# Общий пример из задания
records = [
    {'title': 'A', 'category': 'основное', 'amount': 4},
    {'title': 'B', 'category': 'дополнительное', 'amount': 2},
    {'title': 'C', 'category': 'основное', 'amount': 3}
]
original = [record.copy() for record in records]

assert totals_by_category(records) == {'основное': 7, 'дополнительное': 2}
assert titles_in_category(records, 'основное') == ['A', 'C']
assert titles_in_category(records, 'нет') == []
assert totals_by_category([]) == {}
assert titles_in_category([], 'основное') == []
assert sorted_category_totals(records) == [('основное', 7), ('дополнительное', 2)]
assert records == original

# Вариант 1. Учебные занятия, три категории
study_records = [
    {'title': 'Математика', 'category': 'точные науки', 'amount': 4},
    {'title': 'Программирование', 'category': 'точные науки', 'amount': 6},
    {'title': 'История', 'category': 'гуманитарные', 'amount': 2},
    {'title': 'Английский язык', 'category': 'языки', 'amount': 3},
    {'title': 'Русский язык', 'category': 'языки', 'amount': 2},
    {'title': 'Информационная безопасность', 'category': 'точные науки', 'amount': 5}
]
study_original = [record.copy() for record in study_records]

assert totals_by_category(study_records) == {
    'точные науки': 15,
    'гуманитарные': 2,
    'языки': 5
}
assert titles_in_category(study_records, 'языки') == [
    'Английский язык', 'Русский язык'
]
assert sorted_category_totals(study_records) == [
    ('точные науки', 15), ('языки', 5), ('гуманитарные', 2)
]
assert study_records == study_original

# Дополнительная проверка: при равных суммах сортировка по названию
same_amounts = [
    {'title': 'A', 'category': 'вторая', 'amount': 2},
    {'title': 'B', 'category': 'первая', 'amount': 2}
]
assert sorted_category_totals(same_amounts) == [
    ('вторая', 2), ('первая', 2)
]
assert sorted_category_totals([]) == []

print('Все проверки пройдены')
