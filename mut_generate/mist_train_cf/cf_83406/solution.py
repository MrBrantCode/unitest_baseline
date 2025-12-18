"""
QUESTION:
Create a function `pattern_check(l: list, even: bool = False) -> bool` that checks if a list follows an alternating pattern of numbers and letters. If `even` is `True`, the numbers in the list must be even; otherwise, they must be odd. The function should return `True` if the list meets these conditions and `False` otherwise.
"""

def pattern_check(l: list, even: bool = False) -> bool:
    """
    Returns True if the list follows an alternated pattern (number, letter, number, and so on) heeding the even requirement and a supplementary condition - the list should not carry any even numbers when 'even' parameter is True. 
    If even is True, numbers in the list must be even; otherwise, they may be any.

    """
    for i in range(len(l)):
        if i % 2 == 0:
            if even:
                if not(isinstance(l[i], int) and l[i] % 2 == 0):
                    return False
            else:
                if not(isinstance(l[i], int) and l[i] % 2 != 0):
                    return False
        elif not isinstance(l[i], str):
            return False
    return True