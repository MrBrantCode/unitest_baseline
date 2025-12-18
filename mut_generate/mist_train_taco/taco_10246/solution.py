"""
QUESTION:
Given two numbers represented by two different arrays A and B. The task is to find the sum array. The sum array is an array representation of addition of two input arrays.
Example 1:
Input:
N = 3, M = 3
A[] = {5, 6, 3}
B[] = {8, 4, 2}
Output: 1 4 0 5
Explanation: As 563 + 842 = 1405.
Example 2:
Input:
N = 6, M = 4 
A[] = {2, 2, 7, 5, 3, 3}
B[] = {4, 3, 3, 8}
Output: 2 3 1 8 7 1
Explanation: As 227533 + 4338 = 231871.
Your Task:  
You don't need to read input or print anything. Your task is to complete the function findSum() which takes the array(vector) of integers a and b as parameters and returns an array denoting the answer.
Expected Time Complexity: O(max(N, M))
Expected Auxiliary Space: O(1)
Constraints:
1 ≤ N ≤ M ≤ 10^{6}
0 ≤ A_{i}, B_{i }≤ 9
No leading zeroes in array A and B.
"""

def array_sum(a: list[int], b: list[int]) -> list[int]:
    # Convert the arrays to strings to form the numbers
    num1 = ''.join(map(str, a))
    num2 = ''.join(map(str, b))
    
    # Calculate the sum of the two numbers
    sum_num = int(num1) + int(num2)
    
    # Convert the sum back to a list of integers
    return [int(digit) for digit in str(sum_num)]