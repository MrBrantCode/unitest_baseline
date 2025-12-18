"""
QUESTION:
D: Sontaku (Surmise)

Some twins like even numbers.

Count how many even numbers are in $ N $ integers $ A_1, A_2, A_3, \ dots, A_N $.

input

The integer $ N $ is given on the first line.

On the second line, $ N $ integers $ A_1, A_2, A_3, \ dots, A_N $ are given, separated by blanks.

output

Output an even number. However, insert a line break at the end.

Constraint

* $ N $ is an integer greater than or equal to $ 1 $ and less than or equal to $ 100 $
* $ A_1, A_2, A_3, \ dots, A_N $ are integers between $ 1 $ and $ 100 $



Input example 1


Five
4 3 5 2 6


Output example 1


3


$ A_1 = 4 $, $ A_4 = 2 $ and $ A_5 = 6 $ are even numbers. Therefore, the even number is $ 3 $.

Input example 2


3
2 2 2


Output example 2


3


Even if the numbers are the same, if the positions in $ A_1, A_2, A_3, \ dots, A_N $ are different, they are counted as different numbers.





Example

Input

5
4 3 5 2 6


Output

3
"""

def count_even_numbers(N: int, A: list) -> int:
    """
    Counts the number of even numbers in the list A.

    Parameters:
    - N (int): The number of integers in the list.
    - A (list): A list of integers where each integer is between 1 and 100.

    Returns:
    - int: The count of even numbers in the list A.
    """
    # Calculate the count of even numbers
    even_count = sum(1 for x in A if x % 2 == 0)
    return even_count