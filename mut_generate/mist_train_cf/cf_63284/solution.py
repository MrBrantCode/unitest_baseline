"""
QUESTION:
Implement a function `calculate_final_points` that takes in two parameters: `initial_points` and `threshold`. The function should simulate a game where the points increase by the sum of the last two numbers of a dynamic Fibonacci sequence that starts with 1 and 2. The Fibonacci sequence should restart from the beginning if a number divisible by 7 is encountered. If the points reach half of the threshold, 5 points should be deducted. The function should return the final points when the points exceed the threshold.
"""

def calculate_final_points(initial_points, threshold):
    """
    Simulate a game where the points increase by the sum of the last two numbers 
    of a dynamic Fibonacci sequence that starts with 1 and 2. The Fibonacci 
    sequence restarts from the beginning if a number divisible by 7 is encountered. 
    If the points reach half of the threshold, 5 points are deducted. The function 
    returns the final points when the points exceed the threshold.

    Args:
        initial_points (int): The initial points of the player.
        threshold (int): The target points to be reached.

    Returns:
        int: The final points of the player.
    """

    current_points = initial_points
    fibonacci_sequence = [1, 2]

    while current_points <= threshold:
        next_value = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        if next_value % 7 == 0:
            fibonacci_sequence = [1, 2]
        else:
            fibonacci_sequence.append(next_value)
            current_points += next_value

        if current_points >= threshold / 2 and current_points - next_value < threshold / 2:
            current_points -= 5

    return current_points