"""
QUESTION:
Let us define the beauty of a sequence (a_1,... ,a_n) as the number of pairs of two adjacent elements in it whose absolute differences are d. For example, when d=1, the beauty of the sequence (3, 2, 3, 10, 9) is 3.

There are a total of n^m sequences of length m where each element is an integer between 1 and n (inclusive). Find the beauty of each of these n^m sequences, and print the average of those values.

Constraints

* 0 \leq d < n \leq 10^9
* 2 \leq m \leq 10^9
* All values in input are integers.

Input

Input is given from Standard Input in the following format:


n m d


Output

Print the average of the beauties of the sequences of length m where each element is an integer between 1 and n. The output will be judged correct if the absolute or relative error is at most 10^{-6}.

Examples

Input

2 3 1


Output

1.0000000000


Input

1000000000 180707 0


Output

0.0001807060
"""

def calculate_average_beauty(n: int, m: int, d: int) -> float:
    if d != 0:
        return (2 * (n - d) * (m - 1)) / (n ** 2)
    else:
        return ((n - d) * (m - 1)) / (n ** 2)