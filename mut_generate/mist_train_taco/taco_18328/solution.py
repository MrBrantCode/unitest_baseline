"""
QUESTION:
AtCoder Inc. has decided to lock the door of its office with a 3-digit PIN code.

The company has an N-digit lucky number, S. Takahashi, the president, will erase N-3 digits from S and concatenate the remaining 3 digits without changing the order to set the PIN code.

How many different PIN codes can he set this way?

Both the lucky number and the PIN code may begin with a 0.

Constraints

* 4 \leq N \leq 30000
* S is a string of length N consisting of digits.

Input

Input is given from Standard Input in the following format:


N
S


Output

Print the number of different PIN codes Takahashi can set.

Examples

Input

4
0224


Output

3


Input

6
123123


Output

17


Input

19
3141592653589793238


Output

329
"""

def count_possible_pins(N: int, S: str) -> int:
    ans = 0
    for i in range(1000):
        cnt = 0
        n = str(i).zfill(3)
        for c in S:
            if c == n[cnt]:
                cnt += 1
            if cnt == 3:
                ans += 1
                break
    return ans