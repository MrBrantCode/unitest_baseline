"""
QUESTION:
You will be given a positive integer N. Your task is to find the number of positive integers K ≤ N such that K is not divisible by any number among the set {2,3,4,5,6,7,8,9,10}.
 
Example 1:
Input:
N = 11
Output:
2
Explanation:
1 and 11 are the only possible solutions.
Example 2:
Input:
N = 2
Output:
1
Explanation:
1 is the only possible solution.
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function noOfNumbers() which takes an Integer N as input and returns the answer.
 
Expected Time Complexity: O(1)
Expected Auxiliary Space: O(1)
 
Constraints:
1 <= N <= 10^{18}
"""

def count_non_divisible(N: int) -> int:
    a = N // 7 - N // 14 - N // 21 - N // 35 + N // 42 - N // 210 + N // 70 + N // 105
    b = N // 5 - N // 10 - N // 15 + N // 30
    c = N // 3 - N // 6
    d = N // 2
    return N - (a + b + c + d)