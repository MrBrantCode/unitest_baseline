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

def count_distinct_pairs(arr):
    count = 0
    l = len(arr)
    i = 0
    while i < l:
        j = i
        while j < l:
            if arr[i] == arr[j]:
                count += 1
            j += 1
        i += 1
    return count