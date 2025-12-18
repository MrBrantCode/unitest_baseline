"""
QUESTION:
You are given a positive number $x$. Find the smallest positive integer number that has the sum of digits equal to $x$ and all digits are distinct (unique).


-----Input-----

The first line contains a single positive integer $t$ ($1 \le t \le 50$) — the number of test cases in the test. Then $t$ test cases follow.

Each test case consists of a single integer number $x$ ($1 \le x \le 50$).


-----Output-----

Output $t$ answers to the test cases:

if a positive integer number with the sum of digits equal to $x$ and all digits are different exists, print the smallest such number;

otherwise print -1.


-----Examples-----

Input
4
1
5
15
50
Output
1
5
69
-1


-----Note-----

None
"""

def find_smallest_distinct_digit_number(x: int) -> int:
    # Precomputed list of smallest numbers with distinct digits for sums from 1 to 45
    arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 19, 29, 39, 49, 59, 69, 79, 89, 189, 289, 389, 489, 589, 689, 789, 1789, 2789, 3789, 4789, 5789, 6789, 16789, 26789, 36789, 46789, 56789, 156789, 256789, 356789, 456789, 1456789, 2456789, 3456789, 13456789, 23456789, 123456789]
    
    # Check if x is within the valid range
    if x < 1 or x > 45:
        return -1
    
    # Return the corresponding number from the precomputed list
    return arr[x]