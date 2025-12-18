"""
QUESTION:
Create a function `convert_to_grade` that takes a numeric score between 1 and 100 as input, converts it into its corresponding alphabetic grade representation along with a descriptor, and returns the grade and descriptor. The conversion rules are as follows: 
- 'A' and "Excellent" for scores 90 and above,
- 'B' and "Good" for scores between 80 and 89,
- 'C' and "Average" for scores between 70 and 79,
- 'D' and "Poor" for scores between 60 and 69,
- 'E' and "Fail" for scores below 60. 

Additionally, raise an exception if the input score is outside the range of 1 to 100.
"""

def convert_to_grade(score):
    """
    Converts a numeric score between 1 and 100 into its corresponding 
    alphabetic grade representation along with a descriptor.

    Args:
    score (int): A numeric score between 1 and 100.

    Returns:
    tuple: A tuple containing the grade and descriptor.

    Raises:
    Exception: If the input score is outside the range of 1 to 100.
    """

    if score < 1 or score > 100:
        raise Exception("Score should be between 1 and 100.")
    elif score >= 90:
        return 'A', "Excellent"
    elif score >= 80:
        return 'B', "Good"
    elif score >= 70:
        return 'C', "Average"
    elif score >= 60:
        return 'D', "Poor"
    else:
        return 'E', "Fail"