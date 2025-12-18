"""
QUESTION:
Find the length of the longest contiguous segment in an array, in which if a given element $K$ is inserted, $K$ becomes the second largest element of that subarray.

-----Input:-----
- The first line will contain $T$, number of test cases. Then the test cases follow. 
- The first line of each test case contains two integers $N$ and $K$.
- The next line contains N space-separated integers Ai denoting the elements of the array.

-----Output:-----
Print a single line corresponding to each test case — the length of the largest segment.

-----Constraints-----
- $1 \leq T \leq 10$
- $1 \leq N \leq 10^6$
- $1 \leq Ai, K \leq 10^9$
- Sum of N across all test cases doesn't exceed $10^6$

-----Sample Input:-----
2
5 3
2 4 2 4 2
8 5
9 3 5 7 8 11 17 2

-----Sample Output:-----
5
3

-----EXPLANATION:-----
If 3 is inserted at anywhere in the array, it is the second largest element. Hence the maximum length is 5.
If 5 is inserted anywhere between 1st and 4th element, it is the second largest element. The length of such subarray is 3.
"""

def find_longest_segment_length(arr, k):
    tarr = []
    p = -1
    
    for i in range(len(arr)):
        if arr[i] > k:
            if p == -1:
                p = arr[i]
                tarr.append(i)
            elif arr[i] != p:
                tarr.append(i)
                p = arr[i]
    
    if len(tarr) == 0:
        return 0
    elif len(tarr) == 1:
        return len(arr)
    else:
        mtn = max(tarr[1], len(arr) - tarr[-2] - 1)
        for i in range(1, len(tarr) - 1):
            mtn = max(mtn, tarr[i] - tarr[i - 1] + tarr[i + 1] - tarr[i] - 1)
        return mtn