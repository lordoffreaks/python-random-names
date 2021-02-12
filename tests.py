import unittest
import unittest.mock as mock
import names
from names import random_names


class TestRandomNames(unittest.TestCase):

    def test_positive_number_of_names(self):
        lines = 'Danielle 367791\nTheresa 369848\nMarilyn 369847'
        with mock.patch('builtins.open', mock.mock_open(read_data=lines)) as m:
            names = random_names('data/names.txt', 3)
            self.assertEqual(len(names), 3)
            self.assertEqual(type(names[0]).__name__, 'str')

    def test_zero_number_of_names(self):
        lines = 'Danielle 367791\nTheresa 369848\nMarilyn 369847'
        with mock.patch('builtins.open', mock.mock_open(read_data=lines)) as m:
            names = random_names('data/names.txt', 0)
            self.assertEqual(len(names), 0)

    def test_negative_number_of_names(self):
        lines = 'Danielle 367791\nTheresa 369848\nMarilyn 369847'
        with mock.patch('builtins.open', mock.mock_open(read_data=lines)) as m:
            names = random_names('data/names.txt', -5)
            self.assertEqual(len(names), 0)

    def test_blanks(self):
        lines = 'Danielle 367791\n   \nTheresa 369848\nMarilyn 369847'
        with mock.patch('builtins.open', mock.mock_open(read_data=lines)) as m:
            self.assertEqual(len(random_names('data/names.txt', 3)), 3)
            self.assertRaises(ValueError, random_names, 'data/names.txt', 4)

    def test_new_lines(self):
        lines = 'Danielle 367791\nTheresa 369848\n\nMarilyn 369847\n\n'
        with mock.patch('builtins.open', mock.mock_open(read_data=lines)) as m:
            self.assertEqual(len(random_names('data/names.txt', 3)), 3)
            self.assertRaises(ValueError, random_names, 'data/names.txt', 4)

    def test_new_numbers_as_name(self):
        lines = '367791 367791\nTheresa 369848\n\nMarilyn 369847\n\n'
        with mock.patch('builtins.open', mock.mock_open(read_data=lines)) as m:
            names = random_names('data/names.txt', 2)
            self.assertEqual(len(names), 2)
            self.assertEqual(names, ['Theresa', 'Marilyn'])
            self.assertRaises(ValueError, random_names, 'data/names.txt', 3)

    def test_ordering(self):
        lines = 'Danielle 367791\nTheresa 369848\nMarilyn 369847'
        with mock.patch('builtins.open', mock.mock_open(read_data=lines)) as m:
            names = random_names('data/names.txt', 3)
            self.assertEqual(['Theresa', 'Marilyn', 'Danielle'], names)

    def test_duplicate_lines(self):
        lines = 'Danielle 367791\nTheresa 369848\n\nTheresa 369848'
        with mock.patch('builtins.open', mock.mock_open(read_data=lines)) as m:
            self.assertEqual(len(random_names('data/names.txt', 2)), 2)
            self.assertRaises(ValueError, random_names, 'data/names.txt', 3)

    def test_duplicate_names(self):
        lines = 'Danielle 367791\nTheresa 369848\n\nTheresa 1234'
        with mock.patch('builtins.open', mock.mock_open(read_data=lines)) as m:
            self.assertEqual(len(random_names('data/names.txt', 2)), 2)
            self.assertRaises(ValueError, random_names, 'data/names.txt', 3)

if __name__ == '__main__':
    unittest.main()
