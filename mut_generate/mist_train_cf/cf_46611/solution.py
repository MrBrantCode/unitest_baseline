"""
QUESTION:
Design a function `knuth_sequence_shell_sort` that sorts a list of integers using Shell Sort with Knuth's increment sequence. The function should take a list of integers as input and return the sorted list. The list can contain duplicate elements and can be of any size. Implement Knuth's increment sequence to determine the initial gap size and perform the shell sort. The gap size should be reduced to a third of its current size in each iteration until it becomes 0.
"""

def knuth_sequence_shell_sort(lst):
    length = len(lst)
    # Knuth's increment sequence
    gap = 1
    while gap < length//3:
        gap = gap*3 + 1
        
    # start shell sort
    while gap > 0:
        for i in range(gap, length):
            temp = lst[i]
            j = i
            while j >= gap and lst[j - gap] > temp:
                lst[j] = lst[j - gap]
                j -= gap
            lst[j] = temp
        gap //= 3
    return lst