"""
QUESTION:
Given an integer n, find the number of positive integers whose factorial ends with n zeros. 
 
Example 1:
Input:
N = 1
Output: 5
Explanation:
5! = 120, 6! = 720, 7! = 5040, 
8! = 40320 and 9! = 362880.
 
Example 2:
Input:
N = 5
Output: 0
Your Task:  
You don't need to read input or print anything. Your task is to complete the function countZeroes() which takes the integer N as input parameters and returns the count of positive numbers whose factorial ends with N zeros.
Expected Time Complexity: O(log(n))
Expected Auxiliary Space: O(1)
 
Constraints:
1<=N<=1000
"""

def count_factorials_with_n_trailing_zeros(n: int) -> int:
    def cal(n: int) -> int:
        count = 0
        i = 5
        while True:
            if n // i >= 1:
                count += n // i
                i *= 5
            else:
                break
        return count

    low = 1
    high = n * 5
    ans = 0
    while low <= high:
        mid = low + (high - low) // 2
        temp = cal(mid)
        if temp == n:
            ans = mid
            break
        elif temp > n:
            high = mid - 1
        else:
            low = mid + 1
    
    if ans == 0:
        return 0
    return 5