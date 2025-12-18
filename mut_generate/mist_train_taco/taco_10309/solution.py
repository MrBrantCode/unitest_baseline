"""
QUESTION:
Consider Ø(n) as the Euler Totient Function for n. You will be given a positive integer N and you have to find the smallest positive integer n, n <= N for which the ratio n/Ø(n) is maximized.
 
Example 1:
Input:
N = 6
Output:
6
Explanation:
For n = 1, 2, 3, 4, 5 and 6 the values of
the ratio are 1, 2, 1.5, 2, 1.25 and 3
respectively. The maximum is obtained at 6.
Example 2:
Input:
N = 50
Output:
30
Explanation:
For n = 1 to 50, the maximum value of the
ratio is 3.75 which is obtained at n = 30.
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function maximizeEulerRatio() which takes an Integer N as input and returns the smallest positive integer (<= N) which maximizes the ratio n/Ø(n) is maximized.
 
Expected Time Complexity: O(constant)
Expected Auxiliary Space: O(constant)
 
Constraints:
1 <= N <= 10^{12}
"""

def maximize_euler_ratio(N: int) -> int:
    def is_prime(n: int) -> bool:
        i = 2
        while i * i <= n:
            if n % i == 0:
                return False
            i += 1
        return True

    r = 1
    i = 2
    while r * i <= N:
        if is_prime(i):
            r *= i
        i += 1
    return r