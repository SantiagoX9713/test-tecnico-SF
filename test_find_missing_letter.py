import unittest
from find_missing_letter import find_missing_letter

class TestFindmissingLetter(unittest.TestCase):
    def test_find_missing_letter(self):
        self.assertEqual(find_missing_letter(['a','b','c','d','f']), 'e')
        self.assertEqual(find_missing_letter(['O','Q','R','S']), 'P')
        self.assertEqual(find_missing_letter(['H','I','J','M']), 'K')
        # self.assertEqual(find_missing_letter(['a','b','c','d','G']), 'e')
        #self.assertEqual(find_missing_letter(['o','Q','R','S']), 'P')
        #self.assertEqual(find_missing_letter(['H','i','J','m']), 'K')


if __name__ == '__main__':
    unittest.main()