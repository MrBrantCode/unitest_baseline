"""
QUESTION:
The function `findOrder` takes in two parameters: `numCourses`, the total number of courses to be completed, and `prerequisites`, a list of pairs where `prerequisites[i] = [ai, bi]` indicates that course `bi` must be completed before course `ai`. The function should return a sequence of courses that can be taken to complete all courses, or an empty array if it is not feasible to complete all courses. The constraints are `1 <= numCourses <= 2000` and `0 <= prerequisites.length <= numCourses * (numCourses - 1)`.
"""

def findOrder(numCourses, prerequisites):
    """
    Returns a sequence of courses that can be taken to complete all courses.
    
    Parameters:
    numCourses (int): The total number of courses to be completed.
    prerequisites (list): A list of pairs where prerequisites[i] = [ai, bi] 
                          indicates that course bi must be completed before course ai.
    
    Returns:
    list: A sequence of courses that can be taken to complete all courses, 
          or an empty array if it is not feasible to complete all courses.
    """
    
    # Initialize an array, indegree, to keep track of the number of prerequisites each course has.
    indegree = [0] * numCourses
    
    # Initialize a list, graph, to serve as an adjacency list.
    graph = [[] for _ in range(numCourses)]
    
    # Loop through the prerequisites array and add the course to the graph of each prerequisite course 
    # and increment the indegree of the course.
    for x, y in prerequisites:
        graph[y].append(x)
        indegree[x] += 1
    
    # Initialize a queue, Q, to handle courses which have no prerequisites.
    Q = [i for i in range(numCourses) if indegree[i] == 0]
    
    # Initialize an array to store the result.
    res = []
    
    # Begin a loop while Q is not empty and remove the first course, u, from the queue. 
    # For every course v in graph[u], decrement its indegree by 1 because one of its prerequisites has been removed. 
    # If indegree[v] becomes 0, add it to Q because v doesn’t have any prerequisites.
    while Q:
        u = Q.pop(0)
        res.append(u)
        for v in graph[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                Q.append(v)
    
    # If a solution exists, every course will be in the queue exactly once. 
    # Thus, the number of courses that were in the queue would be equal to the total number of courses. 
    # If they are not equal then return an empty array.
    return res if len(res) == numCourses else []