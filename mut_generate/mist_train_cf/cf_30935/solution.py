"""
QUESTION:
Create a unit test class named `TestAverageCalculator` that inherits from `unittest.TestCase`. 

Implement a test method named `test_average_calculation` to verify the correctness of the `Util.calculate_average` function, which takes a list of numbers as input and returns the average. 

The test method should cover the following scenarios:
- An empty list
- A list with positive numbers
- A list with negative numbers
- A list with a combination of positive and negative numbers 

Use a custom logger to log the test progress and a checkpoint to verify the test result.
"""

def calculate_average(input_list):
    if len(input_list) == 0:
        return None
    return sum(input_list) / len(input_list)