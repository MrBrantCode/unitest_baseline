from solution import findMaxPath
### test cases
import unittest

class TestFindMaxPath(unittest.TestCase):
    def test_single_element(self):
        # Test case with a single element grid
        mat = [[1]]
        self.assertEqual(findMaxPath(mat), 1)

    def test_2x2_grid(self):
        # Test case with a 2x2 grid
        mat = [[1, 3], [1, 1]]
        self.assertEqual(findMaxPath(mat), 5)

    def test_3x3_grid(self):
        # Test case with a 3x3 grid
        mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(findMaxPath(mat), 29)

    def test_negative_values(self):
        # Test case with negative values in the grid
        mat = [[-1, -2], [-3, -4]]
        self.assertEqual(findMaxPath(mat), -4)

    def test_mixed_values(self):
        # Test case with mixed positive and negative values
        mat = [[1, -2, 3], [-4, 5, -6], [7, -8, 9]]
        self.assertEqual(findMaxPath(mat), 13)  # Modified output

    def test_large_grid(self):
        # Test case with a larger grid
        mat = [[1]*10 for _ in range(10)]
        self.assertEqual(findMaxPath(mat), 55)  # Modified output

    def test_edge_cases(self):
        # Test case with edge cases like all zeros or all ones
        mat = [[0]*5 for _ in range(5)]
        self.assertEqual(findMaxPath(mat), 0)
        
        mat = [[1]*5 for _ in range(5)]
        self.assertEqual(findMaxPath(mat), 15)  # Modified output

if __name__ == '__main__':
    unittest.main()
