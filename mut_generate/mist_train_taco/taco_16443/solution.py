"""
QUESTION:
You are the head of a firm and you have to assign jobs to people. You have N persons working under you and you have N jobs that are to be done by these persons. Each person has to do exactly one job and each job has to be done by exactly one person. Each person has his own capability (in terms of time taken) to do any particular job. Your task is to assign the jobs to the persons in such a way that the total time taken is minimum. A job can be assigned to only one person and a person can do only one job.
Example 1:
Input:
N = 2
Arr[] = {3, 5, 10, 1}
Output:
4
Explanation:
The first person takes times 3 and 5
for jobs 1 and 2 respectively. The second
person takes times 10 and 1 for jobs 1 and
2 respectively. We can see that the optimal
assignment will be to give job 1 to person 1
and job 2 to person 2 for a total for 3+1 = 4.
Example 2:
Input:
N = 3
Arr[] = {2, 1, 2, 9, 8, 1, 1, 1, 1}
Output:
3 
Explanation: 
The optimal arrangement would be to assign 
job 1 to person 3,job 2 to person 1 and job 
3 to person 2.
Your Task:
You don't need to read input or print anything. Your task is to complete the function assignmentProblem() which takes an Integer N and an array Arr[] of size N^{2} as input and returns the time taken for the best possible assignment.
Expected Time Complexity: O(N^{2})
Expected Auxiliary Space: O(N^{2})
Constraints:
1 <= N <= 30
1 <= Arr[i] <= 100
"""

def minimum_assignment_cost(N, Arr):
    n = N
    l = Arr
    m = []
    mybeg = []
    for i in range(n):
        m.append(l[i * n:(i + 1) * n])
        mybeg.append(l[i * n:(i + 1) * n])

    def util():
        (u, v, ind) = ([0] * n, [0] * n, [-1] * n)
        for i in range(n):
            (links, mins, visited) = ([-1] * n, [1000] * n, [False] * n)
            (marki, markj) = (i, -1)
            while marki != -1:
                j = -1
                for j1 in range(n):
                    if not visited[j1]:
                        current = m[marki][j1] - u[marki] - v[j1]
                        if current < mins[j1]:
                            mins[j1] = current
                            links[j1] = markj
                        if j == -1 or mins[j1] < mins[j]:
                            j = j1
                delta = mins[j]
                for j1 in range(n):
                    if visited[j1]:
                        u[ind[j1]] += delta
                        v[j1] -= delta
                    else:
                        mins[j1] -= delta
                u[i] += delta
                visited[j] = True
                (markj, marki) = (j, ind[j])
            while links[j] != -1:
                ind[j] = ind[links[j]]
                j = links[j]
            ind[j] = i
        return [(ind[j], j) for j in range(n)]
    
    return sum((mybeg[x][y] for (x, y) in util()))