"""
QUESTION:
Implement a function `lazy_propagation` that utilizes the concept of segment trees to perform range updates and queries efficiently, specifically when dealing with a large number of updates and infrequent queries. The function should take the following inputs: 

- An array `arr` of numbers.
- A range `start` and `end` for the update operation.
- An update value `val` to be added to the elements within the range.
- A query range `q_start` and `q_end` to retrieve the updated values.

Restrictions: The function should optimize range update operations by postponing the actual updates until the nodes are queried.
"""

class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)
        self.lazy = [0] * (4 * self.n)
        self.build_tree(arr, 0, 0, self.n - 1)

    def build_tree(self, arr, node, start, end):
        if start == end:
            self.tree[node] = arr[start]
        else:
            mid = (start + end) // 2
            self.build_tree(arr, 2 * node + 1, start, mid)
            self.build_tree(arr, 2 * node + 2, mid + 1, end)
            self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]

    def update_range(self, node, start, end, range_start, range_end, val):
        if start > range_end or end < range_start:
            return
        if self.lazy[node] != 0:
            self.tree[node] += self.lazy[node] * (end - start + 1)
            if start != end:
                self.lazy[2 * node + 1] += self.lazy[node]
                self.lazy[2 * node + 2] += self.lazy[node]
            self.lazy[node] = 0
        if start >= range_start and end <= range_end:
            self.tree[node] += (end - start + 1) * val
            if start != end:
                self.lazy[2 * node + 1] += val
                self.lazy[2 * node + 2] += val
        else:
            mid = (start + end) // 2
            self.update_range(2 * node + 1, start, mid, range_start, range_end, val)
            self.update_range(2 * node + 2, mid + 1, end, range_start, range_end, val)
            self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]

    def query(self, node, start, end, range_start, range_end):
        if start > range_end or end < range_start:
            return 0
        if self.lazy[node] != 0:
            self.tree[node] += self.lazy[node] * (end - start + 1)
            if start != end:
                self.lazy[2 * node + 1] += self.lazy[node]
                self.lazy[2 * node + 2] += self.lazy[node]
            self.lazy[node] = 0
        if start >= range_start and end <= range_end:
            return self.tree[node]
        mid = (start + end) // 2
        return self.query(2 * node + 1, start, mid, range_start, range_end) + self.query(2 * node + 2, mid + 1, end, range_start, range_end)

def lazy_propagation(arr, start, end, val, q_start, q_end):
    segment_tree = SegmentTree(arr)
    segment_tree.update_range(0, 0, len(arr) - 1, start, end, val)
    return segment_tree.query(0, 0, len(arr) - 1, q_start, q_end)