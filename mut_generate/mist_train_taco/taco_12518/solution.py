"""
QUESTION:
Takahashi and Aoki are training for long-distance races in an infinitely long straight course running from west to east.

They start simultaneously at the same point and moves as follows towards the east:

* Takahashi runs A_1 meters per minute for the first T_1 minutes, then runs at A_2 meters per minute for the subsequent T_2 minutes, and alternates between these two modes forever.
* Aoki runs B_1 meters per minute for the first T_1 minutes, then runs at B_2 meters per minute for the subsequent T_2 minutes, and alternates between these two modes forever.



How many times will Takahashi and Aoki meet each other, that is, come to the same point? We do not count the start of the run. If they meet infinitely many times, report that fact.

Constraints

* 1 \leq T_i \leq 100000
* 1 \leq A_i \leq 10^{10}
* 1 \leq B_i \leq 10^{10}
* A_1 \neq B_1
* A_2 \neq B_2
* All values in input are integers.

Input

Input is given from Standard Input in the following format:


T_1 T_2
A_1 A_2
B_1 B_2


Output

Print the number of times Takahashi and Aoki will meet each other.
If they meet infinitely many times, print `infinity` instead.

Examples

Input

1 2
10 10
12 4


Output

1


Input

100 1
101 101
102 1


Output

infinity


Input

12000 15700
3390000000 3810000000
5550000000 2130000000


Output

113
"""

def calculate_meeting_times(T1, T2, A1, A2, B1, B2):
    x = T1 * (A1 - B1)
    y = x + T2 * (A2 - B2)
    
    if x * y > 0:
        return 0
    elif x * y == 0:
        return 'infinity'
    elif abs(x) % abs(y) == 0:
        return 2 * (abs(x) // abs(y))
    else:
        return 2 * (abs(x) // abs(y)) + 1