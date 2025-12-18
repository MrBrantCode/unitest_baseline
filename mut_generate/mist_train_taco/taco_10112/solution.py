"""
QUESTION:
You will be given a string (x) featuring a cat 'C', a dog 'D' and a mouse 'm'. The rest of the string will be made up of '.'. 

You need to find out if the cat can catch the mouse from it's current position. The cat can jump (j) characters. 

Also, the cat cannot jump over the dog.

So:

if j = 5:

```..C.....m.``` returns 'Caught!'  <-- not more than j characters between

```.....C............m......``` returns 'Escaped!'  <-- as there are more than j characters between the two, the cat can't jump far enough

if j = 10:

```...m.........C...D``` returns 'Caught!' <--Cat can jump far enough and jump is not over dog

```...m....D....C.......``` returns 'Protected!' <-- Cat can jump far enough, but dog is in the way, protecting the mouse

Finally, if all three animals are not present, return 'boring without all three'
"""

def cat_mouse_game(x, j):
    # Find the positions of the cat, dog, and mouse
    d = x.find('D')
    c = x.find('C')
    m = x.find('m')
    
    # Check if any of the characters are missing
    if -1 in [d, c, m]:
        return 'boring without all three'
    
    # Check if the cat can catch the mouse within the jump distance
    if abs(c - m) <= j:
        # Check if the dog is in the way
        if (c < d < m) or (m < d < c):
            return 'Protected!'
        else:
            return 'Caught!'
    
    # If the cat cannot catch the mouse within the jump distance
    return 'Escaped!'