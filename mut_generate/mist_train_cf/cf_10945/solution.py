"""
QUESTION:
Create a function called merge_sort that takes an array of integers as input and returns a sorted array using an iterative merge sort approach, without using recursion. The function should be able to handle an array of any size.
"""

def merge_sort(arr):
    size = len(arr)
    temp = []
    length = 1

    while length < size:
        for i in range(0, size, 2 * length):
            left = i
            right = i + length
            left_end = min(i + length, size)
            right_end = min(i + 2 * length, size)
            i = left
            j = right

            while i < left_end and j < right_end:
                if arr[i] <= arr[j]:
                    temp.append(arr[i])
                    i += 1
                else:
                    temp.append(arr[j])
                    j += 1

            while i < left_end:
                temp.append(arr[i])
                i += 1

            while j < right_end:
                temp.append(arr[j])
                j += 1

            for k in range(left, right_end):
                arr[k] = temp[k - left]

            temp = []

        length *= 2

    return arr