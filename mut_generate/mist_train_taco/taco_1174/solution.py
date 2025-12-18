"""
QUESTION:
There is a given sequence of integers a1, a2, ..., an, where every number is from 1 to 3 inclusively. You have to replace the minimum number of numbers in it so that all the numbers in the sequence are equal to each other.

Input

The first line contains an integer n (1 ≤ n ≤ 106). The second line contains a sequence of integers a1, a2, ..., an (1 ≤ ai ≤ 3).

Output

Print the minimum number of replacements needed to be performed to make all the numbers in the sequence equal.

Examples

Input

9
1 3 2 2 2 1 1 2 3


Output

5

Note

In the example all the numbers equal to 1 and 3 should be replaced by 2.
"""

def min_replacements_to_equalize_sequence(sequence):
    from collections import Counter
    
    # Count the frequency of each number in the sequence
    frequency = Counter(sequence)
    
    # Extract the counts of each number
    counts = list(frequency.values())
    
    # Sort the counts to find the minimum replacements needed
    counts.sort()
    
    # Determine the minimum replacements based on the number of unique counts
    if len(counts) == 3:
        return counts[0] + counts[1]
    elif len(counts) == 2:
        return counts[0]
    else:
        return 0