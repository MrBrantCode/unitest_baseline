"""
QUESTION:
G, a college student living in a certain sky city, has a hornworm, Imotaro. He disciplined Imotaro to eat all the food in order with the shortest number of steps. You, his friend, decided to write a program because he asked me to find out if Imotaro was really disciplined.



Input


H W N
area


Input is given in H + 1 lines. The first line contains three integers H, W, N (2 ≤ H ≤ 10, 2 ≤ W ≤ 10, 1 ≤ N ≤ 9). H is the height of the area, W is the width, and N is the number of foods (at this time, 6 + N ≤ H × W always holds).

In each line from the 2nd line to H + 1st line, ´S´, ´1´, 2´,… ´9´, ´a´, ´b´, ´c´, ´d´, ´e´, A W character string consisting of ´ # ´ and ´.´ is written, and each represents the state of each section of the area. In addition, ´S´, ´a´, ´b´, ´c´, ´d´, ´e´ represent the initial state of the hornworm. There is no food or obstacles so that it is covered with the hornworm in the initial state. In addition, the initial position of the hornworm and the position of the food are guaranteed to be entered correctly.

Output

Output the minimum number of steps when the hornworm eats food in order, or -1 if that is not possible.

Examples

Input

5 8 3
#.......
#.####2#
#.#.3..#
#.######
.1Sabcde


Output

14


Input

5 8 3
.......
.####2#
.#.3..#
.######
.1Sabcde


Output

14


Input

2 6 2
.1.baS
.2.cde


Output

7


Input

2 6 2
.1#baS
.2.cde


Output

-1
"""

from collections import deque

def find_minimum_steps(h, w, n, area):
    mp = [list('#' * (w + 2))] + [list('#' + row + '#') for row in area] + [list('#' * (w + 2))]
    init_body = [None] * 4
    init_head = None
    
    for y in range(1, h + 1):
        for x in range(1, w + 1):
            if mp[y][x] == 'S':
                init_head = (x, y)
                mp[y][x] = '.'
            if mp[y][x] == 'e':
                mp[y][x] = '.'
            if 'a' <= mp[y][x] <= 'd':
                init_body[ord(mp[y][x]) - ord('a')] = (x, y)
                mp[y][x] = '.'
            if '1' <= mp[y][x] <= '9':
                mp[y][x] = int(mp[y][x])
    
    que = deque()
    que.append((0, init_head, init_body, 1))
    mem = {}
    mem[init_head, tuple(init_body), 1] = 0
    vec = ((1, 0), (0, -1), (-1, 0), (0, 1))
    
    while que:
        (score, head, body, target) = que.popleft()
        if target > n:
            return score
        (x, y) = head
        for (dx, dy) in vec:
            (nx, ny) = (x + dx, y + dy)
            if (nx, ny) in body:
                continue
            if mp[ny][nx] == '#':
                continue
            new_target = target
            if mp[ny][nx] == target:
                new_target += 1
            new_body = tuple([head] + list(body)[:-1])
            if ((nx, ny), new_body, new_target) not in mem:
                mem[(nx, ny), new_body, new_target] = True
                que.append((score + 1, (nx, ny), new_body, new_target))
    
    return -1