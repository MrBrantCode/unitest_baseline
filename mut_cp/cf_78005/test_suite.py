from solution import distribute_equally
### test cases
import unittest

class TestDistributeEqually(unittest.TestCase):
    """
    Test class for the distribute_equally function.
    """

    def test_even_distribution(self):
        # Test case where the total sum can be evenly divided by the number of people
        total_sum = 100
        people = 5
        expected_each_gets = 20
        expected_amount_left = 0
        self.assertEqual(distribute_equally(total_sum, people), (expected_each_gets, expected_amount_left))

    def test_odd_distribution(self):
        # Test case where the total sum cannot be evenly divided by the number of people
        total_sum = 101
        people = 5
        expected_each_gets = 20
        expected_amount_left = 1
        self.assertEqual(distribute_equally(total_sum, people), (expected_each_gets, expected_amount_left))

    def test_single_person(self):
        # Test case with only one person
        total_sum = 100
        people = 1
        expected_each_gets = 100
        expected_amount_left = 0
        self.assertEqual(distribute_equally(total_sum, people), (expected_each_gets, expected_amount_left))

    def test_zero_people(self):
        # Test case with zero people (should raise an error or return a specific value)
        total_sum = 100
        people = 0
        with self.assertRaises(ZeroDivisionError):
            distribute_equally(total_sum, people)

    def test_negative_total_sum(self):
        # Test case with a negative total sum
        total_sum = -100
        people = 5
        expected_each_gets = -20
        expected_amount_left = 0
        self.assertEqual(distribute_equally(total_sum, people), (expected_each_gets, expected_amount_left))  # Modified output

    def test_negative_people(self):
        # Test case with a negative number of people
        total_sum = 100
        people = -5
        with self.assertRaises(ZeroDivisionError):
            distribute_equally(total_sum, people)  # Modified output

if __name__ == '__main__':
    unittest.main()
