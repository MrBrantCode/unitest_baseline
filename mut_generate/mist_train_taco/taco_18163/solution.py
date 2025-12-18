"""
QUESTION:
Write a program to calculate _{n}P^{r}. _{n}P^{r} represents n permutation r and value of _{n}P^{r }is (n!) / (n-r)!.
Example 1:
Input: n = 2, r = 1
Output: 2
Explaination: 2!/(2-1)! = 2!/1! = (2*1)/1 = 2.
Example 2:
Input: n = 3, r = 3
Output: 6
Explaination: 3!/(3-3)! = 3!/0! = 6/1 = 6.
Your Task:
You do not need to read input or print anything. Your task is to complete the function nPr() which takes n and r as input parameters and returns _{n}P^{r} .
Expected Time Complexity: O(n)
Expected Auxiliary Space: O(1)
Constraints:
1 ≤ n, r ≤ 20
"""

def calculate_permutation(n: int, r: int) -> int:
    """
    Calculate the permutation value nPr, which is defined as (n!) / (n-r)!.

    Parameters:
    n (int): The total number of items.
    r (int): The number of items to choose.

    Returns:
    int: The value of nPr.
    """
    # Calculate factorial of n
    factorial_n = 1
    for i in range(1, n + 1):
        factorial_n *= i
    
    # Calculate factorial of (n-r)
    factorial_n_minus_r = 1
    for j in range(1, n - r + 1):
        factorial_n_minus_r *= j
    
    # Calculate nPr
    permutation_value = factorial_n // factorial_n_minus_r
    
    return permutation_value