"""
QUESTION:
In the previous problem Chandu bought some unsorted arrays and sorted them (in non-increasing order). Now, he has many sorted arrays to give to his girlfriend. But, the number of sorted arrays are very large so Chandu decided to merge two sorted arrays into one sorted array. But he is too lazy to do that. So, he asked your help to merge the two sorted arrays into one sorted array (in non-increasing order).

Input:
First line contains an integer T, denoting the number of test cases.
First line of each test case contains two space separated integers N and M, denoting the size of the two sorted arrays.
Second line of each test case contains N space separated integers, denoting the first sorted array A.
Third line of each test case contains M space separated integers, denoting the second array B.

Output:
For each test case, print (N + M) space separated integer representing the merged array.

Constraints:
1 ≤ T ≤ 100
1 ≤ N, M ≤ 5*10^4
0 ≤ Ai, Bi ≤ 10^9

SAMPLE INPUT
1
4 5
9 7 5 3
8 6 4 2 0

SAMPLE OUTPUT
9 8 7 6 5 4 3 2 0
"""

def merge_sorted_arrays(arr1, arr2):
    """
    Merges two sorted arrays (in non-increasing order) into one sorted array (in non-increasing order).

    Parameters:
    arr1 (list of int): The first sorted array in non-increasing order.
    arr2 (list of int): The second sorted array in non-increasing order.

    Returns:
    list of int: The merged sorted array in non-increasing order.
    """
    merged_array = []
    p1, p2 = 0, 0
    N, M = len(arr1), len(arr2)
    
    while p1 < N and p2 < M:
        if arr1[p1] >= arr2[p2]:
            merged_array.append(arr1[p1])
            p1 += 1
        else:
            merged_array.append(arr2[p2])
            p2 += 1
    
    while p1 < N:
        merged_array.append(arr1[p1])
        p1 += 1
    
    while p2 < M:
        merged_array.append(arr2[p2])
        p2 += 1
    
    return merged_array