"""
QUESTION:
Write a function `bifurcate_sequence` that takes a list of integers or real numbers as input and divides it into two separate, non-overlapping segments such that the sum of the numbers in both segments is even. If the sum of the input list is odd, return an error message. The function should return two lists of numbers representing the two segments.
"""

def bifurcate_sequence(seq):
    total = sum(seq)
    if total % 2 != 0:
        return "Error: The total sum of the sequence is not even!"
    
    part1 = [] 
    part2 = []
    running_sum = 0
    
    for num in seq:
        if running_sum + num <= total // 2:
            running_sum += num
            part1.append(num)
        else:
            part2.append(num)
    
    return part1, part2