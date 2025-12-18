"""
QUESTION:
Implement a function `findLatestStep` that takes three parameters: `arr` (a list of integers), `m` (an integer), and `b` (a list of integers). The function should return the latest step at which there exists a group of ones of length exactly `m` in a binary string. If no such group exists, return `-1`. The binary string is constructed by setting the bit at position `arr[i]` to `1` at each step `i` if `b[i]` is `1`. The constraints are `n == arr.length == b.length`, `1 <= n <= 10^5`, `1 <= arr[i], b[i] <= n`, all integers in `arr` are distinct, and `1 <= m <= arr.length`.
"""

def findLatestStep(arr, m, b):
    n = len(arr)
    que = [(-1, n)]  
    mp = {n: 1}  
    for i in range(n - 1, -1, -1):
        idx = arr[i] - 1  
        j = 0
        while que[j][1] < idx: 
            j += 1
        
        a, b = que[j]
        que.pop(j)
        mp[b - a - 1] -= 1
        
        left, right = idx - a - 1, b - idx - 1
        if left >= 0:
            que.insert(j, (a, idx))
            if left in mp:
                mp[left] += 1
            else:
                mp[left] = 1
        if right >= 0:
            que.insert(j, (idx, b))
            if right in mp:
                mp[right] += 1
            else:
                mp[right] = 1
        if mp.get(m, 0) > 0:
            return i
    return -1