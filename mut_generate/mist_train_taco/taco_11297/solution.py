"""
QUESTION:
Read problems statements in mandarin chinese, russian and vietnamese as well. 

You are given N integers. In each step you can choose some K of the remaining numbers and delete them, if the following condition holds: Let the K numbers you've chosen be a_{1}, a_{2}, a_{3}, ..., a_{K} in sorted order. Then, for each i ≤ K - 1, a_{i+1} must be greater than or equal to a_{i} * C.

You are asked to calculate the maximum number of steps you can possibly make.

------ Input ------ 

The first line of the input contains an integer T, denoting the number of test cases. The description of each testcase follows.
The first line of each testcase contains three integers: N, K, and C
The second line of each testcase contains the N initial numbers

------ Output ------ 

For each test case output the answer in a new line.

------ Subtasks ------ 

Subtask #1 (40 points):

1 ≤ N ≤ 10^{3} 
1 ≤ Sum of N over all test cases ≤  10^{3} 

Subtask #2 (60 points):

Original constraints

------ Constraints ------ 

$1 ≤ T ≤ 100$
$1 ≤ N ≤ 3 * 10^{5}$
$1 ≤ K ≤ 64$
$2 ≤ C ≤ 50$
$1 ≤ a_{i} ≤ 10^{18}$
$1 ≤ Sum of N over all test cases ≤  3 * 10^{5} $

----- Sample Input 1 ------ 
2

6 3 2

4 1 2 2 3 1

6 3 2

1 2 2 1 4 4
----- Sample Output 1 ------ 
1

2
----- explanation 1 ------ 
Testcase 1: You can make one step by choosing {1, 2, 4}.
Testcase 2: You can make one step by choosing {1, 2, 4} and another by choosing {1, 2, 4}.
"""

def calculate_max_steps(n, k, c, arr):
    def check(x):
        vec = [[] for _ in range(x)]
        l = 0
        for num in arr:
            if len(vec[l]) == k:
                return True
            elif not vec[l] or vec[l][-1] * c <= num:
                vec[l].append(num)
                l = (l + 1) % x
        for i in range(x):
            if len(vec[i]) != k:
                return False
        return True
    
    arr.sort()
    l, h = 0, n // k + 1
    ans = 0
    while h - l > 1:
        mid = (l + h) // 2
        if check(mid):
            l = mid
            ans = max(ans, mid)
        else:
            h = mid
    return ans