"""
QUESTION:
Read problems statements in Mandarin Chinese, Russian and Vietnamese as well.

Given an array of size n, you have to answer queries of the form :  L R k . For each query, you have to find an element which occurs consecutively in the subarray [L,R] more than or equal to k times. k will always be greater than floor((R-L+1)/2). If no such element exists, print -1.

------ Input ------ 

First line of the input contains 2 space separated N and M, denoting the size of the array and the number of queries. 
The next line contains N space separated integers, where the i-th integer A_{i} denotes the ith element of the array.
Each of the next M lines contains 3 integers space separated integers L, R and k.

------ Output ------ 

Output M lines where each line contains the answer to the i-th query.

------ Constraints ------ 

$1 ≤ N, M ≤ 10^{5}$
$1 ≤ L ≤ R ≤ N$
$floor((R-L+1)/2) < k ≤ R-L+1$    
$0 ≤ A_{i} ≤ 10^{9}$

------ Subtasks ------ 

Subtask #1 (10 points):
$1 ≤ A_{i} ≤ 3$ 
$1 ≤ M ≤ 10$    

Subtask #2 (30 points):
$1 ≤ N ≤ 1000$

Subtask #3 (60 points):
$No other constraints$

----- Sample Input 1 ------ 
5 1
1 2 2 2 2
1 5 3
----- Sample Output 1 ------ 
2
----- explanation 1 ------ 
The element 2 occurs more than 3 times in the range [1,5].
"""

def find_consecutive_element(array, queries):
    n = len(array)
    lb = [None] * n
    rb = [None] * n
    
    i = 0
    j = 0
    while i < n:
        while j < n - 1 and array[j + 1] == array[j]:
            j += 1
        for k in range(i, j + 1):
            lb[k] = i
            rb[k] = j
        i = j + 1
        j = i
    
    results = []
    for (l, r, k) in queries:
        l = l - 1
        r = r - 1
        c = (l + r) // 2
        ll = max(lb[c], l)
        rr = min(rb[c], r)
        results.append(array[c] if rr - ll + 1 >= k else -1)
    
    return results