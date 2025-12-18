"""
QUESTION:
Create a function called `evaluate_testing_approach` that determines whether to replace unit tests with scripted tests for certain classes of unit tests in an iterative incremental model project. The function should consider factors such as the cost of maintaining unit tests, the effectiveness of scripted tests, and the potential risks of dropping unit tests.
"""

def evaluate_testing_approach(maintenance_cost, scripted_test_effectiveness, risk_level):
    """
    Determine whether to replace unit tests with scripted tests based on cost, effectiveness, and risk.

    Args:
        maintenance_cost (float): The cost of maintaining unit tests.
        scripted_test_effectiveness (float): The effectiveness of scripted tests.
        risk_level (float): The potential risks of dropping unit tests.

    Returns:
        bool: Whether to replace unit tests with scripted tests.
    """
    # Calculate a score based on the factors
    score = maintenance_cost + scripted_test_effectiveness - risk_level

    # If the score is above a certain threshold, replace unit tests with scripted tests
    return score > 0.5