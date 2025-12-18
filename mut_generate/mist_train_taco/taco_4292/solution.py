"""
QUESTION:
Given are integers a,b,c and d.
If x and y are integers and a \leq x \leq b and c\leq y \leq d hold, what is the maximum possible value of x \times y?

-----Constraints-----
 - -10^9 \leq a \leq b \leq 10^9
 - -10^9 \leq c \leq d \leq 10^9
 - All values in input are integers.

-----Input-----
Input is given from Standard Input in the following format:
a b c d

-----Output-----
Print the answer.

-----Sample Input-----
1 2 1 1

-----Sample Output-----
2

If x = 1 and y = 1 then x \times y = 1.
If x = 2 and y = 1 then x \times y = 2.
Therefore, the answer is 2.
"""

def find_max_product(a: int, b: int, c: int, d: int) -> int:
    if a > 0 and d < 0 or (b < 0 and c > 0):
        return min(abs(a), abs(b)) * min(abs(c), abs(d)) * -1
    else:
        return max(a * c, a * d, b * c, b * d)