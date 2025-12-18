"""
QUESTION:
Among the ruins of an ancient city a group of archaeologists found a mysterious function with lots of HOLES in it called ```getNum(n)``` (or `get_num(n)` in ruby, python, or r). They tried to call it with some arguments. And finally they got this journal:
The archaeologists were totally stuck with this challenge. They were all in desperation but then.... came YOU the SUPER-AWESOME programmer. Will you be able to understand the mystery of this function and rewrite it?
"""

def count_holes(n: int) -> int:
    """
    Counts the number of holes in the given number.
    
    A hole is defined as a closed area within a digit. For example:
    - '0', '6', and '9' each have 1 hole.
    - '8' has 2 holes.
    - Other digits have 0 holes.
    
    Args:
        n (int): The number to count holes in.
        
    Returns:
        int: The total number of holes in the number.
    """
    hole_counts = {'0': 1, '6': 1, '9': 1, '8': 2}
    return sum(hole_counts.get(d, 0) for d in str(n))