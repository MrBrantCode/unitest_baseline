"""
QUESTION:
Shreyan is appearing for CAT examination and is stuck at a problem to find minimum value needed to be added or subtracted to make a number perfect square.You as his friend and a good programmer agrees to help him find the answer. 

INPUT:

First line will contain no of test cases T (1 < T < 10000)

Next T lines will have integer N (1 < N < 1000000000000)

OUTPUT:

Print YES if the N is a perfect square.

If not then print the minimum value that must be added or subtracted to N to make it perfect square with sign

SAMPLE INPUT
3
25
168
19

SAMPLE OUTPUT
YES
+1
-3

Explanation

25 is prefect square so output is YES

168 is not perfect square but if 1 is added then 169 is perfect square.

19 is not perfect square but if 3 is subtracted it becomes 16 which is a perfect square and if 6 is added it becomes 25 which is perfect square but we choose 3 as its is the minimum value
"""

import math

def find_min_adjustment_for_perfect_square(N):
    t = math.sqrt(N)
    if math.floor(t) == t:
        return 'YES'
    else:
        lower_square = math.floor(t) ** 2
        upper_square = math.ceil(t) ** 2
        if N - lower_square <= upper_square - N:
            return f'-{N - lower_square}'
        else:
            return f'+{upper_square - N}'