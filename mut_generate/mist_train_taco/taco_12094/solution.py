"""
QUESTION:
Given an integer k, return the minimum number of Fibonacci numbers whose sum is equal to k. The same Fibonacci number can be used multiple times.
The Fibonacci numbers are defined as:

F1 = 1
F2 = 1
Fn = Fn-1 + Fn-2 for n > 2.

It is guaranteed that for the given constraints we can always find such Fibonacci numbers that sum up to k.
 
Example 1:
Input: k = 7
Output: 2 
Explanation: The Fibonacci numbers are: 1, 1, 2, 3, 5, 8, 13, ... 
For k = 7 we can use 2 + 5 = 7.
Example 2:
Input: k = 10
Output: 2 
Explanation: For k = 10 we can use 2 + 8 = 10.

Example 3:
Input: k = 19
Output: 3 
Explanation: For k = 19 we can use 1 + 5 + 13 = 19.

 
Constraints:

1 <= k <= 10^9
"""

def find_min_fibonacci_numbers(k: int) -> int:
    # Generate Fibonacci numbers up to k
    fib = [1, 1]
    i = 1
    temp = fib[0] + fib[1]
    while temp <= k:
        fib.append(temp)
        i += 1
        temp = fib[i] + fib[i - 1]
    
    # Find the minimum number of Fibonacci numbers that sum to k
    ans = 0
    j = -1
    while k > 0:
        temp = fib[j]
        j -= 1
        if temp <= k:
            ans += 1
            k -= temp
    
    return ans