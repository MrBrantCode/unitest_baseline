from solution import navigate_grid
### test cases
import unittest

class TestNavigateGrid(unittest.TestCase):
    def test_reachable_destination(self):
        # Test case where the destination is reachable
        grid = [
            [0, 0, 0],
            [0, 1, 0],
            [0, 0, 0]
        ]
        start = (0, 0)
        destination = (2, 2)
        self.assertTrue(navigate_grid(grid, start, destination))

    def test_blocked_path(self):
        # Test case where there is a blocked path between start and destination
        grid = [
            [0, 0, 0],
            [0, 1, 0],
            [0, 0, 0]
        ]
        start = (0, 0)
        destination = (2, 1)
        self.assertFalse(navigate_grid(grid, start, destination))

    def test_start_equals_destination(self):
        # Test case where the start and destination are the same
        grid = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        start = (1, 1)
        destination = (1, 1)
        self.assertTrue(navigate_grid(grid, start, destination))

    def test_impossible_path(self):
        # Test case where the destination is completely blocked
        grid = [
            [0, 0, 0],
            [0, 1, 0],
            [0, 1, 0]
        ]
        start = (0, 0)
        destination = (2, 2)
        self.assertFalse(navigate_grid(grid, start, destination))

    def test_large_grid(self):
        # Test case with a larger grid
        grid = [
            [0, 0, 0, 0, 0],
            [0, 1, 1, 1, 0],
            [0, 0, 0, 0, 0],
            [0, 1, 1, 1, 0],
            [0, 0, 0, 0, 0]
        ]
        start = (0, 0)
        destination = (4, 4)
        self.assertTrue(navigate_grid(grid, start, destination))  # Modified output

    def test_start_blocked(self):
        # Test case where the start is blocked
        grid = [
            [1, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        start = (0, 0)
        destination = (2, 2)
        self.assertFalse(navigate_grid(grid, start, destination))  # Modified output

if __name__ == '__main__':
    unittest.main()
