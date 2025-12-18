"""
QUESTION:
Smart number is a number which has at least three distinct prime factors. Given a number n, find the n’th smart number.
 
Example 1: 
Input:
n = 1
Output:
30
Explanation:
30 is the first number which has 3 prime
factors. So, it's the first Smart Number.
Example 2: 
Input:
n = 2
Output:
42
Explanation:
42 = 2*3*7, 42 is the second number which
has 3 prime factors or more. So, it's the
second Smart Number.
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function nthSmartNum() which takes an Integer n as input and returns the n'th Smart Number.
 
Expected Time Complexity: O(nloglogn)
Expected Auxiliary Space: O(n)
 
Constraints:
1 <= n <= 10^{5}
"""

def nth_smart_number(n: int) -> int:
    maxx = 100000
    primes = [0] * maxx
    result = []
    
    for i in range(2, maxx):
        if primes[i] == 0:
            primes[i] = 1
            j = i * 2
            while j < maxx:
                primes[j] -= 1
                if primes[j] + 3 == 0:
                    result.append(j)
                j = j + i
    
    result.sort()
    return result[n - 1]