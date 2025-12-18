"""
QUESTION:
Alice is a very brilliant student. He considers '4' and '7' as Magic numbers. The numbers containing only magic numbers are also magical. Given a magic number N ,he wants to know what could be the next magical number greater than the given number.

-----Input-----

First line of input contains number of test cases T. For each test case, there is exits only one line containing a magic number N. 

-----Output-----

For each test case,  output a single line containing the next greater magical number.

-----Constraints-----
1<=T<=1000
4<= N<=10^100

-----Example-----
Input:
2
4
47

Output:
7
74
"""

def find_next_magical_number(N: str) -> str:
    """
    Finds the next greater magical number that contains only '4' and '7'.

    Parameters:
    N (str): The input magic number for which we need to find the next magical number.

    Returns:
    str: The next greater magical number.
    """
    def increment_digit(digit):
        return '7' if digit == '4' else '4'

    digits = list(N)
    length = len(digits)

    # Start from the least significant digit and move to the most significant
    for i in range(length - 1, -1, -1):
        if digits[i] == '4':
            digits[i] = '7'
            return ''.join(digits)
        else:
            digits[i] = '4'

    # If all digits were '7', we need to add a new digit '4' at the beginning
    return '4' + ''.join(digits)

# Example usage:
# print(find_next_magical_number("4"))  # Output: "7"
# print(find_next_magical_number("47")) # Output: "74"