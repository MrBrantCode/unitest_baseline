"""
QUESTION:
Levko loves permutations very much. A permutation of length n is a sequence of distinct positive integers, each is at most n.

Let’s assume that value gcd(a, b) shows the greatest common divisor of numbers a and b. Levko assumes that element p_{i} of permutation p_1, p_2, ... , p_{n} is good if gcd(i, p_{i}) > 1. Levko considers a permutation beautiful, if it has exactly k good elements. Unfortunately, he doesn’t know any beautiful permutation. Your task is to help him to find at least one of them.


-----Input-----

The single line contains two integers n and k (1 ≤ n ≤ 10^5, 0 ≤ k ≤ n).


-----Output-----

In a single line print either any beautiful permutation or -1, if such permutation doesn’t exist.

If there are multiple suitable permutations, you are allowed to print any of them.


-----Examples-----
Input
4 2

Output
2 4 3 1
Input
1 1

Output
-1



-----Note-----

In the first sample elements 4 and 3 are good because gcd(2, 4) = 2 > 1 and gcd(3, 3) = 3 > 1. Elements 2 and 1 are not good because gcd(1, 2) = 1 and gcd(4, 1) = 1. As there are exactly 2 good elements, the permutation is beautiful.

The second sample has no beautiful permutations.
"""

def find_beautiful_permutation(n, k):
    # Initialize the permutation with numbers from 1 to n
    ans = [i + 1 for i in range(n)]
    
    # If k is equal to n, it's impossible to have a beautiful permutation
    if k == n:
        return -1
    
    # Calculate the number of elements that need to be swapped
    temp = n - k
    
    # If there's only one element to swap, return the original permutation
    if temp == 1:
        return ans
    
    # If the number of elements to swap is odd, reduce it by 1 to make it even
    if temp % 2 == 1:
        temp -= 1
    
    # Swap pairs of elements to ensure gcd(i, p_i) > 1 for k elements
    for i in range(temp // 2):
        j = 2 * i
        m = j + 1
        ans[j], ans[m] = ans[m], ans[j]
    
    return ans