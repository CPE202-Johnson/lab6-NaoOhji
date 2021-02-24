import unittest
from sorts import *
from quicksort import *

class TestLab4(unittest.TestCase):

    def test_simple(self):
        nums = [23, 10]
        comps = selection_sort(nums)
        #comps = quick_sort(nums)
        self.assertEqual(comps, 1)
        self.assertEqual(nums, [10, 23])

if __name__ == '__main__': 
    unittest.main()
