"""
QUESTION:
# Fun fact
Tetris was the first video game played in outer space

In 1993, Russian cosmonaut Aleksandr A. Serebrov spent 196 days on the Mir space station with a very special distraction: a gray Game Boy loaded with Tetris. During that time the game orbited the Earth 3,000 times and became the first video game played in space. The Game Boy was sold in a Bonhams auction for $1,220 during the Space History Sale in 2011.

# Task
Parse the game log and determine how many lines have been cleared through the game. The game ends if all commands from input were interpreted or the maximum field height (30 units) is reached.

A horizontal line, according to the rules of classic Tetris, is considered cleared if it represents a solid line without gaps formed by falling blocks.
When such a line is formed, it disappears and any blocks above it fall down to fill the space.

# Input
```python
['4L2', '3R4', '4L3', '3L4', '4R0', '1L2'] # example
```
As an argument, you are given gamelog - an array of commands which you need to interpret.

Each command has the same form:
* The first character - the type of block (integer from 1 to 4, as in this kata we have only 4 types of blocks). Block types are described below.
* The second - the direction of movement (`"R"` or `"L"` - right or left).
* The third is an offset (integer from 0 to 4, as width of our field 9 units and new block always appears at the center of the field) relative to the starting position. Thus, `L4` means the leftmost position, and `R4` the rightmost, and `L0` is equivalent to `R0`.

# Output
The total number of cleaned horizontal lines (`int`) to the end of the game. Note, if the field height is exceeded, then the game ends immediately.

# Blocks
In this kata we have only 4 types of blocks. Yes, this is not a classic set of shapes, but this is only for simplicity.
```
# and their graphical representation:
             ■
         ■   ■
     ■   ■   ■
 ■   ■   ■   ■
---+---+---+---
#1  #2  #3  #4
```
# Field
Gamefield (a rectangular vertical shaft) has width 9 units and height 30 units.


table, th, td {
  border: 1px solid;
}


Indices can be represented as:


L4
L3
L2
L1
L0/R0
R1
R2
R3
R4



# Example 1
```python
>>> gamelog = ['1R4', '2L3', '3L2', '4L1', '1L0', '2R1', '3R2', '4R3', '1L4']
>>> tetris(gamelog)
1
```
Gamefield before last command (_ means empty space):
```
___■___■_
__■■__■■_
_■■■_■■■_
_■■■■■■■■
```
Gamefield after all commands:
```
___■___■_
__■■__■■_
_■■■_■■■_
```
As you can see, one solid line was cleared. So, answer is 1.

# Example 2
```python
>>> gamelog = ['1L2', '4R2', '3L3', '3L1', '1L4', '1R4']
>>> tetris(gamelog)
0
```
Gamefield after all commands:
```
 _____■__
_■_■__■__
_■_■__■__
■■■■__■_■
```
As you can see, there is no solid lines, so nothing to clear. Our answer is 0, zero cleaned lines.

# Note

Since there is no rotation of blocks in our model and all blocks are very simple, do not overthink the task.

# Other  

If you like the idea: leave feedback, and there will be more katas in the Tetris series.

* 7 kyuTetris Series #1 — Scoring System
* 6 kyuTetris Series #2 — Primitive Gameplay
* 6 kyuTetris Series #3 — Adding Rotation (TBA)
* 5 kyuTetris Series #4 — New Block Types (TBA)
* 4 kyuTetris Series #5 — Complex Block Types (TBA?)
"""

def calculate_cleared_lines(gamelog):
    pos = {'L4': 0, 'L3': 1, 'L2': 2, 'L1': 3, 'L0': 4, 'R0': 4, 'R1': 5, 'R2': 6, 'R3': 7, 'R4': 8}
    
    current = [0] * 9  # Initialize the game field with zeros
    res = 0  # Initialize the result (number of cleared lines)
    
    for command in gamelog:
        p = pos[command[1:]]  # Get the position index from the command
        current[p] += int(command[0])  # Add the block height to the corresponding position
        
        if current[p] >= 30:  # Check if the field height is exceeded
            break
        
        y = min(current)  # Find the minimum height in the current field
        if y:  # If there is a non-zero minimum height, it means a line can be cleared
            current = [v - y for v in current]  # Clear the line by reducing all heights by y
            res += y  # Increment the result by the number of cleared lines (y)
    
    return res  # Return the total number of cleared lines