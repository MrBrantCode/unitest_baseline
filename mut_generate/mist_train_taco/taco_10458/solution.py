"""
QUESTION:
Given two function, one is h(x) which is the product of all the number in an array A[ ] having size N and another
function f(x) which denotes the GCD of all the numbers in an array. Your task is to find the value of  h(x)^{f(x)}.
Note: Since the answer can be very large, use modulo 10^{9}+7.
Example 1:
Input:
N = 2, A[] = {2, 4}
Output:
64
Explanation:
h(x) = 8, f(x) = 2, Therefore, the
answer is 8^{2} = 64.
Example 2:
Input:
N = 3, A[] = {1, 3, 7}
Output:
21
Explanation:
h(x) = 21, f(x) = 1, Therefore, the
answer is 21^{1} = 21.
Your Task:
You don't need to read input or print anything. Your task is to complete the function getVal() which takes an Integer N and an array of integers A[] as input and returns the answer.
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)
Constraints:
1 <= N <= 10^{5}
1 <= A[i] <= 10^{5}
"""

def calculate_value(N, A):
    m = 1000000007

    def gcd(a, b):
        if a == 0:
            return b
        return gcd(b % a, a)
    
    multiple = 1
    for i in A:
        multiple = multiple * i % m
    
    g = A[0]
    for i in A[1:]:
        g = gcd(i, g)
    
    return pow(multiple, g, m)