"""
QUESTION:
Given an array of natural numbers count the sum of its proper divisors for every element in the array.
Example 1:
Input:
N = 3
arr = {2, 4, 3}
Output: {1, 3, 1}
Explaination: 
divisor of 2 is 1.
divisors of 4 is 1, 2.
divisor of 3 is 1.
Example 2:
Input:
N = 3
Arr = {2, 4, 1}
Output: {1, 3, 0}
Explaination: 
Proper divisor of 2 is 1.
Proper divisors of 4 is 1, 2.
Your Task:
You don't need to read input or print anything. Your task is to complete the function sumOfProperDivisors() which takes the array arr[] and its size N as input parameters and returns the sum of its proper divisors for every element in the array.
Expected Time Complexity: O(NlogN)
Expected Auxiliary Space: O(N)
Constraints:
1 ≤ N ≤ 100
1 ≤ arr[i] ≤ 100
"""

def sum_of_proper_divisors(arr, N):
    result = []
    for num in arr:
        sum_divisors = 0
        for j in range(1, num):
            if num % j == 0:
                sum_divisors += j
        result.append(sum_divisors)
    return result