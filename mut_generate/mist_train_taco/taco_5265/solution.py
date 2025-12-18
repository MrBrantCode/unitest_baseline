"""
QUESTION:
Tom is very weak at maths, his teacher gave him a simple problem of dividing two numbers but as usual Tom is having difficulty solving the problem. Can you help tom solve the problem ?

Teacher has given him 3 numbers a, b and c. The task is to divide a by b and write the answer upto c decimal places.

Input:

The first line of input contains an integer T denoting the number of test cases.
Each line of test case contains 3 numbers a, b and c as described in the question.

Output:

For each test case, output the required division of a/b upto c decimal places.

Constraints:

1 ≤ T ≤ 100,

1 ≤ a,b ≤ 100000

0 ≤ c ≤ 100000

SAMPLE INPUT
3
21 4 0
5 4 3
22 7 10

SAMPLE OUTPUT
5
1.250
3.1428571428
"""

def divide_and_round(a: int, b: int, c: int) -> str:
    """
    Divides the number 'a' by 'b' and rounds the result to 'c' decimal places.

    Parameters:
    a (int): The numerator.
    b (int): The denominator.
    c (int): The number of decimal places to round to.

    Returns:
    str: The result of the division rounded to 'c' decimal places.
    """
    if c == 0:
        return str(a // b)
    
    result = str(a / b)
    if '.' not in result:
        result += '.'
    
    integer_part, decimal_part = result.split('.')
    decimal_part += '0' * (c - len(decimal_part))
    
    return f"{integer_part}.{decimal_part[:c]}"