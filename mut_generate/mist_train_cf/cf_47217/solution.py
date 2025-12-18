"""
QUESTION:
Write a function `fibfib_with_offset(n: int, offset: int)` that efficiently computes the n-th element of the fibfib number sequence with an offset. The fibfib number sequence is defined as: 
- fibfib(0) = 0
- fibfib(1) = 0
- fibfib(2) = 1
- fibfib(n) = fibfib(n-1) + fibfib(n-2) + fibfib(n-3) for n >= 3
The function should store pre-calculated values for the fibfib sequence up to fibfib(n + offset), where offset is a non-negative integer.
"""

def fibfib_with_offset(n: int, offset: int) -> int:
    fibfib_list = [0, 0, 1]
    while len(fibfib_list) <= n + offset:
        fibfib_list.append(fibfib_list[-1] + fibfib_list[-2] + fibfib_list[-3])
    
    return fibfib_list[n]