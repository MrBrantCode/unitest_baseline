from solution import knapsack
### test case
import unittest

class TestKnapsack(unittest.TestCase):
    def test_knapsack_basic(self):
        # Test with basic input
        W = 50
        weights = [10, 20, 30]
        values = [60, 100, 120]
        expected_max_value = 220
        expected_selected_items = [2, 0]
        max_value, selected_items = knapsack(W, weights, values)
        self.assertEqual(max_value, expected_max_value)
        self.assertEqual(selected_items, expected_selected_items)

    def test_knapsack_no_items(self):
        # Test with no items
        W = 50
        weights = []
        values = []
        expected_max_value = 0
        expected_selected_items = []
        max_value, selected_items = knapsack(W, weights, values)
        self.assertEqual(max_value, expected_max_value)
        self.assertEqual(selected_items, expected_selected_items)

    def test_knapsack_single_item(self):
        # Test with a single item
        W = 50
        weights = [10]
        values = [60]
        expected_max_value = 60
        expected_selected_items = [0]
        max_value, selected_items = knapsack(W, weights, values)
        self.assertEqual(max_value, expected_max_value)
        self.assertEqual(selected_items, expected_selected_items)

    def test_knapsack_all_items_fit(self):
        # Test when all items fit in the knapsack
        W = 100
        weights = [10, 20, 30]
        values = [60, 100, 120]
        expected_max_value = 280
        expected_selected_items = [2, 1, 0]
        max_value, selected_items = knapsack(W, weights, values)
        self.assertEqual(max_value, expected_max_value)
        self.assertEqual(selected_items, expected_selected_items)

    def test_knapsack_no_space(self):
        # Test when there is no space in the knapsack
        W = 10
        weights = [10, 20, 30]
        values = [60, 100, 120]
        expected_max_value = 0
        expected_selected_items = []
        max_value, selected_items = knapsack(W, weights, values)
        self.assertEqual(max_value, expected_max_value)
        self.assertEqual(selected_items, expected_selected_items)  # Modified output

    def test_knapsack_equal_weights_values(self):
        # Test when weights and values are equal
        W = 10
        weights = [5, 5]
        values = [5, 5]
        expected_max_value = 10
        expected_selected_items = [1, 0]
        max_value, selected_items = knapsack(W, weights, values)
        self.assertEqual(max_value, expected_max_value)
        self.assertEqual(selected_items, expected_selected_items)  # Modified output

if __name__ == '__main__':
    unittest.main()
