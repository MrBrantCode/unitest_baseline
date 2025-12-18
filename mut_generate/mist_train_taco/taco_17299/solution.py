"""
QUESTION:
Snuke has come to a store that sells boxes containing balls. The store sells the following three kinds of boxes:

* Red boxes, each containing R red balls
* Green boxes, each containing G green balls
* Blue boxes, each containing B blue balls



Snuke wants to get a total of exactly N balls by buying r red boxes, g green boxes and b blue boxes. How many triples of non-negative integers (r,g,b) achieve this?

Constraints

* All values in input are integers.
* 1 \leq R,G,B,N \leq 3000

Input

Input is given from Standard Input in the following format:


R G B N


Output

Print the answer.

Examples

Input

1 2 3 4


Output

4


Input

13 1 4 3000


Output

87058
"""

def count_valid_triples(R: int, G: int, B: int, N: int) -> int:
    """
    Counts the number of triples (r, g, b) such that:
    - r red boxes, each containing R red balls
    - g green boxes, each containing G green balls
    - b blue boxes, each containing B blue balls
    sum up to exactly N balls.

    Parameters:
    - R (int): Number of red balls in each red box.
    - G (int): Number of green balls in each green box.
    - B (int): Number of blue balls in each blue box.
    - N (int): Total number of balls Snuke wants to get.

    Returns:
    - int: Number of valid triples (r, g, b).
    """
    ans = 0
    for i in range(1 + N // R):
        r = R * i
        for j in range(1 + (N - r) // G):
            g = G * j
            if (N - r - g) % B == 0:
                ans += 1
    return ans