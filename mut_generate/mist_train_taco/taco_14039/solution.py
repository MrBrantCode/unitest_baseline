"""
QUESTION:
Tom goes out on the day "HOLI" wearing a checked shirt. After having a good time he returns with colors all over his shirt.

He cuts his shirt int a M*M checks, such that M is of the form 2N. Each check on his shirt has got a single color (Exactly one). The jth check on the ith row has got the same color as the (i+j)th check of the jth row. NOTE : (i+j) is always modulo M

Your task is to determine the maximum possible colors on his shirt.

Input

T, the number of test cases, followed by T lines.

Each line containing the positive integer 0<N<50000

Output

T lines of output, each line contain the positive integer, denoting the count of maximum possible colors on his shirt 

SAMPLE INPUT
2
1
3

SAMPLE OUTPUT
2
8
"""

def calculate_max_colors(n: int) -> int:
    """
    Calculate the maximum possible colors on Tom's shirt for a given N.

    Parameters:
    n (int): The value of N, where M = 2^N.

    Returns:
    int: The count of maximum possible colors on the shirt, which is 2^N.
    """
    return pow(2, n)