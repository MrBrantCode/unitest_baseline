"""
QUESTION:
Carving the cake 2 (Cake 2)

JOI-kun and IOI-chan are twin brothers and sisters. JOI has been enthusiastic about making sweets lately, and JOI tried to bake a cake and eat it today, but when it was baked, IOI who smelled it came, so we decided to divide the cake. became.

The cake is round. We made radial cuts from a point, cut the cake into N pieces, and numbered the pieces counterclockwise from 1 to N. That is, for 1 ≤ i ≤ N, the i-th piece is adjacent to the i − 1st and i + 1st pieces (though the 0th is considered to be the Nth and the N + 1st is considered to be the 1st). The size of the i-th piece was Ai, but I was so bad at cutting that all Ai had different values.

<image>
Figure 1: Cake example (N = 5, A1 = 2, A2 = 8, A3 = 1, A4 = 10, A5 = 9)


I decided to divide these N pieces by JOI-kun and IOI-chan. I decided to divide it as follows:

1. First, JOI chooses and takes one of N.
2. After that, starting with IOI-chan, IOI-chan and JOI-kun alternately take the remaining pieces one by one. However, if you can only take a piece that has already been taken at least one of the pieces on both sides, and there are multiple pieces that can be taken, IOI will choose the largest one and JOI will take it. You can choose what you like.



JOI wants to maximize the total size of the pieces he will finally take.

Task

Given the number N of cake pieces and the size information of N pieces, create a program to find the maximum value of the total size of pieces that JOI can take.

input

Read the following input from standard input.

* The integer N is written on the first line, which means that the cake is cut into N pieces.
* The integer Ai is written on the i-th line (1 ≤ i ≤ N) of the following N lines, which indicates that the size of the i-th piece is Ai.



output

Output an integer representing the maximum value of the total size of pieces that JOI can take to the standard output on one line.

Limits

All input data satisfy the following conditions.

* 1 ≤ N ≤ 20000.
* 1 ≤ Ai ≤ 1 000 000 000.
* Ai are all different.



Input / output example

Input example 1


Five
2
8
1
Ten
9


Output example 1


18


JOI is best to take the pieces as follows.

1. JOI takes the second piece. The size of this piece is 8.
2. IOI takes the first piece. The size of this piece is 2.
3. JOI takes the 5th piece. The size of this piece is 9.
4. IOI takes the 4th piece. The size of this piece is 10.
5. JOI takes the third piece. The size of this piece is 1.



Finally, the total size of the pieces taken by JOI is 8 + 9 + 1 = 18.

Input example 2


8
1
Ten
Four
Five
6
2
9
3


Output example 2


26


Input example 3


15
182243672
10074562
977552215
122668426
685444213
3784162
463324752
560071245
134465220
21447865
654556327
183481051
20041805
405079805
564327789


Output example 3


3600242976


The question text and the data used for the automatic referee are the question text and the test data for scoring, which are created and published by the Japan Committee for Information Olympics.





Example

Input

5
2
8
1
10
9


Output

18
"""

def maximize_joi_cake_pieces(N, A):
    memo = [[-1] * N for _ in range(N)]
    
    # Initialize memoization table for base cases
    for i in range(N):
        memo[i][i] = A[i] if N % 2 != 0 else 0
    
    def dfs(p, q, t):
        if memo[p][q] != -1:
            return memo[p][q]
        if t:
            memo[p][q] = max(A[p] + dfs((p + 1) % N, q, 0), A[q] + dfs(p, (q - 1) % N, 0))
        elif A[p] < A[q]:
            memo[p][q] = dfs(p, (q - 1) % N, 1)
        else:
            memo[p][q] = dfs((p + 1) % N, q, 1)
        return memo[p][q]
    
    ans = 0
    for i in range(N):
        ans = max(ans, A[i] + dfs((i + 1) % N, (i - 1) % N, 0))
    
    return ans