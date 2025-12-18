"""
QUESTION:
This will probably be a little series :)

X-Shape

You will get an odd Integer n (>= 3) and your task is to draw a X. Each line is separated with '\n'.

Use the following characters:  ■ □

For Ruby, Crystal and PHP:   whitespace and o 

e.g.:



                                     ■□□□■
            ■□■                      □■□■□
  x(3) =>   □■□              x(5)=>  □□■□□
            ■□■                      □■□■□
                                     ■□□□■


 Series: ASCII Fun

ASCII Fun #1: X-Shape
ASCII Fun #2: Funny Dots
ASCII Fun #3: Puzzle Tiles
ASCII Fun #4: Build a pyramid
"""

def generate_x_shape(n):
    # Initialize a 2D list with '□' characters
    ret = [['□' for _ in range(n)] for _ in range(n)]
    
    # Fill the appropriate positions with '■' to form the X shape
    for i in range(n):
        ret[i][i] = '■'
        ret[i][n - 1 - i] = '■'
    
    # Join the rows into a single string with newline characters
    return '\n'.join(''.join(row) for row in ret)