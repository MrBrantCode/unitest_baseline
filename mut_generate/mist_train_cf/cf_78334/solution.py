"""
QUESTION:
Write a function `time_to_reach_max_height(v_i)` that calculates the time it will take for a rocket to reach its maximum height given its initial velocity `v_i` (in m/s), assuming a gravitational acceleration of 9.8 m/s^2. The function should return the time in seconds, rounded to three decimal places. Ensure the function includes input validation to handle cases where `v_i` is not provided, is negative, or is a non-numeric input.
"""

def time_to_reach_max_height(v_i):
    try:
        if isinstance(v_i, (list, dict, bool)) or v_i <= 0:
            raise Exception
        else:
            g = 9.8
            t = round(v_i / g, 3)
            return t
    except Exception:
        return "Invalid input. Please enter a positive numeric initial velocity."