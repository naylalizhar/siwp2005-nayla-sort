import unittest
from src.sort.bubble_sort import bubble_sort

class TestBubbleSort(unittest.TestCase):
    def test_bubble_sort(self):
        data = [64, 34, 25, 12, 22, 11, 90]
        sorted_data = [11, 12, 22, 25, 34, 64, 90]
        self.assertEqual(bubble_sort(data), sorted_data)

if __name__ == '__main__':
    unittest.main()
