"""
QUESTION:
You will be given two ASCII strings, `a` and `b`. Your task is write a function to determine which one of these strings is "worth" more, and return it.

A string's worth is determined by the sum of its ASCII codepoint indexes. So, for example, the string `HELLO` has a value of 372: H is codepoint 72, E 69, L 76, and O is 79. The sum of these values is 372.

In the event of a tie, you should return the first string, i.e. `a`.
"""

def highest_value_string(a: str, b: str) -> str:
    """
    Determines which of the two given ASCII strings is "worth" more based on the sum of their ASCII codepoint indexes.

    Args:
        a (str): The first ASCII string.
        b (str): The second ASCII string.

    Returns:
        str: The string with the higher ASCII codepoint sum. If both sums are equal, returns the first string `a`.
    """
    def ascii_sum(s: str) -> int:
        return sum(ord(char) for char in s)
    
    return max(a, b, key=ascii_sum)