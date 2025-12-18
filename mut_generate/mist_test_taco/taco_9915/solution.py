"""
QUESTION:
You are given two four digit prime numbers Num1 and Num2. Find the distance of the shortest path from Num1 to Num2 that can be attained by altering only single digit at a time such that every number that we get after changing a digit is a four digit prime number with no leading zeros.
 
Example 1:
Input:
Num1 = 1033 
Num2 = 8179
Output: 6
Explanation:
1033 -> 1733 -> 3733 -> 3739 -> 3779 -> 8779 -> 8179.
There are only 6 steps reuired to reach Num2 from Num1. 
and all the intermediate numbers are 4 digit prime numbers.
 
Example 2:
Input:
Num1 = 1033 
Num2 = 1033
Output:
0
 
Your Task:  
You don't need to read input or print anything. Your task is to complete the function solve() which takes two integers Num1 and Num2 as input parameters and returns the distance of the shortest path from Num1 to Num2. If it is unreachable then return -1.
 
Expected Time Complexity: O(1)
Expected Auxiliary Space: O(1)
Constraints:
1000<=Num1,Num2<=9999
Num1 and Num2 are prime numbers.
"""

from math import sqrt

def is_prime(n):
    for i in range(2, int(sqrt(n)) + 1):
        if not n % i:
            return False
    return True

def shortest_path_between_primes(Num1, Num2):
    data = [False for i in range(10000)]
    visited = [False for i in range(10000)]
    output = []
    
    # Mark all 4-digit prime numbers
    for i in range(1000, 10000):
        if is_prime(i):
            data[i] = True
            output.append(i)
    
    # Create adjacency list for each prime number
    adj = [[] for i in range(10000)]
    for t in output:
        (a, b, c, d) = map(int, list(str(t)))
        for i in range(1, 10):
            if i != a and data[1000 * i + 100 * b + 10 * c + d]:
                adj[t].append(1000 * i + 100 * b + 10 * c + d)
        for i in range(10):
            if i != b and data[1000 * a + 100 * i + 10 * c + d]:
                adj[t].append(1000 * a + 100 * i + 10 * c + d)
        for i in range(10):
            if i != c and data[1000 * a + 100 * b + 10 * i + d]:
                adj[t].append(1000 * a + 100 * b + 10 * i + d)
        for i in range(10):
            if i != d and data[1000 * a + 100 * b + 10 * c + i]:
                adj[t].append(1000 * a + 100 * b + 10 * c + i)
    
    # BFS to find the shortest path
    q = [Num1]
    visited[Num1] = True
    ptr = 0
    level = 0
    while ptr < len(q):
        if q[ptr] == Num2:
            return level
        for _ in range(len(q) - ptr):
            top = q[ptr]
            if top == Num2:
                return level
            ptr += 1
            for i in adj[top]:
                if not visited[i]:
                    visited[i] = True
                    q.append(i)
        level += 1
    
    return -1