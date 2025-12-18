"""
QUESTION:
Read problem statements in [Russian] and [Mandarin Chinese].

Find the minimum integer K such that sum of bits present on odd positions in binary representation of all integers from 1 to K is greater than or equal to N.

The bits are enumerated from left to right starting from the leftmost set bit i.e. the most significant bit. For example, binary representation of 77 is 1001101. Bits present on 1^{st}, 3^{rd}, 5^{th} and 7^{th} positions in the binary representation are 1, 0, 1, 1 respectively. So sum of bits present on odd positions in binary representation of 77 is 1 + 0 + 1 + 1 = 3.

------ Input Format ------ 

- First line will contain T, number of testcases. Then the testcases follow.
- Each testcase contains of a single line of input, an integer N.

------ Output Format ------ 

For each testcase, output in a single line the minimum possible value of K.

------ Constraints ------ 

$1 ≤ T ≤ 10^{3}$
$1 ≤ N ≤ 10^{9}$

----- Sample Input 1 ------ 
3
2
6
100
----- Sample Output 1 ------ 
2
5
57
----- explanation 1 ------ 
-  In the first test case, binary representations of $1$ and $2$ are 1, 10. Sum of bits present on odd positions in the binary representation of $1$ and $2$ =  $1 + 1$ = $2$.
-  In the second test case, the binary representations of integers from $1$ to $5$ are 1, 10, 
11, 100, 101 respectively. So the sum of bits present on odd positions in binary 
representation of integers from $1$ to $5$ are $1, 1, 1, 1, 2$ respectively which makes a total of $6$.
"""

def find_min_k_for_odd_bit_sum(N):
    def getk(x, bits):
        ans = 0
        for j in range(1, bits, 2):
            i = bits - j - 1
            y = x // 2 ** i
            ans += y // 2 * 2 ** i
            if y % 2:
                ans += x % 2 ** i
        return ans

    def calc(x):
        ans = x
        for b in range(60):
            size = b + 1
            if x >= 2 ** size - 1:
                cnt = 2 ** b
                ans += cnt // 2 * (b // 2)
            else:
                left = x - 2 ** b + 1
                if left <= 0:
                    break
                bits = b
                ans += getk(left, bits)
                break
        return ans

    (alpha, omega) = (1, 10 ** 9)
    while alpha < omega:
        x = (alpha + omega) // 2
        if calc(x) >= N:
            omega = x
        else:
            alpha = x + 1
    return alpha