"""
QUESTION:
Create a function `range_update(node, start, end, l, r, val)` and `range_query(node, start, end, l, r)` in a segment tree with lazy propagation, where `range_update(node, start, end, l, r, val)` updates a range by a value and `range_query(node, start, end, l, r)` returns the minimum number in a range. The `range_update` function should only mark the segment and update it when really needed, using a lazy propagation technique to reduce the time complexity to O(log n). The input parameters are: `node` (the current node), `start` and `end` (the start and end of the current segment), `l` and `r` (the start and end of the range to update or query), and `val` (the value to update the range by).
"""

def range_update(node, start, end, l, r, val):
    if start > end or start > r or end < l: # out of bounds
        return
    if start == end: # leaf node
        tree[node] += val
        return
    mid = (start + end) // 2
    range_update(node*2, start, mid, l, r, val)
    range_update(node*2 + 1, mid + 1, end, l, r, val)
    tree[node] = min(tree[node*2], tree[node*2+1])

def range_query(node, start, end, l, r):
    if r < start or end < l:
        return 9999999 # out of bounds
    if l <= start and end <= r:
        return tree[node] # relevant segment
    mid = (start + end) // 2
    p1 = range_query(node*2, start, mid, l, r)
    p2 = range_query(node*2 + 1, mid + 1, end, l, r)
    return min(p1, p2)