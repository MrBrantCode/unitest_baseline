"""
QUESTION:
Create a recursive function `digitize_number` that takes an integer `n` and an array `digits` as input. The function should progressively reduce the absolute value of `n` to zero, appending each prevailing digit to the `digits` array in the process. The function should handle negative integers by taking their absolute value and the number zero as a special case. After all digits have been appended, sort the `digits` array in ascending order without using any inbuilt array sort functions. The overall time complexity should be no worse than O(N log N) and the space complexity should be O(log N).
"""

def digitize_number(n, digits=[]):
    if n < 0:  
        return digitize_number(-n, digits)
    elif n == 0:  
        if not digits:  
            digits.append(0)
        digits = bubble_sort(digits)
        return digits
    else:
        digits.append(n % 10)
        return digitize_number(n // 10, digits)

def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr