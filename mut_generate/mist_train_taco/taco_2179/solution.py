"""
QUESTION:
Takahashi is distributing N balls to K persons.

If each person has to receive at least one ball, what is the maximum possible difference in the number of balls received between the person with the most balls and the person with the fewest balls?

Constraints

* 1 \leq K \leq N \leq 100
* All values in input are integers.

Input

Input is given from Standard Input in the following format:


N K


Output

Print the maximum possible difference in the number of balls received.

Examples

Input

3 2


Output

1


Input

3 1


Output

0


Input

8 5


Output

3
"""

def max_ball_difference(N: int, K: int) -> int:
    if K == 1:
        return 0
    else:
        return N - K