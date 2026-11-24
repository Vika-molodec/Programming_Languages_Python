import unittest
from pathlib import Path
from tempfile import TemporaryDirectory
from storage import load_records, save_records
from logic import add_record

class TestStorage(unittest.TestCase):
    def test_save_load(self):
        with TemporaryDirectory() as folder:
            path = Path(folder) / 'data.json'
            records = []
            add_record(records, 'Python', 'учёба', 4)
            records[0]['completed'] = True
            save_records(path, records)
            self.assertEqual(load_records(path), records)

    def test_invalid_json(self):
        with TemporaryDirectory() as folder:
            path = Path(folder) / 'data.json'
            path.write_text('{', encoding='utf-8')
            with self.assertRaises(ValueError):
                load_records(path)
            self.assertEqual(path.read_text(encoding='utf-8'), '{')

    def test_missing(self):
        with TemporaryDirectory() as folder:
            with self.assertRaises(FileNotFoundError):
                load_records(Path(folder) / 'data.json')

    def test_save_error(self):
        with TemporaryDirectory() as folder:
            with self.assertRaises(OSError):
                save_records(Path(folder) / 'missing' / 'data.json', [])

if __name__ == '__main__':
    unittest.main()
