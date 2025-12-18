"""
QUESTION:
Given a symmetric matrix `M` of size `N x N` representing friend relationships between students, where `M[i][j] = 1` means student `i` and student `j` are friends and `M[i][i] = 1` for all students, implement a function `findCircleNum` to find the total number of friend circles in the class, where a friend circle is a group of students who are direct or indirect friends. The number of students `N` is in the range `[1, 200]`.
"""

def findCircleNum(M):
    def dfs(student, visited):
        for friend in range(len(M)):
            if M[student][friend] == 1 and friend not in visited:
                visited.add(friend)
                dfs(friend, visited)

    num_students = len(M)
    visited = set()
    circles = 0
    for student in range(num_students):
        if student not in visited:
            dfs(student, visited)
            circles += 1
    return circles