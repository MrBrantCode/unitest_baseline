from solution import get_diagonal_sums
### test cases
import unittest

class TestGetDiagonalSums(unittest.TestCase):
    """
    This class contains test cases for the function 'get_diagonal_sums'.
    It checks if the function correctly calculates the sums of the main and secondary diagonals of a square matrix.
    """

    def test_3x3_matrix(self):
        """
        Test case for a 3x3 matrix.
        """
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        expected_result = [15, 15]  # Main diagonal: 1 + 5 + 9; Secondary diagonal: 3 + 5 + 7
        self.assertEqual(get_diagonal_sums(matrix), expected_result)

    def test_4x4_matrix(self):
        """
        Test case for a 4x4 matrix.
        """
        matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
        expected_result = [34, 34]  # Main diagonal: 1 + 7 + 11 + 15; Secondary diagonal: 4 + 7 + 10 + 13
        self.assertEqual(get_diagonal_sums(matrix), expected_result)

    def test_single_element_matrix(self):
        """
        Test case for a single-element matrix (1x1).
        """
        matrix = [[1]]
        expected_result = [1, 1]  # Both diagonals are the same and equal to 1
        self.assertEqual(get_diagonal_sums(matrix), expected_result)

    def test_zero_matrix(self):
        """
        Test case for a zero-filled matrix.
        """
        matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        expected_result = [0, 0]  # All elements are zero
        self.assertEqual(get_diagonal_sums(matrix), expected_result)  # Modified output

    def test_negative_values(self):
        """
        Test case for a matrix with negative values.
        """
        matrix = [[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]]
        expected_result = [-15, -15]  # Main diagonal: -1 + -5 + -9; Secondary diagonal: -3 + -5 + -7
        self.assertEqual(get_diagonal_sums(matrix), expected_result)  # Modified output

if __name__ == '__main__':
    unittest.main()
