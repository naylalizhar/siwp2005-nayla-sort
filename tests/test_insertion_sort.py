import unittest
from src.sort.insertion_sort import insertion_sort

class TestInsertionSort(unittest.TestCase):
    def test_insertion_sort(self):
        data = [64, 34, 25, 12, 22, 11, 90]
        sorted_data = [11, 12, 22, 25, 34, 64, 90]
        self.assertEqual(insertion_sort(data), sorted_data)

if __name__ == '__main__':
    unittest.main()
