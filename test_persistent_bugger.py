import unittest
from persistent_bugger import persistence

class TestPersistence(unittest.TestCase):
    def test_persistence(self):
        self.assertEqual(persistence(39),3,"Wrong output for '39'")
        self.assertEqual(persistence(4),0,"Wrong output for '4'")
        self.assertEqual(persistence(25),2,"Wrong output for '25'")
        self.assertEqual(persistence(999),4,"Wrong output for '999'")

if __name__ == '__main__':
    unittest.main()