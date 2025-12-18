"""
QUESTION:
Let's write all the positive integer numbers one after another from $1$ without any delimiters (i.e. as a single string). It will be the infinite sequence starting with 123456789101112131415161718192021222324252627282930313233343536...

Your task is to print the $k$-th digit of this sequence.


-----Input-----

The first and only line contains integer $k$ ($1 \le k \le 10^{12}$) — the position to process ($1$-based index).


-----Output-----

Print the $k$-th digit of the resulting infinite sequence.


-----Examples-----
Input
7

Output
7

Input
21

Output
5
"""

def get_kth_digit_in_sequence(k: int) -> str:
    """
    Returns the k-th digit in the infinite sequence of concatenated positive integers.

    Parameters:
    k (int): The position in the sequence (1-based index).

    Returns:
    str: The k-th digit in the sequence.
    """
    k -= 1  # Convert to 0-based index
    y = 9
    x = 1
    while k >= x * y:
        k -= x * y
        y *= 10
        x += 1
    start = 10 ** (x - 1)
    start += k // x
    return str(start)[k % x]