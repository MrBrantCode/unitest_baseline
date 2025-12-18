"""
QUESTION:
There is a hallway of length $N-1$ and you have $M$ workers to clean the floor. Each worker is responsible for segment $[L_{i}, R_{i}]$, i.e., the segment starting at $L_{i}$ and ending at $R_{i}$. The segments might overlap. 

Every unit of length of the floor should be cleaned by at least one worker. A worker can clean $1$ unit of length of the floor in $1$ unit of time and can start from any position within their segment. A worker can also choose to move in any direction. However, the flow of each worker should be continuous, i.e, they can’t skip any portion and jump to the next one, though they can change their direction. What’s the minimum amount of time required to clean the floor, if the workers work simultaneously?

------ Input: ------

First line will contain $T$, number of testcases. Then the testcases follow. 
Each testcase contains of $M + 1$ lines of input.
First line contains $2$ space separated integers $N$, $M$, length of the hallway and number of workers.
Each of the next $M$ lines contain $2$ space separated integers $L_{i}$, $R_{i}$, endpoints of the segment under $i^{th}$ worker.

------ Output: ------
For each testcase, output in a single line minimum time required to clean the hallway or $-1$ if it's not possible to clean the entire floor.

------ Constraints  ------
$1 ≤ T ≤ 10^{5}$
$2 ≤ N ≤ 10^{9}$
$1 ≤ M ≤ 10^{5}$
$1 ≤ L_{i} < R_{i} ≤ N$
The sum of $M$ over all tests is atmost $2*10^{5}$

----- Sample Input 1 ------ 
3

10 3

1 10

1 5

6 10

10 1

2 10

10 2

5 10

1 5
----- Sample Output 1 ------ 
3

-1

5
----- explanation 1 ------ 
Case $1$: The first worker cleans the segment $[4, 7]$, the second cleans $[1, 4]$ and the third cleans $[7, 10]$ each taking $3$ units of time. So the minimum time required is $3$ units.

Case $2$: Segment $[1, 2]$ is not covered by any worker and hence the entire hallway can't be cleaned.

Case $3$: The first worker cleans the segment $[5, 10]$ taking $5$ units of time, and the second cleans $[1, 5]$ taking $4$ units of time. So the minimum time required is $max(5, 4) = 5$ units.
"""

def minimum_cleaning_time(N, M, segments):
    # Sort segments by their end points
    segments.sort()
    
    # Initialize binary search bounds
    l = 0
    r = N - 1
    cnt = -1
    
    while l <= r:
        mid = (l + r) // 2
        seg = 1
        
        for i in range(M):
            if seg >= segments[i][0] or segments[i][1] > seg:
                continue
            else:
                seg = min(seg + mid, segments[i][0])
        
        if seg == N:
            cnt = mid
            r = mid - 1
        else:
            l = mid + 1
    
    return cnt