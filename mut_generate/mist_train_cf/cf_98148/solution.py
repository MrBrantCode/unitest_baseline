"""
QUESTION:
Write a function `count_groups` that takes a 2D array `arr` as input, where each element represents a color, and returns the number of groups of contiguous elements of the same color with a minimum size of 100 elements. The function should have a time complexity of O(n), where n is the number of elements in the array.
"""

def count_groups(arr):
    n, m = len(arr), len(arr[0])
    visited = set()
    count = 0
    
    def dfs(i, j, color):
        size = 1
        stack = [(i, j)]
        while stack:
            x, y = stack.pop()
            visited.add((x, y))
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and (nx, ny) not in visited and arr[nx][ny] == color:
                    size += 1
                    visited.add((nx, ny))
                    stack.append((nx, ny))
        if size >= 100:
            return True
        return False
    
    for i in range(n):
        for j in range(m):
            if (i, j) not in visited:
                if dfs(i, j, arr[i][j]):
                    count += 1
                    
    return count