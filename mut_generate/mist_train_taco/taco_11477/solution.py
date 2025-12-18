"""
QUESTION:
A notice on the notice board read:

“Is there an end to it?

While the number remains greater than one, if 2 divides the number completely, divide the number by 2; while the number remains greater than 1, if the number is not divisible by 2 , multiply the successor of the number by 3 and increment this by three. "

David starts off with a number a wonders if there is an end to it?

Input – a single integer

Output -  “Yes” if the program will end, “No” otherwise (quotes for clarity only)

Sample Input:
17
Sample Output:
No

SAMPLE INPUT
17

SAMPLE OUTPUT
No
"""

def will_program_end(n: int) -> str:
    """
    Determines if the given number will eventually reach 1 based on the specified rules.

    Parameters:
    n (int): The starting number.

    Returns:
    str: "Yes" if the program will end, "No" otherwise.
    """
    if (n & (n - 1) == 0) and n != 0:
        return "Yes"
    else:
        return "No"