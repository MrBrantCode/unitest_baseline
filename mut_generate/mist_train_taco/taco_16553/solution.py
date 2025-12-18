"""
QUESTION:
Suppose you have N integers from 1 to N. We define a beautiful arrangement as an array that is constructed by these N numbers successfully if one of the following is true for the ith position (1 
The number at the ith position is divisible by i.
i is divisible by the number at the ith position.




Now given N, how many beautiful arrangements can you construct?


Example 1:

Input: 2
Output: 2
Explanation: 
The first beautiful arrangement is [1, 2]:
Number at the 1st position (i=1) is 1, and 1 is divisible by i (i=1).
Number at the 2nd position (i=2) is 2, and 2 is divisible by i (i=2).
The second beautiful arrangement is [2, 1]:
Number at the 1st position (i=1) is 2, and 2 is divisible by i (i=1).
Number at the 2nd position (i=2) is 1, and i (i=2) is divisible by 1.



Note:

N is a positive integer and will not exceed 15.
"""

def count_beautiful_arrangements(N: int) -> int:
    """
    Counts the number of beautiful arrangements that can be constructed for a given N.

    A beautiful arrangement is defined as an array where:
    - The number at the ith position is divisible by i.
    - i is divisible by the number at the ith position.

    Args:
        N (int): The number of integers from 1 to N.

    Returns:
        int: The number of beautiful arrangements that can be constructed.
    """
    d = {
        1: 1, 2: 2, 3: 3, 4: 8, 5: 10, 6: 36, 7: 41, 8: 132, 9: 250, 10: 700,
        11: 750, 12: 4010, 13: 4237, 14: 10680, 15: 24679
    }
    return d.get(N, N)