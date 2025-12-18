from solution import entrance
### test class
import unittest

class TestProblemSolver(unittest.TestCase):
    """
    This class contains unit tests for the functions solve_problem, calculate_delta, and calculate_sum.
    """

    def test_solve_problem(self):
        """
        Test the solve_problem function with various inputs to ensure it correctly removes duplicates,
        sorts the list in descending order, and handles edge cases.
        """
        # Test with an empty list
        self.assertEqual(entrance([]), [])
        
        # Test with a list containing duplicates
        self.assertEqual(entrance([5, 3, 5, 2]), [5, 3, 2])
        
        # Test with a list containing negative numbers
        self.assertEqual(entrance([-1, -3, -2]), [-1, -2, -3])
        
        # Test with a list containing only one unique element
        self.assertEqual(entrance([7]), [7])

    def test_calculate_delta(self):
        """
        Test the calculate_delta function with various inputs to ensure it correctly calculates the difference
        between the two largest elements in the list.
        """
        # Test with a list of two elements
        self.assertEqual(calculate_delta([10, 20]), 10)
        
        # Test with a list of more than two elements
        self.assertEqual(calculate_delta([10, 20, 30]), 10)
        
        # Test with a list containing duplicates
        self.assertEqual(calculate_delta([10, 10, 20]), 10)
        
        # Test with a list containing negative numbers
        self.assertEqual(calculate_delta([-10, -20]), 10)

    def test_calculate_sum(self):
        """
        Test the calculate_sum function with various inputs to ensure it correctly calculates the sum of the two
        smallest elements in the list.
        """
        # Test with a list of two elements
        self.assertEqual(calculate_sum([10, 20]), 30)
        
        # Test with a list of more than two elements
        self.assertEqual(calculate_sum([10, 20, 30]), 30)
        
        # Test with a list containing duplicates
        self.assertEqual(calculate_sum([10, 10, 20]), 20)
        
        # Test with a list containing negative numbers
        self.assertEqual(calculate_sum([-10, -20]), -30)        

if __name__ == '__main__':
    unittest.main()
