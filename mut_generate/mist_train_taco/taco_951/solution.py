"""
QUESTION:
Input Format


N K
a_1 a_2 a_3 ... a_N


Output Format

Print the minimum cost in one line. In the end put a line break.


Constraints

* 1 ≤ K ≤ N ≤ 15
* 1 ≤ a_i ≤ 10^9



Scoring

Subtask 1 [120 points]


* N = K

Subtask 2 [90 points]


* N ≤ 5
* a_i ≤ 7

Subtask 3 [140 points]


* There are no additional constraints.

Output Format

Print the minimum cost in one line. In the end put a line break.


Constraints

* 1 ≤ K ≤ N ≤ 15
* 1 ≤ a_i ≤ 10^9



Scoring

Subtask 1 [120 points]


* N = K

Subtask 2 [90 points]


* N ≤ 5
* a_i ≤ 7

Subtask 3 [140 points]


* There are no additional constraints.

Input Format


N K
a_1 a_2 a_3 ... a_N

Example

Input

5 5
3949 3774 3598 3469 3424


Output

1541
"""

def calculate_minimum_cost(N, K, A):
    ans = float('inf')
    for i in range(1, 2 ** N):
        num = format(i, 'b').zfill(N)
        if num.count('1') != K:
            continue
        point = 0
        highest = A[0]
        for j in range(1, N):
            if highest >= A[j] and num[j] == '1':
                point += highest - A[j] + 1
                highest += 1
            highest = max(highest, A[j])
        ans = min(ans, point)
    return ans