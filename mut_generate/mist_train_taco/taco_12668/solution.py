"""
QUESTION:
Given a character array tasks of size N, representing the tasks a CPU needs to do, where each letter represents a different task. Tasks could be done in any order. Each task is done in one unit of time. For each unit of time, the CPU could complete either one task or just be idle.
CPU has a cooldown period for each task. CPU can repeat a task only after atleast K units of time has passed after it did same task last time. It can perform other tasks in that time, can stay idle to wait for repeating that task.
Return the least number of units of times that the CPU will take to finish all the given tasks.
Example 1:
Input:
N = 6
K = 2
task[ ] = {'A', 'A', 'A', 'B', 'B', 'B'}
Output: 8
Explanation: 
A -> B -> idle -> A -> B -> idle -> A -> B
There is atleast 2 units of time between any two same tasks.
 
Example 2:
Input:
N = 12
K = 2
task[ ] = {'A', 'A', 'A', 'A', 'A', 'A', 'B', 'C', 'D', 'E', 'F', 'G'}
Output: 16
Explanation:  
One possible solution is 
A -> B -> C -> A -> D -> E -> A -> F -> G -> A -> idle -> idle -> A -> idle -> idle -> A.
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function leastInterval() which takes the interger N, integer K and an character array tasks as parameters and returns the minimum unit of time required to complete all tasks.
Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)
Constraints:
1 ≤ N ≤ 10^{4}
0 ≤ K ≤ 100
task_{i }is upper-case English letter.
"""

import heapq

def least_interval(N, K, tasks):
    dic = {}
    for task in tasks:
        if task in dic:
            dic[task] += 1
        else:
            dic[task] = 1
    
    heap = []
    for task, count in dic.items():
        heapq.heappush(heap, [-count, task])
    
    time = 0
    while heap:
        temp = []
        for _ in range(K + 1):
            if heap:
                count, task = heapq.heappop(heap)
                if count < -1:
                    temp.append([count + 1, task])
            time += 1
            if not heap and not temp:
                break
        
        for item in temp:
            heapq.heappush(heap, item)
    
    return time