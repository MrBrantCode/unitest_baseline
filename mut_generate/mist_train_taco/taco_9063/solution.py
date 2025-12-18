"""
QUESTION:
Given an array A of N integers and a 2D matrix denoting q queries. Each query consists of two elements, index and value. Update value at index in A for each query and then perform the following operations to get the result for that query.
1. Perform bitwise OR on each pair 
2. Perform bitwise XOR on each pair 
Do this alternately till you are left with only a single element in A. 
Example 1:
Input: 
N = 4
A = {1, 4, 5, 6}
q = 2
query = {{0, 2}, {3, 5}}
Output: 1 3
Explaination: 
1st query: 
Update the value of A[0] to 2 as given in 
the query pair.The array becomes {2, 4, 5, 6}.
1st iteration: Perform bitwise OR on pairs 
{2,4} and {5,6}. The array becomes {6,7}.
2nd iteration: Perform bitwise XOR on pairs 
{6,7}. The array becomes {1}.
2nd query: 
Update the value of A[3] to 5 as given in 
the query pair. The array becomes {2, 4, 5, 5}.
1st iteration: Perform bitwise OR on pairs 
{2,4} and {5,5}. The array becomes {6,5}.
2nd iteration: 6^5=3. The array becomes {3}.
Your Task:
You do not need to read input or print anything. Your task is to complete the function left() which takes N, A[], q and query as input parameters and returns a list of integers denoting the result for each query.
Expected Time Complexity:O(q*logN)
Expected Auxiliary Space: O(N)
Constraints:
1 ≤ N ≤ 10^{5}
1 ≤ A[i] ≤ 10^{5}
1 ≤ q ≤ 10^{4}
"""

def process_queries(N, A, q, query):
    class segtree:
        def __init__(self, n):
            self.st = [0] * (4 * n)
            self.size = n - 1

        def update(self, x, value, m, l=0, h=-1, i=0):
            if h == -1:
                h = self.size
            if l > h or l > x or h < x:
                return
            if l == h:
                if l == x:
                    self.st[i] = value
                return
            mid = (l + h) // 2
            self.update(x, value, m - 1, l, mid, 2 * i + 1)
            self.update(x, value, m - 1, mid + 1, h, 2 * i + 2)
            if m % 2:
                self.st[i] = self.st[2 * i + 1] | self.st[2 * i + 2]
            else:
                self.st[i] = self.st[2 * i + 1] ^ self.st[2 * i + 2]

        def query(self, x, y, l=0, h=-1, i=0):
            if h == -1:
                h = self.size
            if l > y or h < x:
                return 0
            if l >= x and h <= y:
                return self.st[i]
            if l == h:
                return 0
            mid = (l + h) // 2
            left = self.query(x, y, l, mid, 2 * i + 1)
            right = self.query(x, y, mid + 1, h, 2 * i + 2)
            return left + right

    m = 1
    x = 0
    while m < N:
        m *= 2
        x += 1
    if m != N:
        for i in range(m - N):
            A.append(0)
    st = segtree(m)
    for i in range(m):
        st.update(i, A[i], x)
    ans = []
    for (i, v) in query:
        if i < m:
            st.update(i, v, x)
            ans.append(st.query(0, m - 1))
        else:
            ans.append(-1)
    return ans