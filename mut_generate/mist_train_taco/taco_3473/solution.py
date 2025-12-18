"""
QUESTION:
There are two parallel roads, each containing N and M buckets, respectively. Each bucket may contain some balls. The balls in first road are given in an array a and balls in the second road in an array b. The buckets on both roads are kept in such a way that they are sorted according to the number of balls in them. Geek starts from the end of the road which has the bucket with a lower number of balls(i.e. if buckets are sorted in increasing order, then geek will start from the left side of the road).
Geek can change the road only at a point of intersection i.e. a point where buckets have the same number of balls on two roads. Help Geek collect the maximum number of balls.
 
Example 1:
Input: 
N = 5, M = 5
a[] = {1, 4, 5, 6, 8}
b[] = {2, 3, 4, 6, 9}
Output: 29
Explanation: The optimal way to get the 
maximum number of balls is to start from 
road 2. Get 2+3. Then switch at intersection 
point 4. Get 4+5+6. Then switch at intersection
point 6. Get 9. Total = 2+3+4+5+6+9 = 29.
Example 2:
Input:
N = 3, M = 3
a[] = {1, 2, 3}
b[] = {4, 5, 6}
Output: 15
 
Your Task:
You do not need to read input or print anything. Your task is to complete the function maxBalls() which takes N, M, a[] and b[] as input parameters and returns the maximum number of balls that can be collected.
 
Expected Time Complexity: O(N+M)
Expected Auxililary Space: O(1)
 
Constraints:
1 ≤ N, M ≤ 10^{3}
1 ≤ a[i], b[i] ≤ 10^{6}
"""

def max_balls(N, M, a, b):
    i = 0
    j = 0
    val1 = 0
    val2 = 0
    
    while i < N and j < M:
        if a[i] < b[j]:
            val1 += a[i]
            i += 1
        elif b[j] < a[i]:
            val2 += b[j]
            j += 1
        else:
            x = a[i]
            y = b[j]
            x1 = 0
            y1 = 0
            
            while i < N and a[i] == x:
                x1 += x
                i += 1
            while j < M and b[j] == y:
                y1 += y
                j += 1
            
            val1 = max(val1 + x1, val1 + x1 + y1 - 2 * x, val2 + x1 + y1 - x)
            val2 = max(val2 + y1, val2 + x1 + y1 - 2 * x, val1 + x1 + y1 - x)
    
    while i < N:
        val1 += a[i]
        i += 1
    
    while j < M:
        val2 += b[j]
        j += 1
    
    return max(val1, val2)