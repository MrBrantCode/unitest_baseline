"""
QUESTION:
There are n walruses standing in a queue in an airport. They are numbered starting from the queue's tail: the 1-st walrus stands at the end of the queue and the n-th walrus stands at the beginning of the queue. The i-th walrus has the age equal to ai.

The i-th walrus becomes displeased if there's a younger walrus standing in front of him, that is, if exists such j (i < j), that ai > aj. The displeasure of the i-th walrus is equal to the number of walruses between him and the furthest walrus ahead of him, which is younger than the i-th one. That is, the further that young walrus stands from him, the stronger the displeasure is.

The airport manager asked you to count for each of n walruses in the queue his displeasure.

Input

The first line contains an integer n (2 ≤ n ≤ 105) — the number of walruses in the queue. The second line contains integers ai (1 ≤ ai ≤ 109).

Note that some walruses can have the same age but for the displeasure to emerge the walrus that is closer to the head of the queue needs to be strictly younger than the other one.

Output

Print n numbers: if the i-th walrus is pleased with everything, print "-1" (without the quotes). Otherwise, print the i-th walrus's displeasure: the number of other walruses that stand between him and the furthest from him younger walrus.

Examples

Input

6
10 8 5 3 50 45


Output

2 1 0 -1 0 -1 

Input

7
10 4 6 3 2 8 15


Output

4 2 1 0 -1 -1 -1 

Input

5
10 3 1 10 11


Output

1 0 -1 -1 -1
"""

from bisect import bisect_left

def calculate_walrus_displeasure(n, ages):
    suf = [[10 ** 10, -1] for _ in range(n)]
    suf[-1][0] = ages[-1]
    suf[-1][1] = n - 1
    
    for i in range(n - 2, -1, -1):
        if suf[i + 1][0] > ages[i]:
            suf[i][0] = ages[i]
            suf[i][1] = i
        else:
            suf[i][0] = suf[i + 1][0]
            suf[i][1] = suf[i + 1][1]
    
    vals = [i[0] for i in suf]
    displeasure = []
    
    for i in range(n):
        idx = bisect_left(vals, ages[i])
        displeasure.append(max(-1, idx - i - 2))
    
    return displeasure