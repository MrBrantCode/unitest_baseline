"""
QUESTION:
The University of Aizu has a park covered with grass, and there are no trees or buildings that block the sunlight. On sunny summer days, sprinklers installed in the park operate to sprinkle water on the lawn. The frog Pyonkichi lives in this park. Pyonkichi is not good at hot weather, and on summer days when the sun is strong, he will dry out and die if he is not exposed to the water of the sprinkler. The sprinklers installed in the park are supposed to sprinkle only one sprinkler at a time to save water, so Pyonkichi must move according to the operation of the sprinklers.

<image>
---
(a) Map of the park

<image> | <image>
--- | ---
(b) Pyonkichi's jump range | (c) Sprinkler watering range



The park is as shown in (a) of the above figure, the location in the park is represented by the coordinates 0 to 9 in each of the vertical and horizontal directions, and the black ● is the sprinkler, which indicates the order in which the numbers operate. This is just an example, and the location and order of operation of each sprinkler changes daily.

Pyonkichi is clumsy, so he can only jump a certain distance to move. Pyonkichi's jumpable range is as shown in (b) above, and he cannot move to any other location. Moreover, one jump consumes a lot of physical strength, so you have to rest in the water for a while.

The range in which the sprinkler can sprinkle water is as shown in the above figure (c), including the coordinates of the sprinkler itself. Each sprinkler will stop after a period of watering, and the next sprinkler will start working immediately. Pyonkichi shall jump only once at this time, and shall not jump until the next watering stops. Also, since the park is surrounded on all sides by scorching asphalt, it is assumed that you will not jump in a direction that would cause you to go out of the park.

This summer was extremely hot. Was Pyonkichi able to survive? One day, read the initial position of Pyonkichi, the position of the sprinkler and the operation order, and if there is a movement path that Pyonkichi can survive, "OK", how? If you die even if you do your best, create a program that outputs "NA". However, the maximum number of sprinklers is 10, and Pyonkichi will jump from the initial position at the same time as the first sprinkler is activated.



Input

Given multiple datasets. Each dataset is given in the following format:


px py
n
x1 y1 x2 y2 ... xn yn


The first line gives the abscissa px and ordinate py of the initial position of Pyonkichi. The second line gives the number of sprinklers n. The third line gives the abscissa xi and the ordinate yi of the sprinkler that operates third.

The input ends with two zero lines. The number of datasets does not exceed 20.

Output

For each dataset, print OK if it is alive, or NA on one line otherwise.

Example

Input

6 1
10
6 4 3 3 1 2 0 5 4 6 1 8 5 9 7 7 8 6 8 3
6 1
10
6 4 3 3 1 2 0 5 4 6 1 8 5 9 7 7 8 6 9 0
0 0


Output

OK
NA
"""

def can_pyonkichi_survive(px, py, n, sprinklers):
    move = [[-1, 2], [0, 2], [1, 2], [-1, -2], [0, -2], [1, -2], [2, 1], [2, 0], [2, -1], [-2, 1], [-2, 0], [-2, -1]]
    spraing_range = [[-1, 1], [0, 1], [1, 1], [-1, 0], [0, 0], [1, 0], [-1, -1], [0, -1], [1, -1]]

    def make_fields(sprinklers_x, sprinklers_y):
        fields = []
        for x, y in zip(sprinklers_x, sprinklers_y):
            field = [[0] * 10 for _ in range(10)]
            for dx, dy in spraing_range:
                nx = x + dx
                ny = y + dy
                if nx < 0 or ny < 0 or nx > 9 or ny > 9:
                    continue
                field[ny][nx] = 1
            fields.append(field)
        return fields

    def bfs(fields, init_px, init_py, n):
        q = [[init_px, init_py, 0]]
        while q:
            px, py, count = q.pop(0)
            if count == n:
                return True
            for dx, dy in move:
                nx = px + dx
                ny = py + dy
                if nx < 0 or ny < 0 or nx > 9 or ny > 9 or fields[count][ny][nx] == 0:
                    continue
                q.append([nx, ny, count + 1])
        return False

    sprinklers_x = [sprinkler[0] for sprinkler in sprinklers]
    sprinklers_y = [sprinkler[1] for sprinkler in sprinklers]
    fields = make_fields(sprinklers_x, sprinklers_y)
    
    if bfs(fields, px, py, n):
        return "OK"
    else:
        return "NA"