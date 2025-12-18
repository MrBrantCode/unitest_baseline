"""
QUESTION:
You will be given an array A of N non-negative integers. Your task is to find the rightmost non-zero digit in the product of array elements.
Example 1:
Input:
N = 4, A = {3, 23, 30, 45}
Output:
5
Explanation:
Product of these numbers 
are 93150.Rightmost 
non-zero digit is 5.
Example 2:
Input:
N = 5, A = {1, 2, 3, 4, 5}
Output:
2
Explanation:
Product of these numbers 
are 120. Rightmost 
non-zero digit is 2.
Your Task:
You don't need to read input or print anything. Your task is to complete the function rightmostNonZeroDigit() which takes an array A and returns the rightmost non-zero digit in the product of array elements, if there is no right most non zero digit, then return -1.
Expected Time Complexity: O(N*logN)
Expected Auxiliary Space: O(N)
Constraints:
1 ≤ N ≤ 10^{5}
0 ≤ A[i] ≤ 10^{5}
"""

def rightmost_non_zero_digit(N, A):
    cnt5 = 0
    cnt2 = 0
    r = 1
    
    for i in range(N):
        if A[i] == 0:
            r = 0
            break
        while A[i] % 5 == 0:
            A[i] //= 5
            cnt5 += 1
        while A[i] % 2 == 0:
            A[i] //= 2
            cnt2 += 1
        r = r * A[i] % 10
    
    if r == 0:
        return -1
    
    k = min(cnt2, cnt5)
    cnt2 -= k
    cnt5 -= k
    
    while cnt5 > 0:
        r = r * 5 % 10
        cnt5 -= 1
    
    while cnt2 > 0:
        r = r * 2 % 10
        cnt2 -= 1
    
    return r