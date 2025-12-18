"""
QUESTION:
Create a function "avg_grade" that takes a list of grades as input and returns the average of the grades. The function should handle cases where the list of grades is empty and raise an exception if so. It should also check if the grades list contains any negative values and raise an exception if so. The grades in the list will always be integers ranging from 0 to 100. The function should also provide an option to calculate the average of a specific range of grades within the list, given the start and end indices.
"""

def avg_grade(grades, start_index=None, end_index=None):
    """
    Calculate the average of a list of grades.

    Args:
    grades (list): A list of grades.
    start_index (int, optional): The start index of the range of grades to calculate the average for. Defaults to None.
    end_index (int, optional): The end index of the range of grades to calculate the average for. Defaults to None.

    Returns:
    float: The average of the grades.

    Raises:
    Exception: If the list of grades is empty or contains negative values.
    Exception: If the start or end index is out of range.
    """

    # Check if the list of grades is empty
    if not grades:
        raise Exception("Grades list is empty.")

    # Check if the list contains any negative values
    if any(grade < 0 for grade in grades):
        raise Exception("Grades list should not contain negative values.")

    # If start and end indices are not provided, calculate the average of all grades
    if start_index is None and end_index is None:
        return round(sum(grades) / len(grades))

    # Check if the start or end index is out of range
    if start_index < 0 or end_index >= len(grades):
        raise Exception("Invalid range indices.")

    # Calculate the average of the grades in the specified range
    return round(sum(grades[start_index:end_index + 1]) / (end_index - start_index + 1))