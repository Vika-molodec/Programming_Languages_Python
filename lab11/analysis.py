"""Проверка и анализ учебных задач (вариант 1)."""
#Задание 1
def validate_todos(data):
    if not isinstance(data, list):
        raise ValueError('Корень JSON должен быть списком')
    seen_ids = set()
    for index, task in enumerate(data, start=1):
        if not isinstance(task, dict):
            raise ValueError(f'Запись {index}: ожидается словарь')
        for field in ('id', 'userId'):
            if field not in task or type(task[field]) is not int or task[field] <= 0:
                raise ValueError(f'Запись {index}: {field} должен быть положительным целым числом')
        if task['id'] in seen_ids:
            raise ValueError(f"Запись {index}: повторяющийся id {task['id']}")
        seen_ids.add(task['id'])
        if type(task.get('title')) is not str or not task['title'].strip():
            raise ValueError(f'Запись {index}: title должен быть непустой строкой')
        if type(task.get('completed')) is not bool:
            raise ValueError(f'Запись {index}: completed должен быть логическим значением')

#Задание 2
def completion_counts(todos):
    counts = {}
    for task in todos:
        user_id = task['userId']
        counts[user_id] = counts.get(user_id, 0) + int(task['completed'])
    return counts

def top_users(counts):
    if not counts:
        return []
    maximum = max(counts.values())
    if maximum == 0:
        return []
    return sorted(user_id for user_id, count in counts.items() if count == maximum)

def leader_tasks(todos, leaders):
    leader_ids = set(leaders)
    return [task for task in todos if task['completed'] and task['userId'] in leader_ids]


def select_tasks(todos, user_id, parameter=None):
    """Вариант 1: все задачи указанного пользователя в исходном порядке."""
    return [task for task in todos if task['userId'] == user_id]
