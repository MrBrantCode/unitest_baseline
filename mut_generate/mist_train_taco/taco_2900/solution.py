"""
QUESTION:
Given a number N. The task is to find the N^{th} catalan number.
The first few Catalan numbers for N = 0, 1, 2, 3, … are 1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862, …
Catalan Number for N is equal to the number of expressions containing N pairs of paranthesis that are correct matched, i.e., for each of the N '(' there exist N ')' on there right and vice versa.
Note: Positions start from 0 as shown above.
Example 1:
Input:
N = 5
Output: 42
Example 2:
Input:
N = 4
Output: 14
Your Task:
Complete findCatalan() function that takes n as an argument and returns the N^{th} Catalan number. The output is printed by the driver code.
Expected Time Complexity: O(N).
Expected Auxiliary Space: O(N).
Constraints:
1 <= N <= 100
"""

def find_catalan(n: int) -> int:
    """
    Function to find the Nth Catalan number.

    Parameters:
    n (int): The position of the Catalan number to be found.

    Returns:
    int: The Nth Catalan number.
    """
    if n == 0:
        return 1
    
    table = [1] * (n + 1)
    for i in range(1, n + 1):
        x = 1
        y = 1
        for j in range(2, i + 1):
            x *= (i + j)
            y *= j
        table[i] = x // y
    
    return table[n]