"""
QUESTION:
Given the total number of courses `n`, a list of direct `prerequisites` pairs, a list of `optionalPrerequisites` pairs, and a list of `queries` pairs, implement the function `checkIfPrerequisite` to return a list of boolean values indicating whether the course `queries[i][0]` is a prerequisite (either direct or optional) of the course `queries[i][1]` or not.

Restrictions: 
- `2 <= n <= 100`
- `0 <= prerequisite.length <= (n * (n - 1) / 2)`
- `0 <= optionalPrerequisite.length <= (n * (n - 1) / 2)`
- `1 <= queries.length <= 10^4`
- The prerequisites graph and the optional prerequisites graph have no cycles and no repeated edges.
"""

from typing import List

def checkIfPrerequisite(n: int, prerequisites: List[List[int]], optionalPrerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
    matrix = [[False] * n for _ in range(n)]
    for course_a, course_b in prerequisites + optionalPrerequisites:
        matrix[course_a][course_b] = True
        
    for k in range(n):
        for i in range(n):
            for j in range(n):
                matrix[i][j] = matrix[i][j] or (matrix[i][k] and matrix[k][j])
            
    return [matrix[a][b] for a, b in queries]