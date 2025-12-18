"""
QUESTION:
You are given a positive integer $n$, written without leading zeroes (for example, the number 04 is incorrect). 

In one operation you can delete any digit of the given integer so that the result remains a positive integer without leading zeros.

Determine the minimum number of operations that you need to consistently apply to the given integer $n$ to make from it the square of some positive integer or report that it is impossible.

An integer $x$ is the square of some positive integer if and only if $x=y^2$ for some positive integer $y$.


-----Input-----

The first line contains a single integer $n$ ($1 \le n \le 2 \cdot 10^{9}$). The number is given without leading zeroes.


-----Output-----

If it is impossible to make the square of some positive integer from $n$, print -1. In the other case, print the minimal number of operations required to do it.


-----Examples-----
Input
8314

Output
2

Input
625

Output
0

Input
333

Output
-1



-----Note-----

In the first example we should delete from $8314$ the digits $3$ and $4$. After that $8314$ become equals to $81$, which is the square of the integer $9$.

In the second example the given $625$ is the square of the integer $25$, so you should not delete anything. 

In the third example it is impossible to make the square from $333$, so the answer is -1.
"""

import itertools

def min_operations_to_square(n: int) -> int:
    s = str(n)
    e = len(s)
    
    # Pad the string with leading zeros to handle edge cases
    while len(s) < 10:
        s = '0' + s
    
    m = 0
    
    # Generate all possible combinations of digits to keep
    for i in itertools.product(range(2), repeat=10):
        loc = ''
        for j in range(10):
            if i[j]:
                loc += s[j]
        
        # Skip if the resulting number is empty or has leading zeros
        if not loc or loc[0] == '0':
            continue
        
        # Check if the resulting number is a perfect square
        k = int(loc) ** 0.5
        if int(k) != k:
            continue
        
        # Update the maximum length of the valid square number found
        if len(loc) > m:
            m = len(loc)
    
    # Calculate the minimum number of operations required
    return e - m if m != 0 else -1