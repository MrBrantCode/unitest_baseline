"""
QUESTION:
Coolguy gives you a simple problem. Given a $1$-indexed array, $\mbox{A}$, containing $N$ elements, what will $\textit{and}$ be after this pseudocode is implemented and executed? Print $and\%(10^9+7)$.

//f(a, b) is a function that returns the minimum element in interval [a, b]

ans = 0

for a -> [1, n]
    for b -> [a, n]
        for c -> [b + 1, n]
            for d -> [c, n]
                ans = ans + min(f(a, b), f(c, d))

Input Format

The first line contains $N$ (the size of array $\mbox{A}$). 

The second line contains $N$ space-separated integers describing $\mbox{A}$.

Constraints

$1$ ≤ $N$ ≤ $2\times10^5$
$1$ ≤ $A_i$ ≤ $\mathbf{10^{9}}$

Note: $\mbox{A}$ is $1$-indexed (i.e.: $A=\{A_1,A_2,\text{...},A_{N-1},A_N\}$).

Output Format

Print the integer result of $and\%(10^9+7)$.

Sample Input
3
3 2 1

Sample Output
6

Explanation

$min(~f(1,1),~f(2,2)~)=2$

$min(~f(1,1),~f(2,3)~)=1$

$min(~f(1,1),~f(3,3)~)=1$

$min(~f(1,2),~f(3,3)~)=1$

$min(~f(2,2),~f(3,3)~)=1$ 

We then sum these numbers ($2+1+1+1+1=6$) and print $6\%(10^9+7)$, which is $\boldsymbol{6}$.
"""

def calculate_and_modulo(n, A):
    # Initialize auxiliary arrays and variables
    left = [0] * (n + 2)
    right = [0] * (n + 2)
    singles = pairs = 0
    ans = 0

    # Helper functions to manage singles and pairs
    def remove(k):
        nonlocal singles, pairs
        s = k * (k + 1) // 2
        singles -= s
        pairs -= (k + 2) * (k + 1) * k * (k - 1) // 24 + s * singles

    def add(k):
        nonlocal singles, pairs
        s = k * (k + 1) // 2
        pairs += (k + 2) * (k + 1) * k * (k - 1) // 24 + s * singles
        singles += s

    # Process the array elements in sorted order
    for i in sorted(range(1, n + 1), key=A.__getitem__)[::-1]:
        (l, r) = (left[i - 1], right[i + 1])
        k = l + 1 + r
        right[i - l] = left[i + r] = k
        oldpairs = pairs
        remove(l)
        remove(r)
        add(k)
        ans += A[i] * (pairs - oldpairs)

    # Return the result modulo (10^9 + 7)
    return ans % (10 ** 9 + 7)