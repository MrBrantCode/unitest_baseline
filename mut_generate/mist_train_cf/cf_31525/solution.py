"""
QUESTION:
Write a function named `findOrder` that takes two inputs: `numCourses` (an integer representing the number of courses) and `prerequisites` (a list of lists where each inner list contains two integers, `ai` and `bi`, indicating that course `bi` must be taken before course `ai`). The function should return a list representing a valid ordering of courses to finish all courses. If it's impossible to finish all courses, the function should return an empty list.

The input `prerequisites` represents a graph where there are no duplicate edges. The function should handle a scenario where there may be multiple valid orderings, and any of these orderings is acceptable.
"""

from collections import defaultdict, deque

def findOrder(numCourses, prerequisites):
    graph = defaultdict(list)
    indegree = [0] * numCourses
    for course, pre in prerequisites:
        graph[pre].append(course)
        indegree[course] += 1

    queue = deque([i for i in range(numCourses) if indegree[i] == 0])
    result = []
    while queue:
        node = queue.popleft()
        result.append(node)
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    return result if len(result) == numCourses else []