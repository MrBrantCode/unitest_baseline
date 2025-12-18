"""
QUESTION:
The mayor of Amida, the City of Miracle, is not elected like any other city. Once exhausted by long political struggles and catastrophes, the city has decided to leave the fate of all candidates to the lottery in order to choose all candidates fairly and to make those born under the lucky star the mayor. I did. It is a lottery later called Amidakuji.

The election is held as follows. The same number of long vertical lines as the number of candidates will be drawn, and some horizontal lines will be drawn there. Horizontal lines are drawn so as to connect the middle of adjacent vertical lines. Below one of the vertical lines is written "Winning". Which vertical line is the winner is hidden from the candidates. Each candidate selects one vertical line. Once all candidates have been selected, each candidate follows the line from top to bottom. However, if a horizontal line is found during the movement, it moves to the vertical line on the opposite side to which the horizontal line is connected, and then traces downward. When you reach the bottom of the vertical line, the person who says "winning" will be elected and become the next mayor.

This method worked. Under the lucky mayor, a peaceful era with few conflicts and disasters continued. However, in recent years, due to population growth, the limits of this method have become apparent. As the number of candidates increased, the Amidakuji became large-scale, and manual tabulation took a lot of time. Therefore, the city asked you, the programmer of the city hall, to computerize the Midakuji.

Your job is to write a program that finds the structure of the Amidakuji and which vertical line you will eventually reach given the position of the selected vertical line.

The figure below shows the contents of the input and output given as a sample.

<image>

Input

The input consists of multiple datasets. One dataset is given as follows.

> n m a
> Horizontal line 1
> Horizontal line 2
> Horizontal line 3
> ...
> Horizontal line m
>

n, m, and a are integers that satisfy 2 <= n <= 100, 0 <= m <= 1000, 1 <= a <= n, respectively. Represents a number.

The horizontal line data is given as follows.

> h p q

h, p, and q are integers that satisfy 1 <= h <= 1000, 1 <= p <q <= n, respectively, h is the height of the horizontal line, and p and q are connected to the horizontal line 2 Represents the number of the vertical line of the book.

No two or more different horizontal lines are attached to the same height of one vertical line.

At the end of the input, there is a line consisting of only three zeros separated by blanks.

Output

Output one line for each dataset, the number of the vertical line at the bottom of the vertical line a when traced from the top.

Sample Input


4 4 1
3 1 2
2 2 3
3 3 4
1 3 4
0 0 0


Output for the Sample Input


Four






Example

Input

4 4 1
3 1 2
2 2 3
3 3 4
1 3 4
0 0 0


Output

4
"""

def find_mayor_amidakuji(n, m, a, horizontal_lines):
    # Sort horizontal lines by height in descending order
    horizontal_lines.sort(key=lambda x: x[0], reverse=True)
    
    # Initialize the current vertical line position
    current_line = a
    
    # Process each horizontal line
    for line in horizontal_lines:
        if line[1] == current_line:
            current_line = line[2]
        elif line[2] == current_line:
            current_line = line[1]
    
    # Return the final position of the vertical line
    return current_line