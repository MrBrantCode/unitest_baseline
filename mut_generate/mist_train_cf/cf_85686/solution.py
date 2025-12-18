"""
QUESTION:
Write a function named `hex_sort` that takes a list of hexadecimal numbers as input, where numbers can be represented as integers (0-9) or characters ('A'-'F' for 10-15), and returns the sorted list in ascending order without using built-in sort methods.
"""

def hex_sort(arr):
    def hex_to_dec(c):
        if type(c) == str:
            return 10 + ord(c) - ord('A')
        return c

    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if hex_to_dec(arr[j]) > hex_to_dec(arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr