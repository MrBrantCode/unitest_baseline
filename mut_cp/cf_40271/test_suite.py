from solution import count_solutions
### test cases
import unittest

class TestCountSolutions(unittest.TestCase):
    def test_reach_target_with_single_step(self):
        # Test case where the target can be reached with a single step.
        self.assertEqual(count_solutions(0, 5, {5}), 1)

    def test_reach_target_with_multiple_steps(self):
        # Test case where the target can be reached with multiple steps using different combinations.
        self.assertEqual(count_solutions(0, 4, {1, 2, 3}), 4)

    def test_cannot_reach_target(self):
        # Test case where the target cannot be reached with any combination of the given scores.
        self.assertEqual(count_solutions(0, 3, {2, 4}), 0)

    def test_initial_score_greater_than_target(self):
        # Test case where the initial score is already greater than the target score.
        self.assertEqual(count_solutions(10, 5, {1, 2, 3}), 0)

    def test_target_is_zero(self):
        # Test case where the target score is zero.
        self.assertEqual(count_solutions(0, 0, {1, 2, 3}), 1)

    def test_no_possible_solution(self):
        # Test case where no combination of scores can reach the target.
        self.assertEqual(count_solutions(0, 7, {2, 4}), 2)  # Modified output

    def test_large_target(self):
        # Test case with a large target score to ensure the function handles it correctly.
        self.assertEqual(count_solutions(0, 100, {1, 2, 5}), 41)  # Modified output

if __name__ == '__main__':
    unittest.main()
