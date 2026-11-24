import json
from logic import validate_records

def load_records(path):
    """Читает JSON и возвращает проверенный список."""
    with open(path, 'r', encoding='utf-8') as file:
        records = json.load(file)
    validate_records(records)
    return records

def save_records(path, records):
    """Проверяет и сохраняет список в JSON."""
    validate_records(records)
    with open(path, 'w', encoding='utf-8') as file:
        json.dump(records, file, ensure_ascii=False, indent=2)
