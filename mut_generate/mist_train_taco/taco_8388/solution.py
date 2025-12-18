"""
QUESTION:
Given a string of words and numbers. Extract the expression including: 
1. the operator: either addition or subtraction
2. the two numbers that we are operating on

Return the result of the calculation.

Example:

"Panda has 48 apples and loses 4" returns 44

"Jerry has 34 apples and gains 6" returns 40

"loses" and "gains" are the only two words describing operators.

Should be a nice little kata for you :)

Note:
No fruit debts nor bitten apples = The numbers are integers and no negatives
"""

def calculate_expression(s: str) -> int:
    # Extract the numbers from the string
    numbers = [int(i) for i in s.split() if i.isdigit()]
    
    # Determine the operator and perform the corresponding calculation
    if 'gains' in s:
        return sum(numbers)
    elif 'loses' in s:
        return numbers[0] - numbers[1]
    else:
        raise ValueError("The string does not contain a valid operator ('gains' or 'loses')")