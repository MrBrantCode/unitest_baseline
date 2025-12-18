"""
QUESTION:
Given an integer N, list all the divisors of N (excluding N) in sorted order. Find the number formed by performing the XOR operation on each divisor in the list.
Example 1:
Input: N = 10
Output:
1 2 5
6
Explanation:
All the proper divisors are 1, 2 and 5.
1 XOR 2 XOR 5 = 6
Example 2:
Input: N = 8
Output:
1 2 4
7
Explanation:
All the proper divisors are 1, 2 and 4.
1 XOR 2 XOR 4 = 7
Your Task:
You don't need to read or print anything. Your task is to complete the function xor_play() which takes N as input parameter and returns a list of integers containing all the proper divisors in sorted order. The last element in the list must contain the XOR result.
Expected Time Complexity: O(sqrt(N))
Expected Space Complexity: O(K) where K is the number of divisors of N.
 
Constraints:
1 <= N <= 10^{9}
"""

def find_divisors_and_xor(n: int) -> list[int]:
    if n == 1:
        return [0]
    
    result = [1]
    i = 2
    while i * i <= n:
        if n % i == 0:
            result.append(i)
            if i != n // i:
                result.append(n // i)
        i += 1
    
    result.sort()
    xor_result = 0
    for d in result:
        xor_result ^= d
    
    result.append(xor_result)
    return result