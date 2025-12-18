from solution import calculate_ladder_climbing_time
### Test Cases
import unittest
from math import sqrt
from math import atan
from math import sin

class TestLadderClimbingTime(unittest.TestCase):

    def test_calculate_ladder_climbing_time(self):
        # Given values
        ladder_length = 40  # feet
        base_distance = 15  # feet
        climbing_speed = 30 / 65  # feet per second
        time_interval = 65  # seconds

        # Expected result
        expected_time_to_reach_top = ladder_length / (climbing_speed * sin(atan(sqrt(ladder_length**2 - base_distance**2) / base_distance)))

        # Actual result
        actual_time_to_reach_top = calculate_ladder_climbing_time(ladder_length, base_distance, climbing_speed, time_interval)

        # Check if the actual result matches the expected result
        self.assertAlmostEqual(actual_time_to_reach_top, expected_time_to_reach_top, places=5)

    def test_calculate_ladder_climbing_time_with_different_values(self):
        # Given values
        ladder_length = 50  # feet
        base_distance = 20  # feet
        climbing_speed = 40 / 80  # feet per second
        time_interval = 80  # seconds

        # Expected result
        expected_time_to_reach_top = ladder_length / (climbing_speed * sin(atan(sqrt(ladder_length**2 - base_distance**2) / base_distance)))

        # Actual result
        actual_time_to_reach_top = calculate_ladder_climbing_time(ladder_length, base_distance, climbing_speed, time_interval)

        # Check if the actual result matches the expected result
        self.assertAlmostEqual(actual_time_to_reach_top, expected_time_to_reach_top, places=5)

if __name__ == '__main__':
    unittest.main()
