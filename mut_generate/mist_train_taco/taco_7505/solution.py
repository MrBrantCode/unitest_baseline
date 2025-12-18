"""
QUESTION:
We held two competitions: Coding Contest and Robot Maneuver.

In each competition, the contestants taking the 3-rd, 2-nd, and 1-st places receive 100000, 200000, and 300000 yen (the currency of Japan), respectively. Furthermore, a contestant taking the first place in both competitions receives an additional 400000 yen.

DISCO-Kun took the X-th place in Coding Contest and the Y-th place in Robot Maneuver. Find the total amount of money he earned.

Constraints

* 1 \leq X \leq 205
* 1 \leq Y \leq 205
* X and Y are integers.

Input

Input is given from Standard Input in the following format:


X Y


Output

Print the amount of money DISCO-Kun earned, as an integer.

Examples

Input

1 1


Output

1000000


Input

3 101


Output

100000


Input

4 4


Output

0
"""

def calculate_total_earnings(X: int, Y: int) -> int:
    ans = 0
    
    # Calculate earnings from Coding Contest
    if X <= 3:
        ans += (4 - X) * 100000
    
    # Calculate earnings from Robot Maneuver
    if Y <= 3:
        ans += (4 - Y) * 100000
    
    # Additional bonus for first place in both contests
    if X == 1 and Y == 1:
        ans += 400000
    
    return ans