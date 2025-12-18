"""
QUESTION:
Solve the Mystery.  

Input :
First line contains T - No. of Test cases.
Each Test case consists of 2 lines.
First line contains K.
Second line contains 3 space separated Integers A1 ,A2 ,A3.

Output : 
Print required answers in separate lines.

Constraints :
1 ≤ T ≤ 100
1 ≤ K ≤ 10
0 ≤ Ai ≤10  

SAMPLE INPUT
2
2
5 4 3
3
1 2 2

SAMPLE OUTPUT
144
125
"""

def solve_mystery(T, test_cases):
    results = []
    for i in range(T):
        K, A = test_cases[i]
        A1, A2, A3 = A
        result = (A1 + A2 + A3) ** K
        results.append(result)
    return results