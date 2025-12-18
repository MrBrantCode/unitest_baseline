"""
QUESTION:
In this challenge, the task is to debug the existing code to successfully execute all provided test files.

There are $n$ boxes in front of you. For each $\boldsymbol{i}$, box $\boldsymbol{i}$ contains $r[i]$ red balls, $g[i]$ green balls, and $b[i]$ blue balls. 

You want to separate the balls by their color. In each operation, you can pick a single ball from some box and put it into another box. The balls are separated if no box contains balls of more than one color.

Debug the given function min_operations and compute the minimal number of operations required to separate the balls.

Note: In this problem you can modify at most six lines of code and you cannot add any new lines.

To restore the original code, click on the icon to the right of the language selector.

Input Format

The first line contains a single integer $n$.
The next $n$ lines $\boldsymbol{i}$ contain three space-separated integers, $r[i]$, $g[i]$, and $b[i]$, respectively.

Constraints

$1\leq n\leq100$ 

$0\leq r[i],\ g[i],\ b[i]\leq105$ 

Output Format

Print the minimal number of operations required to separate the balls. If this is impossible, return $-1$.

Sample Input
3
1 1 1
1 1 1
1 1 1

Sample Output
6

Explanation

Each box contains 1 ball of each color.  In this explanation, the goal will be to let the first box contain only red balls, the second box only blue balls, and the third box only green balls.   

Move 1 blue ball and 1 green ball from the first box to the second and third boxes.   
Move 1 red ball and 1 green ball from the second box to the first and third boxes.   
Move 1 red ball and 1 blue ball from the third box to the first and second boxes.   

The number of operations is 6.
"""

def min_operations(n, boxes):
    def Max(a, b, c):
        if a > b:
            if a > c:
                return a
            else:
                return c
        elif b > c:
            return b
        else:
            return c

    (tr, tb, tg) = (0, 0, 0)
    for i in range(n):
        if boxes[i][0] > 0:
            tr = 1
        if boxes[i][1] > 0:
            tg = 1
        if boxes[i][2] > 0:
            tb = 1
    
    if tr + tg + tb > n:
        return -1
    
    Moves = 0
    for i in range(n):
        Moves = Moves + boxes[i][0] + boxes[i][1] + boxes[i][2] - Max(boxes[i][0], boxes[i][1], boxes[i][2])
    
    return Moves