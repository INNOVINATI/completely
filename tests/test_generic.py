import unittest

from completely import measure


class GeneralTestCase(unittest.TestCase):

    def test_list_with_alphanums(self):
        ls = ['a', None, 'b', '', 'c', 'd']
        self.assertEqual(measure(ls), 0.667)

    def test_list_with_dicts(self):
        ls = [{'a': 1, 'b': []}, {'a': None, 'b': [1, 2]}, {'a': 2, 'b': [4, 5]}]
        self.assertEqual(measure(ls), 0.667)

    def test_nested_list_with_alphanums(self):
        ls = [[1, None, 1, None, 1, None], ['a', ''], [123123123, 1231231231]]
        self.assertEqual(measure(ls), 0.667)

    def test_nested_list_with_dicts(self):
        ls = [[{'a': 1, 'b': []}], [{'a': None, 'b': [1, 2]}], [{'a': 2, 'b': [4, 5]}]]
        self.assertEqual(measure(ls), 0.667)


if __name__ == '__main__':
    unittest.main()