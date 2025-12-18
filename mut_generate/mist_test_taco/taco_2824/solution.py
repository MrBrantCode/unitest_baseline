"""
QUESTION:
You are given two strings. In a single move, you can choose any of them, and delete the first (i.e. leftmost) character.

For Example:

* By applying a move to the string `"where"`, the result is the string `"here"`.
* By applying a move to the string `"a"`, the result is an empty string `""`.

Implement a function that calculates the minimum number of moves that should be performed to make the given strings equal.

## Notes

* Both strings consist of lowercase latin letters.
* If the string is already empty, you cannot perform any more delete operations.
"""

def min_moves_to_equal_strings(a: str, b: str) -> int:
    # Calculate the initial total number of characters in both strings
    total_moves = len(a) + len(b)
    
    # Iterate from the end of the strings towards the beginning
    for i in range(-1, -min(len(a), len(b)) - 1, -1):
        # If characters at the current position are not equal, break the loop
        if a[i] != b[i]:
            break
        # If characters are equal, reduce the total moves by 2 (one for each string)
        total_moves -= 2
    
    return total_moves