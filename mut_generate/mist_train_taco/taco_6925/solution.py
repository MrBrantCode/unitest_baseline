"""
QUESTION:
Vitaly is a very weird man. He's got two favorite digits a and b. Vitaly calls a positive integer good, if the decimal representation of this integer only contains digits a and b. Vitaly calls a good number excellent, if the sum of its digits is a good number.

For example, let's say that Vitaly's favourite digits are 1 and 3, then number 12 isn't good and numbers 13 or 311 are. Also, number 111 is excellent and number 11 isn't. 

Now Vitaly is wondering, how many excellent numbers of length exactly n are there. As this number can be rather large, he asks you to count the remainder after dividing it by 1000000007 (10^9 + 7).

A number's length is the number of digits in its decimal representation without leading zeroes.


-----Input-----

The first line contains three integers: a, b, n (1 ≤ a < b ≤ 9, 1 ≤ n ≤ 10^6).


-----Output-----

Print a single integer — the answer to the problem modulo 1000000007 (10^9 + 7).


-----Examples-----
Input
1 3 3

Output
1

Input
2 3 10

Output
165
"""

def count_excellent_numbers(a, b, n, mod=1000000007):
    # Helper function to generate good numbers
    def generate_good_numbers(a, b):
        s = set()
        for x in range(2, 1 << 8):
            z = 0
            while x > 1:
                z = z * 10 + (a, b)[x & 1]
                x >>= 1
            s.add(z)
        return s

    # Generate factorial values modulo mod
    def factorial_mod(n, mod):
        f = [1] * (n + 1)
        for i in range(1, n + 1):
            f[i] = f[i - 1] * i % mod
        return f

    # Generate good numbers set
    s = generate_good_numbers(a, b)
    
    # Generate factorial values
    f = factorial_mod(n, mod)
    
    # Calculate the number of excellent numbers
    ans = 0
    for x in range(n + 1):
        if x * a + (n - x) * b in s:
            ans += pow(f[x] * f[n - x], mod - 2, mod)
            ans %= mod
    
    return ans * f[n] % mod