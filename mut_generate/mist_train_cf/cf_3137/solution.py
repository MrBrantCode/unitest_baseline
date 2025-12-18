"""
QUESTION:
Implement a function `sqrt(num)` to calculate the integer square root of a positive number `num` without using any built-in square root function, with a time complexity of O(log n) and a space complexity of O(1). The function should return the integer square root rounded to the nearest integer.
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