"""
QUESTION:
Given a non-negative integer N, find the largest number that is less than or equal to N with monotone increasing digits.

(Recall that an integer has monotone increasing digits if and only if each pair of adjacent digits x and y satisfy x .)


Example 1:

Input: N = 10
Output: 9



Example 2:

Input: N = 1234
Output: 1234



Example 3:

Input: N = 332
Output: 299



Note:
N is an integer in the range [0, 10^9].
"""

def find_monotone_increasing_digits(N: int) -> int:
    arr = [int(ch) for ch in str(N)]
    marker = len(arr)
    i = len(arr) - 2
    while i >= 0:
        if arr[i] > arr[i + 1]:
            marker = i + 1
            arr[i] -= 1
        i -= 1
    while marker < len(arr):
        arr[marker] = 9
        marker += 1
    return int(''.join([str(num) for num in arr]))