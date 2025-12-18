"""
QUESTION:
Write a program which finds a pattern $p$ in a ring shaped text $s$.


<image>

Constraints

* $1 \leq $ length of $p \leq $ length of $s \leq 100$
* $s$ and $p$ consists of lower-case letters

Input

In the first line, the text $s$ is given.
In the second line, the pattern $p$ is given.

Output

If $p$ is in $s$, print Yes in a line, otherwise No.

Examples

Input

vanceknowledgetoad
advance


Output

Yes


Input

vanceknowledgetoad
advanced


Output

No
"""

def find_pattern_in_ring(s: str, p: str) -> str:
    """
    Determines if the pattern `p` exists in the ring-shaped text `s`.

    Parameters:
    - s (str): The ring-shaped text.
    - p (str): The pattern to search for.

    Returns:
    - str: "Yes" if the pattern is found, otherwise "No".
    """
    return 'Yes' if p in s + s else 'No'