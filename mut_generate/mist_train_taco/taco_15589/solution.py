"""
QUESTION:
Let's learn about list comprehensions! You are given three integers $x,y$ and $z$ representing the dimensions of a cuboid along with an integer $n$. Print a list of all possible coordinates given by $(i,j,k)$ on a 3D grid where the sum of $i+j+k$ is not equal to $n$. Here, $0\leq i\leq x;0\leq j\le y;0\leq k\leq z$.  Please use list comprehensions rather than multiple loops, as a learning exercise.  

Example 

 $x=1$ 

 $y=1$ 

 $z=2$ 

 $n=3$

All permutations of $[i,j,k]$ are: 

$[[0,0,0],[0,0,1],[0,0,2],[0,1,0],[0,1,[0,1,2],[1,0,0],[1,0,1],[1,0,2],[1,1,0],[1,1],[1,1,2]]$. 

Print an array of the elements that do not sum to $n=3$.  

$[[0,\textbf{0},\textbf{0}],[\textbf{0},\textbf{0},\textbf{1}],[\textbf{0},\textbf{0},\textbf{2}],[\textbf{0},\textbf{1},\textbf{0}],[\textbf{0},\textbf{1},\textbf{1}],[\textbf{1},\textbf{0},\textbf{0}],[\textbf{1},\textbf{0},\textbf{1}],[\textbf{1},\textbf{1},\textbf{0}],[\textbf{1},\textbf{1},\textbf{2}]]$

Input Format

Four integers $x,y,z$ and $n$, each on a separate line. 

Constraints

Print the list in lexicographic increasing order.

Sample Input 0
1
1
1
2

Sample Output 0
[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]

Explanation 0

Each variable $x,y$ and $z$ will have values of $\mbox{o}$ or $\mbox{I}$.  All permutations of lists in the form $[i,j,k]=[[0,0,0],[0,0,1],[0,1,0],[0,1,1],[1,0,0],[1,0,1],[1,1,0],[1,1,1]]$. 

Remove all arrays that sum to $n=2$ to leave only the valid permutations.

Sample Input 1
2
2
2
2

Sample Output 1
[[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 2], [0, 2, 1], [0, 2, 2], [1, 0, 0], [1, 0, 2], [1, 1, 1], [1, 1, 2], [1, 2, 0], [1, 2, 1], [1, 2, 2], [2, 0, 1], [2, 0, 2], [2, 1, 0], [2, 1, 1], [2, 1, 2], [2, 2, 0], [2, 2, 1], [2, 2, 2]]
"""

def generate_valid_coordinates(x, y, z, n):
    """
    Generates a list of all possible coordinates [i, j, k] on a 3D grid 
    where the sum of i + j + k is not equal to n.

    Parameters:
    x (int): Maximum value for the first coordinate (0 <= i <= x).
    y (int): Maximum value for the second coordinate (0 <= j <= y).
    z (int): Maximum value for the third coordinate (0 <= k <= z).
    n (int): The sum that coordinates should not equal.

    Returns:
    list: A list of lists, where each inner list represents a valid coordinate [i, j, k].
    """
    return [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n]