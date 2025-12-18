"""
QUESTION:
Given an array A comprising of N non-zero, positive integers and an integer X, find the bitwise OR of all such elements in the array that are a multiple of X. The result of OR operation should be  in decimal form. If no multiple of X is found, the answer should be 0.
Example 1:
Input:
N = 4 , X = 2
A = {3 , 4 , 3 , 9}
Output:
4
Explanation:
Only multiple of 2 in array is 4.
Hence it is printed.
Example 2:
Input:
N = 5 , X = 3
A = {9 , 3 , 1 , 6 , 1}
Output:
15
Explanation:
Multiples of 3 in array are 9,3 and 6.
Their OR value is 15 and thus the Output.
Example 3:
Input:
N = 3 , X = 8
A = {1,2,3}
Output:
0
Explanation:
There are no multiples of 8 in the array.
So, Output is 0.
Your Task:
You don't need to read input or print anything. Your task is to complete the function factorOrMultiple() which takes integers N and X, and an Array A as input and returns the answer.
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)
Constraints:
1 <= N,X,A[i] <= 10^{5}
"""

def factor_or_multiple(N, X, A):
    multiples = [i for i in A if i % X == 0]
    result = 0
    for num in multiples:
        result |= num
    return result