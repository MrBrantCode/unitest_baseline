"""
QUESTION:
Chef calls a number *lucky* if it contains the digit 7 at least once. 

Given a number X, determine if it is a *lucky* number or not.

------ Input Format ------ 

- The first line contains a single integer T — the number of test cases. Then the test cases follow.
- The first and only line of each test case contains an integer X — the number mentioned in the problem statement.

------ Output Format ------ 

For each test case, output YES if X is a lucky number. Otherwise, output NO.

You may print each character of YES and NO in uppercase or lowercase (for example, yes, yEs, Yes will be considered identical).

------ Constraints ------ 

$1 ≤ T ≤ 1000$
$1 ≤X ≤10^{9}$

----- Sample Input 1 ------ 
4
6
478
2090
77777

----- Sample Output 1 ------ 
NO
YES
NO
YES

----- explanation 1 ------ 
Test Case 1: The number $6$ is not lucky since it does not contain the digit $7$.

Test Case 2: The number $478$ is lucky since it contains the digit $7$ at least once.

Test Case 3: The number $2090$ is not lucky since it does not contain the digit $7$.

Test Case 4: The number $77777$ is lucky since it contains the digit $7$ at least once.
"""

def is_lucky_number(number: str) -> bool:
    """
    Determines if a given number contains the digit '7'.

    Parameters:
    number (str): The number to be checked.

    Returns:
    bool: True if the number contains the digit '7', otherwise False.
    """
    return '7' in number