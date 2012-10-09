from array_functions import *
import unittest

TEST_ARRAY = [1,5,7,3,8,13,14,16,2]

class array_test(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)

    def test_sort(self):
        sorted_array = sort_array(TEST_ARRAY)
        self.assertTrue(sorted_array == [1,2,3,5,7,8,13,14,16])
        return

    def test_max_element(self):
        max_el = max_element(TEST_ARRAY)
        self.assertTrue(max_el == 16)
        return

    def test_min_element(self):
        min_el = min_element(TEST_ARRAY)
        self.assertTrue(min_el == 1)
        return

    def test_search(self):
        index = search_array(TEST_ARRAY,8)
        self.assertTrue(index==4)
        return

    def test_binary_search(self):
        sorted_array = sort_array(TEST_ARRAY)
        index = binary_search(sorted_array, 8)
        self.assertTrue(index==5)
        return


if __name__ == '__main__':
    unittest.main()