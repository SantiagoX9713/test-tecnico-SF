from difflib import unified_diff
import unittest
from array_diff import array_diff

class TestArraydiff(unittest.TestCase):
    def test_array_diff(self):
        self.assertEqual(array_diff([1,2],[1]),[2],"")
        self.assertEqual(array_diff([1,2,2],[1]),[2,2],"")
        self.assertEqual(array_diff([1,2,2],[2]),[1],"")
        self.assertEqual(array_diff([1,2,2],[]),[1,2,2],"")
        self.assertEqual(array_diff([],[1,2]),[],"")
        self.assertEqual(array_diff([1,2,3],[1,2]),[3],"")


if __name__ == '__main__':
    unittest.main()