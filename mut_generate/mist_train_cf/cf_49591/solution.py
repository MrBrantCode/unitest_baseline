"""
QUESTION:
Implement the `averageWaitingTime` function, which calculates the average waiting time of all customers. The function takes a 2D list `customers` as input, where each inner list contains two integers: the arrival time and the time required to prepare the order. The function should return the average waiting time of all customers. The acceptable solutions can deviate by 10^-5 from the actual answer. The constraints are 1 <= customers.length <= 10^5, 1 <= arrival_i, time_i <= 10^4, and arrival_i <= arrival_{i+1}.
"""

import heapq

def averageWaitingTime(customers):
    n = len(customers)
    time = 0
    waiting = 0
    i = 0

    heap = []
    
    while i < n or heap:
        while i < n and (not heap or customers[i][0] <= time):
            heapq.heappush(heap, (customers[i][1], customers[i][0]))
            i += 1
            
        if heap:
            cook_time, arrive_time = heapq.heappop(heap)
            time = max(time, arrive_time) + cook_time
            waiting += time - arrive_time
        else:
            time = customers[i][0]
    
    return waiting / n