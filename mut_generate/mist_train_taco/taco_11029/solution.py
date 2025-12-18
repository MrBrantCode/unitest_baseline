"""
QUESTION:
Yukiya, the owner of Aizuyama Ski Resort, has prepared a course for advanced skiers with obstacles and jumping hills. There are various ways to slide on the course, and users who can slide in all patterns during the season will be given a gift.

Let's create a program for the oil tree shop that outputs the number of patterns of how to slide based on the floor plan of the course.

<image>



The course is represented by a grid of X x Y squares as shown above. It is assumed that the origin is at the upper left, the x coordinate increases as it goes to the right, and the y coordinate increases as it goes down.

Each gliding pattern starts at the highest point (y = 1, but without obstacles) and progresses towards the goal (y = Y). A runner in a grid square (x, y) can move to either (x − 1, y + 1), (x, y + 1), or (x + 1, y + 1). I will. There are obstacles and jumping platforms in the squares, and you cannot enter the squares with obstacles, and when you enter the squares with jumping platforms, you will move to (x, y + 2). However, there is no jumping platform in the highest cell (the cell with y = 1), and when entering a cell with a jumping platform, you can only enter from the cell with the same x coordinate. Starting from the top of the course (y = 1) and crossing the bottom without deviating from the course (y ≥ Y), it is considered as one way of sliding and ends.

Create a program that takes the course information as input and outputs the total number of slips.



Input

A sequence of multiple datasets is given as input. The end of the input is indicated by two lines of zeros. Each dataset is given in the following format:


X Y
c11 c21 ... cX1
c12 c22 ... cX2
::
c1Y c2Y ... cXY


The first line gives the course size X, Y (1 ≤ X, Y ≤ 15). Course information is given in the Y line that follows. cij (one of 0, 1, or 2) is an integer that represents the information of the squares of x = i, y = j, where 0 is a movable square, 1 is a square with an obstacle, and 2 is a square with a jumping platform. Represents.

The number of datasets does not exceed 50.

Output

For each input dataset, the number of patterns of how to slide the course is output on one line.

Example

Input

5 5
0 0 0 0 1
2 1 0 2 0
1 0 0 1 1
0 2 1 2 0
0 1 0 0 0
5 5
0 0 1 0 0
2 1 0 2 0
1 0 0 1 1
0 2 1 2 0
0 1 0 0 0
15 15
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0


Output

8
6
52694573
"""

def count_sliding_patterns(X, Y, course):
    (BLANK, OBSTACLE, JUMP) = (0, 1, 2)
    ans = 0
    dy = [1, 1, 1]
    dx = [0, -1, 1]
    x_limit = X
    y_limit = Y
    path = defaultdict(int)
    Q = deque()
    
    for x in range(X):
        if course[0][x] == BLANK:
            t = f'{x}_{0}'
            Q.append((x, 0))
            path[t] = 1
    
    while Q:
        cx, cy = Q.popleft()
        t = f'{cx}_{cy}'
        num = path.pop(t)
        
        if course[cy][cx] == OBSTACLE:
            continue
        elif course[cy][cx] == JUMP:
            if cy + 2 > y_limit - 1:
                ans += num
            else:
                t = f'{cx}_{cy + 2}'
                if not path[t]:
                    Q.append((cx, cy + 2))
                path[t] += num
            continue
        elif cy == y_limit - 1:
            ans += num
            continue
        
        for i in range(3):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < x_limit:
                if course[ny][nx] == JUMP and dx[i] == 0:
                    if ny + 2 > y_limit - 1:
                        ans += num
                    else:
                        t = f'{nx}_{ny + 2}'
                        if not path[t]:
                            Q.append((nx, ny + 2))
                        path[t] += num
                elif course[ny][nx] == BLANK:
                    if ny >= y_limit - 1:
                        ans += num
                    else:
                        t = f'{nx}_{ny}'
                        if not path[t]:
                            Q.append((nx, ny))
                        path[t] += num
    
    return ans