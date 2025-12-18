"""
QUESTION:
Implement a function `fib_modified_with_offset(n: int, offset: int)` to calculate the n-th element in a modified Fibonacci sequence with a non-negative offset. The sequence is defined as the sum of the (n-1)th, (n-3)rd, and (n-4)th elements. Use memoization to store pre-computed values. The function should handle base cases for n = 0, 1, 2, and 3, where the sequence values are calculated based on the specified offset.
"""

def fib_modified_with_offset(n: int, offset: int, memo = {}):
    # check if the value is in the memo dictionary
    if (n+offset) in memo: 
        return memo[n + offset]
    # base cases
    elif n == 0:
        result = offset
    elif n == 1:
        result = 1 + offset
    elif n == 2:
        result = 1 + 2 * offset
    elif n == 3:
        result = 2 + 4 * offset
    else:
        result = fib_modified_with_offset(n-1, offset, memo) + \
                  fib_modified_with_offset(n-3, offset, memo) + \
                  fib_modified_with_offset(n-4, offset, memo)

    # update the dict with the new found value
    memo[n + offset] = result
    return result