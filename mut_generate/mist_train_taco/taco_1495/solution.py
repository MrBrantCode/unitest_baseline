"""
QUESTION:
Limak is a little polar bear. He doesn't have many toys and thus he often plays with polynomials.

He considers a polynomial valid if its degree is n and its coefficients are integers not exceeding k by the absolute value. More formally:

Let a0, a1, ..., an denote the coefficients, so <image>. Then, a polynomial P(x) is valid if all the following conditions are satisfied:

  * ai is integer for every i; 
  * |ai| ≤ k for every i; 
  * an ≠ 0. 



Limak has recently got a valid polynomial P with coefficients a0, a1, a2, ..., an. He noticed that P(2) ≠ 0 and he wants to change it. He is going to change one coefficient to get a valid polynomial Q of degree n that Q(2) = 0. Count the number of ways to do so. You should count two ways as a distinct if coefficients of target polynoms differ.

Input

The first line contains two integers n and k (1 ≤ n ≤ 200 000, 1 ≤ k ≤ 109) — the degree of the polynomial and the limit for absolute values of coefficients.

The second line contains n + 1 integers a0, a1, ..., an (|ai| ≤ k, an ≠ 0) — describing a valid polynomial <image>. It's guaranteed that P(2) ≠ 0.

Output

Print the number of ways to change one coefficient to get a valid polynomial Q that Q(2) = 0.

Examples

Input

3 1000000000
10 -9 -3 5


Output

3


Input

3 12
10 -9 -3 5


Output

2


Input

2 20
14 -7 19


Output

0

Note

In the first sample, we are given a polynomial P(x) = 10 - 9x - 3x2 + 5x3.

Limak can change one coefficient in three ways:

  1. He can set a0 = - 10. Then he would get Q(x) = - 10 - 9x - 3x2 + 5x3 and indeed Q(2) = - 10 - 18 - 12 + 40 = 0. 
  2. Or he can set a2 = - 8. Then Q(x) = 10 - 9x - 8x2 + 5x3 and indeed Q(2) = 10 - 18 - 32 + 40 = 0. 
  3. Or he can set a1 = - 19. Then Q(x) = 10 - 19x - 3x2 + 5x3 and indeed Q(2) = 10 - 38 - 12 + 40 = 0. 



In the second sample, we are given the same polynomial. This time though, k is equal to 12 instead of 109. Two first of ways listed above are still valid but in the third way we would get |a1| > k what is not allowed. Thus, the answer is 2 this time.
"""

def count_ways_to_make_polynomial_zero_at_two(n, k, coefficients):
    def convert_to_binary(coef):
        res = []
        n = len(coef)
        carry = 0
        i = 0
        while i < n + 1000:
            if i >= n and (not carry):
                break
            cur = carry
            if i < n:
                cur += coef[i]
            mod = cur % 2
            div = cur // 2
            res.append(mod)
            carry = div
            i += 1
        return (res, carry)

    (b, carry) = convert_to_binary(coefficients)
    ref = False
    if carry < 0:
        (b, carry) = convert_to_binary(list(map(lambda x: -x, coefficients)))
        ref = True

    last = len(b) - 1
    while b[last] != 1:
        last -= 1

    ans = 0
    for i in range(0, n + 1):
        if last - i > 40:
            continue
        cur = 0
        for j in range(i, last + 1):
            cur += b[j] * 2 ** (j - i)
        new_coef = coefficients[i] - cur
        if ref:
            new_coef = coefficients[i] + cur
        if abs(new_coef) > k:
            if b[i] == 1:
                break
            continue
        if i == n and new_coef == 0:
            if b[i] == 1:
                break
            continue
        ans += 1
        if b[i] == 1:
            break

    return ans