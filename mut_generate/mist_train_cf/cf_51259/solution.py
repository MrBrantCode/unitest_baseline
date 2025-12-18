"""
QUESTION:
Estimate the number of seniors who will enroll in a graduate degree program given the total number of seniors and the ratio of seniors progressing to graduate school. 

Function name: expected_grad_students 
Information: 
- Total number of seniors (total_seniors) 
- Ratio of seniors who will progress to attend graduate school (grad_school_ratio) 
Restriction: 
- The total number of seniors and the ratio of seniors progressing to graduate school should be provided as input.
"""

def expected_grad_students(total_seniors, grad_school_ratio):
    """
    Estimates the number of seniors who will enroll in a graduate degree program.

    Args:
        total_seniors (int): The total number of seniors.
        grad_school_ratio (float): The ratio of seniors who will progress to attend graduate school.

    Returns:
        float: The estimated number of seniors who will enroll in a graduate degree program.
    """
    return total_seniors * grad_school_ratio