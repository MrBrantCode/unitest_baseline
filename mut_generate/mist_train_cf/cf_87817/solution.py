"""
QUESTION:
Implement the `sqrt` function to calculate the square root of a given positive integer `num` without using any built-in square root function, rounded to the nearest integer. The function should have a time complexity of O(log n) and a space complexity of O(1).
"""

def sqrt(num):
    start = 0
    end = num
    ans = -1

    while start <= end:
        mid = (start + end) // 2
        if mid * mid == num:
            ans = mid
            break
        elif mid * mid < num:
            start = mid + 1
        else:
            end = mid - 1

    if ans == -1:
        ans = end

    return int(ans)