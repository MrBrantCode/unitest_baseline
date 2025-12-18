"""
QUESTION:
Given an array A[ ] of N numbers, your task is to find LCM of it modulo 1000000007
Example 1: 
Input:
N = 4
A = {1 , 2 , 8 , 3}
Output:
24
Explanation:
LCM of the given array is 24.
24 % 1000000007 = 24
Example 2: 
Input:
N = 2
A = {1 , 8}
Output:
8
Explanation:
LCM of the given array is 8.
Your Task:
You don't need to read input or print anything. Your task is to complete the function lcmOfArray() which takes an Integer N and an Array A as input and returns the answer.
Expected Time Complexity: O(N*log(N))
Expected Auxiliary Space: O(1)
Constraints:
1 <= N <= 10^{5}
1 <= A[i] <= 10^{5}
"""

def calculate_lcm_of_array(arr, mod=1000000007):
    def gcd(num1, num2):
        while num2:
            num1, num2 = num2, num1 % num2
        return num1
    
    def lcm(num1, num2):
        return (num1 * num2) // gcd(num1, num2)
    
    if not arr:
        return 0
    
    lcm_result = arr[0]
    for num in arr[1:]:
        lcm_result = lcm(lcm_result, num)
        if lcm_result >= mod:
            lcm_result %= mod
    
    return lcm_result