"""
QUESTION:
Write a function `minMedianEnergy(cube)` that takes a 3D list `cube` of size N*N*N as input, where each cell represents an energy level. The function should find a route from the top-left-front cell to the bottom-right-back cell with the minimum median energy level, where each move can only be right, down, or deeper, and the difference in energy levels between two adjacent cells cannot exceed 10 units. The median energy level is calculated as the middle value when all energy levels are sorted in ascending order. If no such route exists, return `None`.
"""

import heapq

def minMedianEnergy(cube):
    n = len(cube)
    heap = [(cube[0][0][0], (0, 0, 0))]
    visited = set([(0,0,0)])
    dx, dy, dz = [0,0,1], [0,1,0], [1,0,0]
    prev = {(0, 0, 0): None}

    while heap:
        energy, (x, y, z) = heapq.heappop(heap)

        if (x, y, z) == (n-1, n-1, n-1):
            path = [(x, y, z)]
            while prev[path[0]]:
                path.insert(0, prev[path[0]])
            energy_list = [cube[x][y][z] for (x,y,z) in path]
            m = len(energy_list)
            median = (energy_list[(m-1)//2] + energy_list[m//2]) / 2 if m % 2 == 0 else energy_list[m//2]
            return median
        
        for i in range(3):
            nx, ny, nz = x + dx[i], y + dy[i], z + dz[i]
            if nx < n and ny < n and nz < n and abs(cube[nx][ny][nz] - cube[x][y][z]) <= 10 and (nx, ny, nz) not in visited:
                heapq.heappush(heap, (cube[nx][ny][nz], (nx, ny, nz)))
                visited.add((nx, ny, nz))
                prev[(nx, ny, nz)] = (x, y, z)

    return None