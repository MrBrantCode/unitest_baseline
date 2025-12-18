"""
QUESTION:
Create a function called `switch` that takes a single character grade as input and returns the corresponding grade value. The grade value mapping is as follows: 'A' to 4.0, 'B' to 3.0, 'C' to 2.0, 'D' to 1.0, and any other grade to 0.
"""

def switch(grade):
    """
    This function takes a single character grade as input and returns the corresponding grade value.
    
    Parameters:
    grade (char): A single character grade
    
    Returns:
    float: The grade value corresponding to the input grade
    """
    grade_values = {
        'A': 4.0,
        'B': 3.0,
        'C': 2.0,
        'D': 1.0
    }
    return grade_values.get(grade, 0.0)