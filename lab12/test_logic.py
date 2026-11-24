import unittest
from logic import *

class TestLogic(unittest.TestCase):
    def test_empty(self):
        validate_records([])
        self.assertEqual(statistics([]), {'total': 0, 'completed': 0,
                         'not_completed': 0, 'amount': 0, 'categories': {}})

    def test_add_search_delete(self):
        records = []
        add_record(records, '  Python  ', ' учёба ', 4)
        add_record(records, 'Python', 'учёба', 2)
        self.assertEqual(records[0]['title'], 'Python')
        self.assertEqual(len(find_records(records, 'PY')), 2)
        self.assertTrue(delete_record(records, 1))
        self.assertEqual(records[0]['id'], 2)
        self.assertEqual(add_record(records, 'Математика', 'учёба', 0)['id'], 3)

    def test_status_statistics(self):
        records = []
        add_record(records, 'Python', 'ИТ', 4)
        add_record(records, 'Алгебра', 'математика', 2)
        self.assertTrue(set_completed(records, 2, True))
        self.assertFalse(set_completed(records, 99, True))
        self.assertFalse(delete_record(records, 99))
        self.assertEqual(statistics(records), {'total': 2, 'completed': 1,
                         'not_completed': 1, 'amount': 6,
                         'categories': {'ИТ': 4, 'математика': 2}})
        self.assertTrue(set_completed(records, 2, False))

    def test_invalid(self):
        record = add_record([], 'Python', 'ИТ', 4)
        for key, value in [('id', True), ('id', 0), ('amount', True),
                           ('amount', -1), ('amount', 1.5), ('completed', 1),
                           ('title', ' '), ('category', None)]:
            bad = record.copy()
            bad[key] = value
            with self.assertRaises(ValueError):
                validate_records([bad])
        with self.assertRaises(ValueError):
            validate_records([record, record.copy()])
        with self.assertRaises(ValueError):
            find_records([], ' ')

if __name__ == '__main__':
    unittest.main()
