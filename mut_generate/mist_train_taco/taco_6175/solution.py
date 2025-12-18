"""
QUESTION:
Your task is to write a function which counts the number of squares contained in an ASCII art picture.

The input pictures contain rectangles---some of them squares---drawn with the characters `-`, `|`, and `+`, where `-` and `|` are used to represent horizontal and vertical sides, and `+` is used to represent corners and intersections. Each picture may contain multiple, possibly overlapping, rectangles.

A simple example input looks like this:

    +--+  +----+
    |  |  |    |    +-+
    |  |  +----+    | |
    +--+            +-+
    
There are two squares and one rectangle in this picture, so your function should return 2 for this input.

The following picture does not contain any squares, so the answer for this one is 0:

    +------+
    |      |
    +------+

Here is another, more complex input:

    +---+
    |   |
    | +-+-+
    | | | |
    +-+-+ |
      |   |
      +---+

The answer for this one is 3: two big squares, and a smaller square formed by the intersection of the two bigger ones. Similarly, the answer for the following picture is 5:

    +-+-+
    | | |
    +-+-+
    | | |
    +-+-+

You are going to implement a function `count_squares()` which takes an ASCII art picture as input and returns the number of squares the picture shows. The input to that function is an array of strings, where each string corresponds to a line of the ASCII art picture. Each string is guaranteed to contain only the characters `-`, `|`, `+`, and `` `` (space).

The smallest valid square has a side length of 2 and is represented by four `+` characters arranged in a square; a single `+` character is not considered a square.

Have fun!
"""

def count_squares(lines):
    def is_square(i, j, size):
        try:
            # Check if all corners are '+'
            if (lines[i][j] == '+' and
                lines[i + size][j] == '+' and
                lines[i][j + size] == '+' and
                lines[i + size][j + size] == '+'):
                
                # Check horizontal sides
                if all(lines[i][c] in '-+' for c in range(j + 1, j + size)) and \
                   all(lines[i + size][c] in '-+' for c in range(j + 1, j + size)):
                    
                    # Check vertical sides
                    if all(lines[r][j] in '|+' for r in range(i + 1, i + size)) and \
                       all(lines[r][j + size] in '|+' for r in range(i + 1, i + size)):
                        
                        return True
            return False
        except IndexError:
            return False

    count = 0
    for i, row in enumerate(lines[:-1]):
        for j, char in enumerate(row[:-1]):
            if char == '+':
                for size in range(1, min(len(lines) - i, len(row) - j)):
                    if is_square(i, j, size):
                        count += 1
    return count