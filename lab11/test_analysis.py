import json
import tempfile
import unittest
from pathlib import Path
from copy import deepcopy

from analysis import (validate_todos, completion_counts, top_users,
                      leader_tasks, select_tasks)

BASE = Path(__file__).resolve().parent


class AnalysisTests(unittest.TestCase):
    def setUp(self):
        with open(BASE / 'todos.json', encoding='utf-8') as file:
            self.todos = json.load(file)

    def test_example(self):
        validate_todos(self.todos)
        counts = completion_counts(self.todos)
        self.assertEqual(counts, {5: 2, 10: 2})
        leaders = top_users(counts)
        self.assertEqual(leaders, [5, 10])
        self.assertEqual([t['id'] for t in leader_tasks(self.todos, leaders)], [1, 3, 4, 5])

    def test_empty(self):
        self.assertEqual(completion_counts([]), {})
        self.assertEqual(top_users({}), [])
        self.assertEqual(leader_tasks([], []), [])

    def test_no_completed(self):
        tasks = [dict(t, completed=False) for t in self.todos]
        counts = completion_counts(tasks)
        self.assertEqual(counts, {5: 0, 10: 0})
        self.assertEqual(top_users(counts), [])
        self.assertEqual(leader_tasks(tasks, []), [])

    def test_one_leader(self):
        tasks = deepcopy(self.todos)
        tasks[2]['completed'] = False
        tasks[3]['completed'] = False
        self.assertEqual(top_users(completion_counts(tasks)), [5])

    def test_tie(self):
        self.assertEqual(top_users({10: 2, 5: 2, 7: 1}), [5, 10])

    def test_variant1(self):
        previous = deepcopy(self.todos)
        self.assertEqual([t['id'] for t in select_tasks(self.todos, 5)], [1, 2, 5])
        self.assertEqual(select_tasks(self.todos, 999), [])
        self.assertEqual(select_tasks(self.todos[:1], 10), [])
        self.assertEqual(self.todos, previous)

    def test_invalid_data(self):
        bad_cases = [
            {},
            [self.todos[0], self.todos[0]],
            [{k: v for k, v in self.todos[0].items() if k != 'userId'}],
            [dict(self.todos[0], completed='false')],
            [dict(self.todos[0], id=True)],
            [dict(self.todos[0], userId=False)],
            [dict(self.todos[0], title='   ')],
        ]
        for bad in bad_cases:
            with self.subTest(bad=bad), self.assertRaises(ValueError):
                validate_todos(bad)

    def test_roundtrip(self):
        selected = select_tasks(self.todos, 5)
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / 'selected.json'
            with open(path, 'w', encoding='utf-8') as file:
                json.dump(selected, file, ensure_ascii=False, indent=2)
            with open(path, encoding='utf-8') as file:
                restored = json.load(file)
        self.assertEqual(restored, selected)


if __name__ == '__main__':
    unittest.main()
