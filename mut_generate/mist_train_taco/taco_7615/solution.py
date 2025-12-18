"""
QUESTION:
Chef and his friend Miron were getting bored and decided to play a game. 
Miron thinks of a sequence of  N  integers (A1, A2, …., AN) and gives Chef a matrix B, where Bi,j = |Ai - Aj|. He further tells Chef that A1 = 0. The game is for Chef to guess the sequence that Miron thought of. 
But Miron is an adversarial player. Every time Chef tries to guess the sequence, he makes a change to the matrix. He makes such a change Q times. Each time, he replaces an entry in some row and the corresponding column with a new one leaving Chef to guess the sequence after each change. 
Chef needs a friend to help him against such an adversarial player. Can you be that friend and help Chef find a suitable sequence A for the initial matrix B and also after each change Miron makes? 
Note that if several answers exist, then print the lexicographically smallest answer. Further, the numbers in the sequence can be negative.

-----Input-----

The first line contains two space-separated integers N, Q. Each of the N subsequent lines contains N space-separated integers, denoting the matrix B.

Q queries follow. Each query has two lines. The first line of each query contains an integer p, denoting the number of row and column that is changed. The second line of each query contains N space-separated integers F1, F2, F3, ... FN, denoting the new values to the corresponding cells of the matrix (you should make the following assignments Bi,p = Bp,i = Fi for all valid i). 

-----Output-----
Print Q + 1 lines which contain N space-separated integers, Miron's initial array and Miron's array after each query.

-----Constraints-----
- 3 ≤ N ≤  1000 
- 1 ≤ Q ≤  1000 
- 0 ≤ Bi,j ≤  5000 
- 1 ≤ p ≤  n 
- 0 ≤ Fi ≤  5000 
- it's guaranteed there's always an answer

-----Example-----
Input:
3 2
0 1 2
1 0 1
2 1 0
1
0 4 3
2
4 0 7
Output:
0 -1 -2
0 -4 -3
0 -4 3

-----Explanation-----
Example case 1. Initially, sequence {0, 1, 2} is also suitable, but {0, -1, -2} is lexicografically smaller.
"""

def find_sequence_after_changes(N, Q, initial_B, queries):
    def update_B(B, query):
        (p, R) = query
        for i in range(len(R)):
            B[p][i] = R[i]
            B[i][p] = R[i]

    def get_A(B):
        N = len(B)
        A = [0] * N
        i = 0
        for j in range(N):
            if B[0][j] != 0:
                i = j
                A[i] = -B[0][i]
                break
        for j in range(i + 1, N):
            if abs(A[i] - B[0][j]) == B[i][j]:
                A[j] = B[0][j]
            else:
                A[j] = -B[0][j]
        return A

    results = []
    B = [row[:] for row in initial_B]  # Create a copy of the initial matrix
    results.append(get_A(B))  # Initial sequence

    for q in queries:
        update_B(B, q)
        results.append(get_A(B))  # Sequence after each query

    return results