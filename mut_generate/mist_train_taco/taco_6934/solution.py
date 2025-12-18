"""
QUESTION:
Nick's company employed n people. Now Nick needs to build a tree hierarchy of «supervisor-surbodinate» relations in the company (this is to say that each employee, except one, has exactly one supervisor). There are m applications written in the following form: «employee ai is ready to become a supervisor of employee bi at extra cost ci». The qualification qj of each employee is known, and for each application the following is true: qai > qbi. 

Would you help Nick calculate the minimum cost of such a hierarchy, or find out that it is impossible to build it.

Input

The first input line contains integer n (1 ≤ n ≤ 1000) — amount of employees in the company. The following line contains n space-separated numbers qj (0 ≤ qj ≤ 106)— the employees' qualifications. The following line contains number m (0 ≤ m ≤ 10000) — amount of received applications. The following m lines contain the applications themselves, each of them in the form of three space-separated numbers: ai, bi and ci (1 ≤ ai, bi ≤ n, 0 ≤ ci ≤ 106). Different applications can be similar, i.e. they can come from one and the same employee who offered to become a supervisor of the same person but at a different cost. For each application qai > qbi.

Output

Output the only line — the minimum cost of building such a hierarchy, or -1 if it is impossible to build it.

Examples

Input

4
7 2 3 1
4
1 2 5
2 4 1
3 4 1
1 3 5


Output

11


Input

3
1 2 3
2
3 1 2
3 1 3


Output

-1

Note

In the first sample one of the possible ways for building a hierarchy is to take applications with indexes 1, 2 and 4, which give 11 as the minimum total cost. In the second sample it is impossible to build the required hierarchy, so the answer is -1.
"""

def calculate_minimum_hierarchy_cost(n, qualifications, m, applications):
    # Dictionary to store the minimum cost for each subordinate
    d = {}
    
    # Process each application
    for (a, b, c) in applications:
        if b in d:
            d[b] = min(d[b], c)
        else:
            d[b] = c
    
    # Check if there is exactly one root (employee without a supervisor)
    c1 = 0
    for i in range(1, n + 1):
        if i not in d:
            c1 += 1
    
    # If there is more than one root, it's impossible to build the hierarchy
    if c1 > 1:
        return -1
    
    # Calculate the total minimum cost
    total_cost = sum(d.values())
    
    return total_cost