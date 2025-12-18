"""
QUESTION:
Initially on a notepad only one character 'A' is present. You can perform two operations on this notepad for each step: 

Copy All: You can copy all the characters present on the notepad (partial copy is not allowed).
Paste: You can paste the characters which are copied last time.




Given a number n. You have to get exactly n 'A' on the notepad by performing the minimum number of steps permitted. Output the minimum number of steps to get n 'A'. 


Example 1:

Input: 3
Output: 3
Explanation:
Intitally, we have one character 'A'.
In step 1, we use Copy All operation.
In step 2, we use Paste operation to get 'AA'.
In step 3, we use Paste operation to get 'AAA'.




Note:

The n will be in the range [1, 1000].
"""

def min_steps_to_get_n_A(n: int) -> int:
    prime_factors = []
    for i in range(2, int(n ** 0.5) + 1):
        while n % i == 0:
            prime_factors.append(i)
            n = n // i
    if n > 1:
        prime_factors.append(n)
    return sum(prime_factors)