"""
QUESTION:
Write a function `findMaximizedCapital(k, W, Profits, Capital)` that returns the maximum profit achievable after investing in at most k projects. The function takes in the following parameters: 
- `k`: an integer representing the maximum number of projects you can invest in
- `W`: an integer representing the initial capital you have
- `Profits`: a list of integers representing the profits of the projects
- `Capital`: a list of integers representing the capital required to start each project. The function should maximize the total profit while respecting the constraints of the initial capital and the maximum number of projects.
"""

import heapq

def findMaximizedCapital(k, W, Profits, Capital):
    n = len(Profits)
    projects = sorted(zip(Profits, Capital), key=lambda x: x[1])  

    available_projects = []  
    for _ in range(k):
        while projects and projects[0][1] <= W:
            profit, capital = projects.pop(0)
            heapq.heappush(available_projects, -profit)  

        if available_projects:
            W -= heapq.heappop(available_projects)  
        else:
            break  

    return W