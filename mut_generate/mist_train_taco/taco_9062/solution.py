"""
QUESTION:
Lucky numbers are those numbers which are greater than all numbers to its right side.You task is to count all lucky numbers in a given array.
RightMost Element is always lucky Number
INPUT First line contain number of test case T. Each test case contain number of elements N.Next line contains elements of array.
OUTPUT Print numbers of lucky numbers.
Constraints
1 ≤ T ≤ 100

1 ≤ N ≤ 1000000

1 ≤ Elements ≤ 1000000

SAMPLE INPUT
1
6
16 17 4 3 5 2

SAMPLE OUTPUT
3

Explanation

Lucky numbers are 17 , 5 , 2
"""

def count_lucky_numbers(arr):
    n = len(arr)
    if n == 0:
        return 0
    
    # Initialize the count of lucky numbers
    lucky_count = 1  # The rightmost element is always a lucky number
    
    # Initialize the maximum element from the right
    max_from_right = arr[-1]
    
    # Traverse the array from the second last element to the first element
    for i in range(n-2, -1, -1):
        if arr[i] > max_from_right:
            lucky_count += 1
            max_from_right = arr[i]
    
    return lucky_count