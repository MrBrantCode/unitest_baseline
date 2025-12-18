"""
QUESTION:
You have full control over a robot that walks around in a rectangular field paved with square tiles like a chessboard. There are m columns of tiles from west to east, and n rows of tiles from south to north (1 <= m, n <= 100). Each tile is given a pair of coordinates, such as (i, j), where 1 <= i <= m and 1 <= j <= n.

Your robot is initially on the center of the tile at (1, 1), that is, one at the southwest corner of the field, facing straight north. It can move either forward or backward, or can change its facing direction by ninety degrees at a time, according to a command you give to it, which is one of the following.

* `FORWARD` k
Go forward by k tiles to its facing direction (1 <= k < 100).
* `BACKWARD` k
Go backward by k tiles, without changing its facing direction (1 <= k < 100).
* `RIGHT`
Turn to the right by ninety degrees.
* `LEFT`
Turn to the left by ninety degrees.
* `STOP`
Stop.


While executing either a "`FORWARD`" or a "`BACKWARD`" command, the robot may bump against the wall surrounding the field. If that happens, the robot gives up the command execution there and stands at the center of the tile right in front of the wall, without changing its direction.

After finishing or giving up execution of a given command, your robot will stand by for your next command.



Input

The input consists of one or more command sequences. Each input line has at most fifty characters.

The first line of a command sequence contains two integer numbers telling the size of the field, the first number being the number of columns and the second being the number of rows. There might be white spaces (blanks and/or tabs) before, in between, or after the two numbers. Two zeros as field size indicates the end of input.

Each of the following lines of a command sequence contains a command to the robot. When a command has an argument, one or more white spaces are put between them. White spaces may also appear before and after the command and/or its argument.

A command sequence is terminated by a line containing a "`STOP`" command. The next command sequence, if any, starts from the next line.

Output

The output should be one line for each command sequence in the input. It should contain two numbers i and j of the coordinate pair (i, j), in this order, of the tile on which your robot stops. Two numbers should be separated by one white spaces.

Example

Input

6 5
FORWARD 3
RIGHT
FORWARD 5
LEFT
BACKWARD 2
STOP
3 1
FORWARD 2
STOP
0 0


Output

6 2
1 1
"""

def execute_robot_commands(field_size, commands):
    col, row = field_size
    robot = [1, 1]
    direction = 'up'
    
    for command in commands:
        if command == 'STOP':
            break
        elif command == 'LEFT':
            if direction == 'up':
                direction = 'left'
            elif direction == 'left':
                direction = 'down'
            elif direction == 'down':
                direction = 'right'
            else:
                direction = 'up'
        elif command == 'RIGHT':
            if direction == 'up':
                direction = 'right'
            elif direction == 'left':
                direction = 'up'
            elif direction == 'down':
                direction = 'left'
            else:
                direction = 'down'
        else:
            di, step = command.split()
            step = int(step)
            if direction == 'up':
                if di == 'FORWARD':
                    robot[1] = min(robot[1] + step, row)
                else:
                    robot[1] = max(robot[1] - step, 1)
            elif direction == 'left':
                if di == 'FORWARD':
                    robot[0] = max(robot[0] - step, 1)
                else:
                    robot[0] = min(robot[0] + step, col)
            elif direction == 'down':
                if di == 'FORWARD':
                    robot[1] = max(robot[1] - step, 1)
                else:
                    robot[1] = min(robot[1] + step, row)
            else:  # direction == 'right'
                if di == 'FORWARD':
                    robot[0] = min(robot[0] + step, col)
                else:
                    robot[0] = max(robot[0] - step, 1)
    
    return tuple(robot)