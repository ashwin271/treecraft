import unittest
from treecraft.core.parser import TreeParser

class TestTreeParser(unittest.TestCase):
    def setUp(self):
        self.parser = TreeParser()

    def test_parse_simple_structure(self):
        content = """
        src/
        ├── main.py
        └── utils/
            └── helpers.py
        """
        expected_structure = {
            'src': {
                'main.py': {},
                'utils': {
                    'helpers.py': {}
                }
            }
        }
        result = self.parser.parse(content)
        self.assertEqual(result, expected_structure)

if __name__ == '__main__':
    unittest.main()