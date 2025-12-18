"""
QUESTION:
Implement a function `judgeCircle(moves: str, obstacles: list) -> bool` that determines if a robot ends up at the origin (0, 0) after a sequence of moves without hitting any obstacles. The robot starts at the origin and moves according to the characters in the `moves` string, where 'U' is up, 'D' is down, 'L' is left, and 'R' is right. The `obstacles` list contains pairs of integers representing the coordinates of obstacles that the robot cannot move to. The function should return `True` if the robot ends up at the origin and `False` otherwise. The input constraints are 1 <= `moves.length` <= 2 * 10^4, `moves` only contains 'U', 'D', 'L', and 'R', 0 <= `obstacles.length` <= 10^4, and -10^4 <= `obstacles[i][j]` <= 10^4.
"""

def judgeCircle(moves: str, obstacles: list) -> bool:
    direction = {'U': [0, 1], 'D': [0,-1], 'L': [-1, 0], 'R': [1, 0]}
    pos = [0, 0]
    obstacles = set(tuple(x) for x in obstacles)
    for move in moves:
        temp_pos = [pos[0] + direction[move][0], pos[1] + direction[move][1]]
        if tuple(temp_pos) not in obstacles:
            pos = temp_pos
        else:
            break
    return pos == [0, 0]