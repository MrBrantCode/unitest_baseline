"""
QUESTION:
Vasya plays a computer game with ninjas. At this stage Vasya's ninja should get out of a deep canyon.

The canyon consists of two vertical parallel walls, their height is n meters. Let's imagine that we split these walls into 1 meter-long areas and number them with positive integers from 1 to n from bottom to top. Some areas are safe and the ninja can climb them. Others are spiky and ninja can't be there. Let's call such areas dangerous.

Initially the ninja is on the lower area of the left wall. He can use each second to perform one of the following actions: 

  * climb one area up; 
  * climb one area down; 
  * jump to the opposite wall. That gets the ninja to the area that is exactly k meters higher than the area he jumped from. More formally, if before the jump the ninja is located at area x of one wall, then after the jump he is located at area x + k of the other wall. 



If at some point of time the ninja tries to get to an area with a number larger than n, then we can assume that the ninja got out of the canyon.

The canyon gets flooded and each second the water level raises one meter. Initially the water level is at the lower border of the first area. Ninja cannot be on the area covered by water. We can assume that the ninja and the water "move in turns" — first the ninja performs some action, then the water raises for one meter, then the ninja performs one more action and so on.

The level is considered completed if the ninja manages to get out of the canyon.

After several failed attempts Vasya started to doubt whether it is possible to complete the level at all. Help him answer the question.

Input

The first line contains two integers n and k (1 ≤ n, k ≤ 105) — the height of the canyon and the height of ninja's jump, correspondingly.

The second line contains the description of the left wall — a string with the length of n characters. The i-th character represents the state of the i-th wall area: character "X" represents a dangerous area and character "-" represents a safe area.

The third line describes the right wall in the same format.

It is guaranteed that the first area of the left wall is not dangerous.

Output

Print "YES" (without the quotes) if the ninja can get out from the canyon, otherwise, print "NO" (without the quotes).

Examples

Input

7 3
---X--X
-X--XX-


Output

YES


Input

6 2
--X-X-
X--XX-


Output

NO

Note

In the first sample the ninja should first jump to the right wall, then go one meter down along the right wall, then jump to the left wall. The next jump can get the ninja from the canyon. 

In the second sample there's no way the ninja can get out of the canyon.
"""

from collections import deque

def can_ninja_escape(n, k, left_wall, right_wall):
    g = {}
    
    # Initialize the graph with safe areas
    for i in range(n):
        if left_wall[i] == '-':
            g[1, i + 1] = (-1, 0, 0, False)
        if right_wall[i] == '-':
            g[-1, i + 1] = (-1, 0, 0, False)
    
    # Mark the starting point
    g[1, 1] = ('VISITED', 1, 0, False)
    
    q = deque([(1, 1)])
    
    while q:
        c = q.popleft()
        up = (c[0], c[1] + 1)
        down = (c[0], c[1] - 1)
        jump = (c[0] * -1, c[1] + k)
        
        if g[c][1] <= g[c][2]:
            g[c] = (g[c][0], g[c][1], g[c][2], True)
        
        if up in g and g[up][0] == -1:
            q.append(up)
            g[up] = ('VISITED', g[c][1] + 1, g[c][2] + 1, g[c][3])
        
        if down in g and g[down][0] == -1:
            q.append(down)
            g[down] = ('VISITED', g[c][1] - 1, g[c][2] + 1, g[c][3])
        
        if jump in g and g[jump][0] == -1:
            q.append(jump)
            g[jump] = ('VISITED', g[c][1] + k, g[c][2] + 1, g[c][3])
    
    def graphHasEscape(graph):
        for node in graph:
            result = graph[node]
            if result[0] == 'VISITED' and (result[1] + 1 > n or result[1] + k > n) and (not result[3]):
                return True
        return False
    
    return 'YES' if graphHasEscape(g) else 'NO'