"""
QUESTION:
You are given two integers a and b. In one turn, you can do one of the following operations: 

  * Take an integer c (c > 1 and a should be divisible by c) and replace a with a/c; 
  * Take an integer c (c > 1 and b should be divisible by c) and replace b with b/c. 



Your goal is to make a equal to b using exactly k turns.

For example, the numbers a=36 and b=48 can be made equal in 4 moves: 

  * c=6, divide b by c ⇒ a=36, b=8; 
  * c=2, divide a by c ⇒ a=18, b=8; 
  * c=9, divide a by c ⇒ a=2, b=8; 
  * c=4, divide b by c ⇒ a=2, b=2. 



For the given numbers a and b, determine whether it is possible to make them equal using exactly k turns.

Input

The first line contains one integer t (1 ≤ t ≤ 10^4). Then t test cases follow.

Each test case is contains three integers a, b and k (1 ≤ a, b, k ≤ 10^9).

Output

For each test case output: 

  * "Yes", if it is possible to make the numbers a and b equal in exactly k turns; 
  * "No" otherwise. 



The strings "Yes" and "No" can be output in any case.

Example

Input


8
36 48 2
36 48 3
36 48 4
2 8 1
2 8 2
1000000000 1000000000 1000000000
1 2 1
2 2 1


Output


YES
YES
YES
YES
YES
NO
YES
NO
"""

import math

def prime_factors_count(n):
    count = 0
    while n % 2 == 0:
        count += 1
        n = n // 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            count += 1
            n = n // i
    if n > 2:
        count += 1
    return count

def gcd(a, b):
    if a == 0 or b == 0:
        return max(a, b)
    if a > b:
        a %= b
    else:
        b %= a
    return gcd(a, b)

def can_make_equal_in_k_turns(a, b, k):
    if a > b:
        a, b = b, a
    
    godNM = gcd(a, b)
    gcdNM = 0
    
    gcdNM += prime_factors_count(a // godNM)
    gcdNM += prime_factors_count(b // godNM)
    gcdNM += prime_factors_count(godNM)
    
    if 1 <= k <= gcdNM and a != b and (a % b == 0):
        return 'Yes'
    elif 2 <= k <= gcdNM:
        return 'Yes'
    else:
        return 'No'