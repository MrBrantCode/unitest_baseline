"""
QUESTION:
Read problems statements in Mandarin chinese, Russian and Vietnamese as well. 

Chef and his little brother are playing with sticks. Initially, Chef has $N$ sticks with lengths $A_{1}, A_{2}, \dots, A_{N}$. He should give his little brother at least $K$ of these sticks. Afterwards, Chef's brother should choose four sticks and use them to form a rectangle (a square is also a rectangle). Chef does not want his brother to break any of the sticks, so each of the chosen sticks should be one side of the rectangle.

Chef's little brother wants the rectangle he makes to have the maximum possible area, while Chef wants it to have the minimum possible area. Therefore, Chef wants to choose the sticks to give his brother in such a way that they cannot be used to form a rectangle; if it's impossible, then he wants to choose the sticks in such a way that the maximum area of a rectangle his little brother can form is minimum possible.

Can you find the area of the resulting rectangle (or determine that it won't be possible to form any) if both Chef and his little brother play optimally?

------  Input ------
The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
The first line of each test case contains two space-separated integers $N$ and $K$.
The second line contains $N$ space-separated integers $A_{1}, A_{2}, \dots, A_{N}$.

------  Output ------
For each test case, print a single line containing one integer — the area of the resulting rectangle or $-1$ if Chef can give his brother sticks that cannot be used to form any rectangle.

------  Constraints ------
$1 ≤ T ≤ 100$
$1 ≤ N ≤ 10^{5}$
$0 ≤ K ≤ N$
the sum of $N$ over all test cases does not exceed $10^{5}$
$1 ≤ A_{i} ≤ 10^{9}$ for each valid $i$

----- Sample Input 1 ------ 
2
7 6
1 2 3 1 2 2 1
5 4
1 2 1 2 3
----- Sample Output 1 ------ 
2
-1
----- explanation 1 ------ 
Example case 1: Chef should give his brother all sticks except one. Regardless of the length of that one stick, Chef's brother can choose sticks with lengths $1, 2, 1, 2$ to create a rectangle with area $1 \cdot 2 = 2$.

Example case 2: If Chef gives his brother sticks with lengths $2, 1, 2, 3$, then there is no way to form a rectangle.
"""

def find_minimum_rectangle_area(A, k):
    n = len(A)
    A = sorted(A)
    B = [A[0]]
    AA = []
    
    # Separate sticks into unique lengths and repeated lengths
    for i in range(1, n):
        if A[i] == A[i - 1]:
            AA += [A[i]]
        else:
            B += [A[i]]
    
    # If Chef can give more than k sticks, return -1
    if len(B) >= k:
        return -1
    
    k -= len(B)
    
    # If k is 1 or 2, handle special cases
    if k == 1:
        return -1
    if k == 2:
        for i in range(1, len(AA)):
            if AA[i] == AA[i - 1]:
                return -1
        return AA[0] * AA[1]
    
    # Adjust AA to consider only the necessary sticks
    AA = AA[k - 3:]
    
    # Calculate the minimum possible area
    if AA[1] == AA[2]:
        return AA[0] * AA[2]
    if AA[0] == AA[1]:
        return AA[1] * AA[2]
    
    ret = AA[1] * AA[2]
    for i in range(3, len(AA)):
        if AA[i] == AA[i - 1]:
            return min(ret, AA[0] * AA[i])
    
    return ret