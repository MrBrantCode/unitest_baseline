"""
QUESTION:
Write a function `grade_task` that takes a string `submitted_text` as input and returns the points earned for the submission. The function should implement a grading logic that assigns points based on the content of the submitted text. The points earned should be an integer value. The function should not take any additional parameters other than the submitted text.

Function Signature: `def grade_task(submitted_text: str) -> int`

Note: The grading logic is not specified, so it's up to the implementer to decide how to grade the submitted text.
"""

def grade_task(submitted_text: str) -> int:
    """
    Grades a submitted text based on its content and returns the points earned.

    The grading logic is a simple example that counts the number of occurrences 
    of a specific keyword in the submitted text and assigns points based on the count.

    Args:
    submitted_text (str): The text submitted for grading.

    Returns:
    int: The points earned for the submission.
    """
    keyword = "python"
    points = submitted_text.lower().count(keyword) * 5  # Each occurrence of the keyword is worth 5 points
    return points