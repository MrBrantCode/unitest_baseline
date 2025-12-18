"""
QUESTION:
Implement a function called `sponsor_exam_fees` that determines the sponsorship amount for a programming certification exam based on the number of attempts taken to pass the exam. The function should follow these rules: 
- If the programmer passes the exam on the first attempt, the company should fully sponsor the exam fees.
- If the programmer passes the exam on the second attempt, the company should sponsor 50% of the exam fees.
- If the programmer fails the exam after two attempts, the programmer should pay the full exam fees, including for the first two attempts.
- The function should take the exam fees and the number of attempts taken to pass the exam as inputs.
"""

def sponsor_exam_fees(exam_fees, attempts):
    """
    This function determines the sponsorship amount for a programming certification exam based on the number of attempts taken to pass the exam.

    Parameters:
    exam_fees (float): The total fees of the exam.
    attempts (int): The number of attempts taken to pass the exam.

    Returns:
    float: The sponsorship amount the company will provide.
    """

    if attempts == 1:
        # If the programmer passes the exam on the first attempt, the company should fully sponsor the exam fees.
        return exam_fees
    elif attempts == 2:
        # If the programmer passes the exam on the second attempt, the company should sponsor 50% of the exam fees.
        return exam_fees * 0.5
    else:
        # If the programmer fails the exam after two attempts, the programmer should pay the full exam fees, including for the first two attempts.
        return 0