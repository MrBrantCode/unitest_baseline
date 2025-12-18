"""
QUESTION:
There is a puzzle to complete by combining 14 numbers from 1 to 9. Complete by adding another number to the given 13 numbers.

The conditions for completing the puzzle are

* You must have one combination of the same numbers.
* The remaining 12 numbers are 4 combinations of 3 numbers.
The combination of three numbers is either three of the same numbers or three consecutive numbers. However, sequences such as 9 1 2 are not considered consecutive numbers.
* The same number can be used up to 4 times.



Create a program that reads a string of 13 numbers and outputs all the numbers that can complete the puzzle in ascending order. If you cannot complete the puzzle by adding any number from 1 to 9, output 0.

For example, if the given string is 3456666777999

If there is a "2", 234 567 666 77 999
If there is a "3", then 33 456 666 777 999
If there is a "5", then 345 567 666 77 999
If there is an "8", then 345 666 678 77 999

And so on, the puzzle is complete when one of the numbers 2 3 5 8 is added. Note that "6" is fine, but it will be used for the 5th time, so it cannot be used in this example.



Input

The input consists of multiple datasets. For each dataset, 13 numbers are given on one line. The number of datasets does not exceed 50.

Output

For each dataset, the numbers that can complete the puzzle are output on one line in ascending order, separated by blanks.

Example

Input

3649596966777
6358665788577
9118992346175
9643871425498
7755542764533
1133557799246


Output

2 3 5 8
3 4
1 2 3 4 5 6 7 8 9
7 8 9
1 2 3 4 6 7 8
0
"""

def find_completing_numbers(input_string: str) -> list:
    """
    Finds all numbers from 1 to 9 that can complete the puzzle by adding one number to the given 13 numbers.

    The conditions for completing the puzzle are:
    - You must have one combination of the same numbers.
    - The remaining 12 numbers are 4 combinations of 3 numbers.
    - The combination of three numbers is either three of the same numbers or three consecutive numbers.
    - The same number can be used up to 4 times.

    Parameters:
    input_string (str): A string of 13 numbers.

    Returns:
    list: A list of numbers that can complete the puzzle in ascending order, or [0] if no number can complete the puzzle.
    """
    
    def can_complete_puzzle(counts):
        if sum(counts) in counts:
            return True
        if 5 in counts:
            return False
        if 4 in counts:
            k = counts.index(4)
            counts[k] -= 3
            if can_complete_puzzle(counts):
                return True
            counts[k] += 3
        if 3 in counts:
            k = counts.index(3)
            counts[k] -= 3
            if can_complete_puzzle(counts):
                return True
            counts[k] += 3
        for i in range(7):
            if counts[i] and counts[i + 1] and counts[i + 2]:
                counts[i] -= 1
                counts[i + 1] -= 1
                counts[i + 2] -= 1
                if can_complete_puzzle(counts):
                    return True
                counts[i] += 1
                counts[i + 1] += 1
                counts[i + 2] += 1
        return False

    n = '123456789'
    input_list = list(input_string)
    possible_completions = []

    for i in n:
        counts = [(input_list + [i]).count(j) for j in n]
        if can_complete_puzzle(counts):
            possible_completions.append(i)

    return sorted(possible_completions) if possible_completions else [0]