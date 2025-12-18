"""
QUESTION:
Given an array A of N numbers, find the number of distinct pairs (i, j) such that j ≥i and A[i] = A[j].

First line of the input contains number of test cases T. Each test case has two lines, first line is the number N, followed by a line consisting of N integers which are the elements of array A.

For each test case print the number of distinct pairs.

Constraints

1 ≤ T ≤ 10

1 ≤ N ≤ 10^6 

-10^6 ≤ A[i] ≤ 10^6 for 0 ≤ i < N

SAMPLE INPUT
2
4
1 2 3 4
3
1 2 1

SAMPLE OUTPUT
4
4
"""

def count_distinct_pairs(A, N):
    c = 0
    for i in range(N):
        for j in range(i, N):
            if A[i] == A[j]:
                c += 1
    return c