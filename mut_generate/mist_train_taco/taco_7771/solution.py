"""
QUESTION:
Kate constantly finds herself in some kind of a maze. Help her to find a way out!.

For a given maze and Kate's position find if there is a way out. Your function should return True or False.

Each maze is defined as a list of strings, where each char stays for a single maze "cell". ' ' (space) can be stepped on, '#' means wall and 'k' stays for Kate's starting position. Note that the maze may not always be square or even rectangular.

Kate can move left, up, right or down only.

There should be only one Kate in a maze. In any other case you have to throw an exception.


Example input
=============
```
['# ##',
 '# k#',
 '####']
```

Example output
==============
True

Example input
=============
```
['####'.
 '# k#',
 '####']
```

Example output
==============
False
"""

def can_kate_escape(maze):
    MOVES = {(0, 1), (0, -1), (1, 0), (-1, 0)}
    
    # Find Kate's position
    kate_positions = [(x, y) for x in range(len(maze)) for y in range(len(maze[x])) if maze[x][y] == 'k']
    
    if len(kate_positions) != 1:
        raise ValueError("There should be exactly one 'k' in the maze.")
    
    kate_pos = kate_positions[0]
    seen = set([kate_pos])
    pos_set = set([kate_pos])
    
    while pos_set:
        (x, y) = pos_set.pop()
        
        # Check if Kate is at the boundary
        if any((not (0 <= x + dx < len(maze) and 0 <= y + dy < len(maze[x + dx])) for (dx, dy) in MOVES)):
            return True
        
        # Find valid neighbors
        neighbors = {(x + dx, y + dy) for (dx, dy) in MOVES 
                     if 0 <= x + dx < len(maze) and 0 <= y + dy < len(maze[x + dx]) 
                     and maze[x + dx][y + dy] == ' ' 
                     and (x + dx, y + dy) not in seen}
        
        pos_set |= neighbors
        seen |= neighbors
    
    return False