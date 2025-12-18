"""
QUESTION:
Nitika recently read about XOR operation and she got obssessed with it. She has an array a containing N Positive integers.She wants to perform Q queries on the array.In a query She gives two integers L and R.(1 based indexing).Now, she asks what is the xor of all the elements of the array after not including the subarray ranging from L to R (both inclusive).Nitika guarantees that in each query, The resulting array is non empty. The queries are given in a 2D matrix query having L and R for each entry. 
Example 1:
Input: N = 10, Q = 3
a = {4, 7, 8, 5, 9, 6, 1, 0, 20, 10}
query = {{3, 8},{1, 6},{2, 3}}
Output: 
29
31
17
Explaination: For the first query: 
The resulting array is: (4 ,7 ,20, 10).
Their Xor will be: 29. 
For the Second query: The resulting 
array is: (1, 0, 20, 10). Their Xor 
will be: 31. 
For the Third query:  The resulting 
array is: (4, 5, 9, 6, 1,0 ,20, 10). 
Their Xor will be: 17.
Your Task:
you do not need to read input or print anything. Your task is to complete the function specialXor() which takes N, Q, a[] and query as input parameters and returns a list containing answer for each query.
Expected Time Complexity: O(N+Q*logN)
Expected Auxiliary Space: O(N+Q)
Constraints:
1 ≤ N, Q ≤ 10^{5}
1 ≤ A[i] ≤ 10^{9}
1 ≤ L, R ≤ N
"""

def calculate_special_xor(N, Q, a, query):
    class SegmentTree:
        def __init__(self, arr):
            self.arr = arr
            self.n = len(arr)
            self.seg = [0] * self.n * 4

            def build(ind, low, high):
                if low == high:
                    self.seg[ind] = arr[low]
                    return
                mid = low + high >> 1
                build(ind * 2 + 1, low, mid)
                build(ind * 2 + 2, mid + 1, high)
                self.seg[ind] = self.seg[ind * 2 + 1] ^ self.seg[ind * 2 + 2]
            build(0, 0, self.n - 1)

        def query(self, ind, low, high, l, r):
            if low > r or l > high:
                return 0
            if low >= l and high <= r:
                return self.seg[ind]
            mid = low + high >> 1
            left = self.query(ind * 2 + 1, low, mid, l, r)
            right = self.query(ind * 2 + 2, mid + 1, high, l, r)
            return left ^ right

    s = SegmentTree(a)
    ans = 0
    for i in a:
        ans ^= i
    res = []
    for (i, j) in query:
        temp = s.query(0, 0, N - 1, i - 1, j - 1)
        res.append(ans ^ temp)
    return res