"""
QUESTION:
-----Input-----

The input contains a single integer a (1 ≤ a ≤ 30).


-----Output-----

Output a single integer.


-----Example-----
Input
3

Output
27
"""

def get_lucky_number(a: int) -> int:
    lucky_numbers = [
        4, 22, 27, 58, 85, 94, 121, 166, 202, 265, 274, 319, 346, 355, 378, 382, 
        391, 438, 454, 483, 517, 526, 535, 562, 576, 588, 627, 634, 636, 645, 
        648, 654, 663, 666, 690, 706, 728, 729, 762, 778, 825, 852, 861, 895, 
        913, 915, 922, 958, 985, 1086, 1111, 1165
    ]
    return lucky_numbers[a - 1]