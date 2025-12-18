"""
QUESTION:
DO YOU EXPECT ME TO FIND THIS OUT?

WHAT BASE AND/XOR LANGUAGE INCLUDES string?

DON'T BYTE OF MORE THAN YOU CAN CHEW

YOU CAN ONLY DISTORT THE LARGEST OF MATHEMATICS SO FAR

SAYING "ABRACADABRA" WITHOUT A MAGIC AND WON'T DO YOU ANY GOOD

THE LAST STACK RUPTURES. ALL DIE. OH, THE EMBARRASSMENT!

I HAVE NO ARRAY AND I MUST SCREAM

ELEMENTS MAY NOT BE STORED IN WEST HYPERSPACE


-----Input-----

The first line of input data contains a single integer n (1 ≤ n ≤ 10).

The second line of input data contains n space-separated integers a_{i} (1 ≤ a_{i} ≤ 11).


-----Output-----

Output a single integer.


-----Example-----
Input
4
2 5 3 1

Output
4
"""

def calculate_max_xor(n: int, a: list) -> int:
    """
    Calculate the XOR of the maximum value in the list with the last element of the list.

    Parameters:
    - n (int): The number of elements in the list.
    - a (list): A list of integers where each element is between 1 and 11.

    Returns:
    - int: The result of the XOR operation between the maximum value in the list and the last element of the list.
    """
    if n < 1 or n > 10:
        raise ValueError("The number of elements must be between 1 and 10.")
    
    if not all(1 <= x <= 11 for x in a):
        raise ValueError("All elements in the list must be between 1 and 11.")
    
    if len(a) != n:
        raise ValueError("The length of the list must match the specified number of elements.")
    
    max_value = max(a)
    last_element = a[-1]
    
    return max_value ^ last_element