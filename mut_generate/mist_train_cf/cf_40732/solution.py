"""
QUESTION:
Create a function named `calculate_average_ap_score` that takes a list of integers `district_data` representing the AP scores of students in a district and returns the average score for all students in that district as a floating-point number. The function should handle edge cases such as empty input.
"""

from typing import List

def calculate_average_ap_score(district_data: List[int]) -> float:
    if not district_data:
        return 0.0  # Return 0 for empty input

    total_score = sum(district_data)
    average_score = total_score / len(district_data)
    return average_score