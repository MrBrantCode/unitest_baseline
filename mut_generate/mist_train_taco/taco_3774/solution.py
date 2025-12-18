"""
QUESTION:
Takahashi has A untasty cookies containing antidotes, B tasty cookies containing antidotes and C tasty cookies containing poison.

Eating a cookie containing poison results in a stomachache, and eating a cookie containing poison while having a stomachache results in a death. As he wants to live, he cannot eat one in such a situation. Eating a cookie containing antidotes while having a stomachache cures it, and there is no other way to cure stomachaches.

Find the maximum number of tasty cookies that Takahashi can eat.

Constraints

* 0 \leq A,B,C \leq 10^9
* A,B and C are integers.

Input

Input is given from Standard Input in the following format:


A B C


Output

Print the maximum number of tasty cookies that Takahashi can eat.

Examples

Input

3 1 4


Output

5


Input

5 2 9


Output

10


Input

8 8 1


Output

9
"""

def max_tasty_cookies(A: int, B: int, C: int) -> int:
    if B + A + 1 >= C:
        return B + C
    else:
        return B + A + B + 1