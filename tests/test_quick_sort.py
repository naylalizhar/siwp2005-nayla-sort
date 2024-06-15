import unittest
from src.sort.quick_sort import quick_sort

class TestQuickSort(unittest.TestCase):
    def test_quick_sort(self):
        data = [64, 34, 25, 12, 22, 11, 90]
        sorted_data = [11, 12, 22, 25, 34, 64, 90]
        self.assertEqual(quick_sort(data), sorted_data)

if __name__ == '__main__':
    unittest.main()
