"""
QUESTION:
Chef found an array A of N elements. He defines a subarray as *bad* if the maximum element of the subarray is equal to the minimum element of the subarray.

More formally, a subarray [L,R] (1 ≤ L ≤ R ≤ N) is *bad* if \texttt{max}(A_{L}, A_{L+1}, \ldots , A_{R}) = \texttt{min} (A_{L}, A_{L+1}, ... , A_{R}).

Chef is allowed to change at most K elements of the array.  
Find the minimum number of *bad* subarrays Chef can obtain after changing at most K elements of the array.    

------ Input Format ------ 

- First line will contain T, the number of test cases. Then the test cases follow.
- Each test case contains two lines of input, the first line contains two space-separated integers N and K - the number of elements in the array and the maximum number of elements Chef can change respectively.
- The second line contains N space-separated integers A_{1}, A_{2},\ldots, A_{N} - the initial array.

------ Output Format ------ 

For each test case, output the minimum number of *bad* subarrays Chef can obtain after changing at most K elements of the array.

------ Constraints ------ 

$1 ≤ T ≤ 3\cdot 10^{4}$
$1 ≤ N ≤ 10^{5}$
$1 ≤ K ≤ N$
$1 ≤ A_{i} ≤ 10^{9}$
- Sum of $N$ over all test cases does not exceed $3\cdot 10^{5}$.

----- Sample Input 1 ------ 
3
3 1
1 2 3
4 2
3 3 3 1
5 1
1 1 1 1 1

----- Sample Output 1 ------ 
3
4
7

----- explanation 1 ------ 
Test case $1$: The minimum number of *bad* subarrays Chef can obtain is $3$. Chef does not need to perform any operations. The subarrays where the maximum element is equal to the minimum element are $[1,1], [2,2],$ and $[3,3]$ where $[L,R]$ denotes the subarray starting at index $L$ and ending at index $R$.

Test case $2$: The minimum number of *bad* subarrays Chef can obtain is $4$. Chef can perform $2$ operations and change the array to $[2, 4, 3, 1]$. The subarrays where the maximum element is equal to the minimum element are $[1,1], [2,2], [3,3],$ and $[4,4]$.
"""

import heapq

def comp(x, y):
    s = (x - y) % (y + 1)
    t = (x - y) // (y + 1)
    return s * (t + 1) + (y + 1) * t * (t + 1) // 2 + y

def hfindb(a, k):
    aa = [[comp(val, 1) - comp(val, 0), val, 0, idx, comp(val, 0), comp(val, 1)] for (idx, val) in enumerate(a)]
    heapq.heapify(aa)
    for i in range(k):
        x = heapq.heappop(aa)
        x[2] += 1
        x[4] = x[5]
        x[5] = comp(x[1], x[2] + 1)
        x[0] = x[5] - x[4]
        heapq.heappush(aa, x)
    return sum([x[4] for x in aa])

def min_bad_subarrays(N, K, A):
    temp = A[0]
    tempc = 0
    count = []
    for val in A:
        if val == temp:
            tempc += 1
        else:
            count.append(tempc)
            tempc = 1
            temp = val
    count.append(tempc)
    count.sort(reverse=True)
    output = len(count)
    eff = sum([t // 2 for t in count])
    count = [val for val in count if val > 1]
    output -= len(count)
    if K >= eff:
        return N
    else:
        return hfindb(count, K) + output