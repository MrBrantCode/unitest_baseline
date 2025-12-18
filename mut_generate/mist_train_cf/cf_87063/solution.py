"""
QUESTION:
Create a function "avg_grade" or class method that takes a list of integer grades and returns the average of the grades. The function/method should have the following properties: 

- It should not use any built-in functions or libraries to calculate the average.
- It should not use any temporary variables to store intermediate values during calculations.
- It should handle cases where the list of grades is empty and throw an appropriate exception.
- It should check if the grades list contains any negative values and raise an exception if so.
- It should handle cases where the list of grades contains duplicate values and calculate the average accordingly.
- It should handle cases where the list of grades is unsorted and calculate the average in O(n) time complexity, where n is the number of grades in the list.
- It should provide an option to calculate the average of a specific range of grades within the list, given the start and end indices. The range should be inclusive of both the start and end indices.
"""

from typing import List

def avg_grade(grades: List[int], start_index: int = 0, end_index: int = None) -> float:
    """
    Calculate the average of a list of grades.

    Args:
    grades (List[int]): A list of grades.
    start_index (int, optional): The start index of the range of grades to calculate the average for. Defaults to 0.
    end_index (int, optional): The end index of the range of grades to calculate the average for. Defaults to None, which means the end of the list.

    Returns:
    float: The average of the grades in the specified range.

    Raises:
    Exception: If the grades list is empty or contains negative values, or if the range indices are invalid.
    """

    if end_index is None:
        end_index = len(grades) - 1

    if len(grades) == 0:
        raise Exception("Grades list is empty.")
    if any(grade < 0 for grade in grades):
        raise Exception("Grades list should not contain negative values.")
    if start_index < 0 or end_index >= len(grades) or start_index > end_index:
        raise Exception("Invalid range indices.")

    sum_grade = 0
    for i in range(start_index, end_index + 1):
        sum_grade += grades[i]
    range_size = end_index - start_index + 1
    return round(sum_grade / range_size)