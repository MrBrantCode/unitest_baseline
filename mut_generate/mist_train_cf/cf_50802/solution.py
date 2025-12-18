"""
QUESTION:
Write a function `pattern_check` that checks if a given list `l` follows an alternated pattern of numbers and letters, meeting the even requirement. The function should take two parameters: `l` (the list to be checked) and `even` (a boolean indicating whether the numbers in the list should be even, defaults to False). The function should return True if the list follows the pattern and meets the even requirement, and False otherwise.
"""

def pattern_check(l: list, even: bool = False) -> bool:
    for i in range(len(l)):
        if i % 2 == 0:
            if even:
                if not (isinstance(l[i], int) and l[i] % 2 == 0):
                    return False
            else:
                if not isinstance(l[i], int):
                    return False
        elif not isinstance(l[i], str):
            return False
    return True