from solution import check_constraint
### test cases
import unittest

class TestCheckConstraint(unittest.TestCase):
    def setUp(self):
        # Set up a standard 10x10 board with some predefined values for testing
        self.board = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 1, 2, 2, 2, 2, 2, 1, 1, 0],
            [0, 1, 2, 3, 3, 3, 2, 1, 1, 0],
            [0, 1, 2, 3, 4, 3, 2, 1, 1, 0],
            [0, 1, 2, 3, 3, 3, 2, 1, 1, 0],
            [0, 1, 2, 2, 2, 2, 2, 1, 1, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]

    def test_no_cells_exceeding_three_mines(self):
        # Test case where no cells within the specified radius exceed three mines
        self.assertTrue(check_constraint((5, 5), self.board))

    def test_cell_exceeding_three_mines(self):
        # Test case where a cell within the specified radius exceeds three mines
        self.assertFalse(check_constraint((4, 4), self.board))

    def test_radius_one(self):
        # Test case with radius set to one
        self.assertTrue(check_constraint((5, 5), self.board, radius=1))

    def test_radius_ten(self):
        # Test case with radius set to ten (should still only consider the board boundaries)
        self.assertFalse(check_constraint((5, 5), self.board, radius=10))  # Modified output

    def test_edge_case(self):
        # Test case where the cell to uncover is on the edge of the board
        self.assertTrue(check_constraint((0, 0), self.board))
        self.assertTrue(check_constraint((9, 9), self.board))  # Modified output

if __name__ == '__main__':
    unittest.main()
