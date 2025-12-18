"""
QUESTION:
Let's write all the positive integer numbers one after another from $1$ without any delimiters (i.e. as a single string). It will be the infinite sequence starting with 123456789101112131415161718192021222324252627282930313233343536...

Your task is to print the $k$-th digit of this sequence.


-----Input-----

The first and only line contains integer $k$ ($1 \le k \le 10000$) — the position to process ($1$-based index).


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

def get_kth_digit_in_sequence(k: int) -> int:
    """
    Returns the k-th digit in the infinite sequence of concatenated positive integers.

    Parameters:
    k (int): The position in the sequence (1-based index).

    Returns:
    int: The k-th digit in the sequence.
    """
    # Generate the sequence up to the required length
    sequence = ''.join((str(x) for x in range(1, 10001)))
    
    # Return the k-th digit (convert to 0-based index)
    return int(sequence[k - 1])