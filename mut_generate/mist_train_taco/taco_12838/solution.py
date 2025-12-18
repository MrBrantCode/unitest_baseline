"""
QUESTION:
Notes

Template in C

Constraints

* 1 ≤ n ≤ 100000
* 1 ≤ q ≤ 1000
* 1 ≤ timei ≤ 50000
* 1 ≤ length of namei ≤ 10
* 1 ≤ Sum of timei ≤ 1000000

Input

n q
name1 time1
name2 time2
...
namen timen


In the first line the number of processes n and the quantum q are given separated by a single space.

In the following n lines, names and times for the n processes are given. namei and timei are separated by a single space.

Output

For each process, prints its name and the time the process finished in order.

Example

Input

5 100
p1 150
p2 80
p3 200
p4 350
p5 20


Output

p2 180
p5 400
p1 450
p3 550
p4 800
"""

def process_tasks_with_quantum(n, q, tasks):
    from collections import deque
    
    # Convert tasks into a deque of tuples (name, time)
    task_queue = deque(tasks)
    
    # Initialize the total time counter
    total_time = 0
    
    # List to store the results
    results = []
    
    # Process each task in the queue
    while task_queue:
        name, time = task_queue.popleft()
        
        if time > q:
            time -= q
            total_time += q
            task_queue.append((name, time))
        else:
            total_time += time
            results.append((name, total_time))
    
    return results