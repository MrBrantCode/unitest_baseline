"""
QUESTION:
Create a recursive function `print_odd_reverse` that prints odd numbers divisible by 3 from a given 2D array in reverse order. The function should take a 2D array `arr` and initial row and column indices as parameters. It should only print numbers that meet the specified conditions and handle the recursive calls to traverse the array in reverse order.
"""

def print_odd_reverse(arr, row, col):
    if row < 0:
        return

    if col < 0:
        print_odd_reverse(arr, row - 1, len(arr[row - 1]) - 1)
    else:
        if arr[row][col] % 2 != 0 and arr[row][col] % 3 == 0:
            print(arr[row][col])

        print_odd_reverse(arr, row, col - 1)