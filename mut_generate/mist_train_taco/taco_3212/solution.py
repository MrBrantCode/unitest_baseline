"""
QUESTION:
Find the minimum number with the given sum of digits $s$ such that all digits in it are distinct (i.e. all digits are unique).

For example, if $s=20$, then the answer is $389$. This is the minimum number in which all digits are different and the sum of the digits is $20$ ($3+8+9=20$).

For the given $s$ print the required number.


-----Input-----

The first line contains an integer $t$ ($1 \le t \le 45$) — the number of test cases.

Each test case is specified by a line that contains the only integer $s$ ($1 \le s \le 45$).


-----Output-----

Print $t$ integers — the answers to the given test cases.


-----Examples-----

Input
4
20
8
45
10
Output
389
8
123456789
19


-----Note-----

None
"""

def find_min_number_with_distinct_digits(s: int) -> int:
    """
    Finds the minimum number with distinct digits that sum up to the given integer `s`.

    Parameters:
    s (int): The sum of the digits required.

    Returns:
    int: The minimum number with distinct digits that sum up to `s`.
    """
    if s > 45:
        raise ValueError("The sum of digits cannot exceed 45.")
    
    reverse = ''
    sum1 = 0
    while sum1 != s:
        digits = '987654321'
        for x in digits:
            if sum1 + int(x) > s:
                digits = digits[digits.index(x) + 1:len(digits)]
            else:
                digits = digits[digits.index(x) + 1:len(digits)]
                reverse += str(x)
                sum1 += int(x)
    
    real = ''
    for y in range(-1, -1 * (len(reverse) + 1), -1):
        real += reverse[y]
    
    return int(real)