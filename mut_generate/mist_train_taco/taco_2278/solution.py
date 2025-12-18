"""
QUESTION:
Given an integer N, the task is to find out the count of numbers M that satisfy the condition M + sum(M) + sum (sum(M)) = N, where sum(M) denotes the sum of digits in M.
Example 1:
Input: N = 9
Output: 1
Explaination: Only 1 positive integer satisfies 
the condition that is 3, 3 + sum(3) + sum(sum(3))
= 3 + 3 + 3 = 9. 
Example 2:
Input: N = 9939
Output: 4
Explaination: M can be 9898, 9907, 9910 and 9913. 
9898 + sum(9898) + sum(sum(9898)) = 9898 + 34 + 7 
= 9939. 
9907 + sum(9907) + sum(sum(9907)) = 9907 + 25 + 7 
= 9939. 
9910 + sum(9910) + sum(sum(9910)) = 9910 + 19 + 10 
= 9939. 
9913 + sum(9913) + sum(sum(9913)) = 9913 + 22 + 4 
= 9939. 
Your Task:
You do not need to read input or print anything. Your task is to complete the function countOfNumbers() which takes the value N and returns the count of numbers M that satisfy the given condition
Expected Time Complexity: O(logn)
Expected Auxiliary Space: O(1)
Constraints:
1 ≤ N ≤ 10^{9}
"""

def sum_of_digits(n):
    """Helper function to calculate the sum of digits of a number."""
    s = 0
    while n != 0:
        s += n % 10
        n = n // 10
    return s

def count_valid_numbers(N):
    """
    Function to count the number of valid integers M such that:
    M + sum(M) + sum(sum(M)) = N
    
    Parameters:
    N (int): The target number.
    
    Returns:
    int: The count of valid numbers M.
    """
    count = 0
    lower_bound = N - 100
    if lower_bound < 0:
        lower_bound = 0
    
    for i in range(lower_bound, N + 1):
        if i + sum_of_digits(i) + sum_of_digits(sum_of_digits(i)) == N:
            count += 1
    
    return count