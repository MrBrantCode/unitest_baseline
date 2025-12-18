"""
QUESTION:
Takahashi has an empty string S and a variable x whose initial value is 0.

Also, we have a string T consisting of `0` and `1`.

Now, Takahashi will do the operation with the following two steps |T| times.

* Insert a `0` or a `1` at any position of S of his choice.
* Then, increment x by the sum of the digits in the odd positions (first, third, fifth, ...) of S. For example, if S is `01101`, the digits in the odd positions are `0`, `1`, `1` from left to right, so x is incremented by 2.



Print the maximum possible final value of x in a sequence of operations such that S equals T in the end.

Constraints

* 1 \leq |T| \leq 2 \times 10^5
* T consists of `0` and `1`.

Input

Input is given from Standard Input in the following format:


T


Output

Print the maximum possible final value of x in a sequence of operations such that S equals T in the end.

Examples

Input

1101


Output

5


Input

0111101101


Output

26
"""

def calculate_max_final_value(T: str) -> int:
    def f(n, r, l, z):
        if n % 2 == 0:
            move = r - l + z
            return (move + 1) * (n // 2)
        if r == l and r % 2 == 0:
            k = (n - 1) // 2
            move = r - l + z
            return (move + 1) * k
        ev = r // 2 - (l - 1) // 2
        od = r - l + 1 - ev
        od += z
        k = (n - 1) // 2
        return ev * k + od * (k + 1)

    Z = T.count('0')
    one = 0
    to = 0
    answer = 0

    for i, x in enumerate(T, 1):
        if x == '0':
            if one:
                answer += f(one, i - 1, to, Z)
                one = 0
            Z -= 1
            continue
        to += 1
        one += 1

    if one:
        answer += f(one, i, to, Z)

    def f(n):
        ret = 0
        for i in range(0, n, 2):
            ret += n - i
        ret -= (n + 1) // 2
        return ret

    n = T.count('1')
    answer += f(n)
    return answer