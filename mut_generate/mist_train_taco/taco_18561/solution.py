"""
QUESTION:
Given an array of n integers. Find the minimum positive number to be inserted in array, so that sum of all elements of array becomes prime. If sum is already prime, then return 0.
 
Example 1:
Input:
N=5
arr[] = { 2, 4, 6, 8, 12 }
Output:  5
Explanation: 
The sum of the array is 32 ,we can add
5 to this to make it 37 which is a
prime number .
Example 2:
Input:
N=3
arr[] = { 1, 5, 7 }
Output:  0 
Explanation: 
The sum of the array is 13 
which is already prime. 
Your Task:
You don't need to read input or print anything. Your task is to complete the function minNumber() that takes array arr and integer N as input parameters and returns the minimum positive number to be inserted in the array so as to make it's sum a prime number.
 
Expected Time Complexity: O(N log(log N))
Expected Auxiliary Space: O(1).
 
Constraints:
1 ≤ N ≤ 10^{5}
"""

def isprime(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def minNumber(arr, N):
    a = sum(arr)
    i = 0
    while True:
        if isprime(a + i):
            return i
        i += 1