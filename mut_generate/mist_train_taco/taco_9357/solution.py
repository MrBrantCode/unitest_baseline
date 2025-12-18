"""
QUESTION:
Write a program of the Bubble Sort algorithm which sorts a sequence A in ascending order. The algorithm should be based on the following pseudocode:


BubbleSort(A)
1 for i = 0 to A.length-1
2     for j = A.length-1 downto i+1
3         if A[j] < A[j-1]
4             swap A[j] and A[j-1]


Note that, indices for array elements are based on 0-origin.

Your program should also print the number of swap operations defined in line 4 of the pseudocode.

Constraints

1 ≤ N ≤ 100

Input

The first line of the input includes an integer N, the number of elements in the sequence.

In the second line, N elements of the sequence are given separated by spaces characters.

Output

The output consists of 2 lines.

In the first line, please print the sorted sequence. Two contiguous elements of the sequence should be separated by a space character.

In the second line, please print the number of swap operations.

Examples

Input

5
5 3 2 4 1


Output

1 2 3 4 5
8


Input

6
5 2 4 6 1 3


Output

1 2 3 4 5 6
9
"""

def bubble_sort_with_swap_count(A):
    """
    Sorts the list A using the Bubble Sort algorithm and returns the sorted list along with the number of swap operations.

    Parameters:
    A (list of int): The list of integers to be sorted.

    Returns:
    tuple: A tuple containing the sorted list and the number of swap operations.
    """
    n = len(A)
    count = 0
    flag = True
    
    while flag:
        flag = False
        for i in range(n - 1):
            if A[i] > A[i + 1]:
                A[i], A[i + 1] = A[i + 1], A[i]
                count += 1
                flag = True
    
    return A, count