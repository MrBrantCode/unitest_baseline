"""
QUESTION:
Read problems statements in Mandarin Chinese, Russian and Vietnamese as well. 

During the Indian Programming Camp (IPC), there are N trainers. The camp runs for D days. Each day, there can be at most one lecture. The i-th trainer arrives on day D_{i} and then stays till the end of the camp. He also wants to teach exactly Ti lectures. For each lecture that a trainer was not able to teach, he will feel sad and his sadness level will be increased by S_{i}.

You are the main organizer of the contest. You want to find minimum total sadness of the trainers.

------ Input ------ 

The first line of the input contains an integer T, denoting the number of testcases.
For each test case, the first line contains two space separated integers, N, D.
The i-th of the next N lines will contain three space separated integers: D_{i}, T_{i}, S_{i} respectively.

------ Output ------ 

For each test case, output a single integer corresponding to the minimum total sadness of the trainers achievable.

------ Constraints ------ 

$1 ≤ T ≤ 10$
$1 ≤ N, D ≤ 10^{5}$
$1 ≤  D_{i},  T_{i} ≤ D$
$1 ≤  S_{i} ≤ 10^{5}$

------ Subtasks ------ 

Subtask #1 (40 points)

$1 ≤ T ≤ 10$
$1 ≤ N, D ≤ 10^{3}$
$1 ≤  D_{i},  T_{i} ≤ D$
$1 ≤  S_{i} ≤ 10^{3}$

Subtask #2 (60 points)

$Original constraints$

----- Sample Input 1 ------ 
3

2 3

1 2 300

2 2 100

2 3

1 1 100

2 2 300

2 3

3 2 150

1 1 200
----- Sample Output 1 ------ 
100

0

150
----- explanation 1 ------ 
Example case 1. Both the first and second trainer want to take exactly two lectures. The first trainer arrives on the 1st day and the second trainer arrives on the 2nd day. Consider a schedule where the first trainer takes the first two lectures, and the second trainer takes the last lecture on the day 3. This way the second trainer will take only one lecture but wanted to take two. Thus, his sadness will be 100. The first trainer took all the lectures that he wanted to take (ie. two lectures). Thus the total sadness is 100 + 0 = 100. You can check that no other way of assigning trainers to the days will give a better answer than this.

Example case 2. In this case, the trainers can all take all their ideal number of lectures.

Example case 3. In this case, the first trainer arrives on day 3 and wants to take two lectures. This is not possible as he can take at most one lecture on day 3 and the camp ends on day 3. The second trainer wants to take only one lecture which he can take on any one of the 1st or 2nd days. You can see that in one of the first or second days, no lecture will be held.
"""

from heapq import heappush, heappop

def calculate_minimum_sadness(N, D, trainers):
    data = {}
    heap = []
    
    # Organize trainers by their arrival day
    for d, t, s in trainers:
        if d in data:
            data[d].append([t, s])
        else:
            data[d] = [[t, s]]
    
    # Process each day
    for d in range(1, D + 1):
        if d in data:
            for v in data[d]:
                heappush(heap, [-1 * v[1], v[0]])
        
        if len(heap):
            x = heappop(heap)
            x[1] -= 1
            if x[1]:
                heappush(heap, x)
    
    # Calculate total sadness
    ans = 0
    while len(heap):
        x = heappop(heap)
        ans += -1 * x[0] * x[1]
    
    return ans