"""
QUESTION:
I conducted an exit poll of the shopping amount at a department store. Create a program that takes the shopping amount data as input, calculates the average shopping amount per person, and outputs it. The number of people surveyed shall be 100,000 or less, and the shopping amount per person shall not exceed 1 million yen.



Input

The input is given in the following format:


n
v1
v2
::
vn


The first line gives the number of people surveyed n, and the following n lines give the integer vi representing the purchase amount of the ith person.

Output

Please output the average shopping amount (integer: rounded down to the nearest whole number) on one line.

Example

Input

6
12300
5600
33800
0
26495
52000


Output

21699
"""

def calculate_average_shopping_amount(shopping_amounts: list[int]) -> int:
    """
    Calculate the average shopping amount per person from a list of shopping amounts.

    Parameters:
    shopping_amounts (list[int]): A list of integers where each integer represents the shopping amount of a person.

    Returns:
    int: The average shopping amount per person, rounded down to the nearest whole number.
    """
    if not shopping_amounts:
        return 0
    
    total_sum = sum(shopping_amounts)
    average = total_sum // len(shopping_amounts)
    return average