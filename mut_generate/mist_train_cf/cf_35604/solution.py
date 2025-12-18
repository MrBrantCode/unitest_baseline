"""
QUESTION:
Implement a constant-time branch operation function `select(subject, result_if_one, result_if_zero)` that takes three parameters: `subject`, `result_if_one`, and `result_if_zero`. The function should return `result_if_one` if `subject` is 1 and `result_if_zero` if `subject` is 0. The function must execute in constant time, meaning the execution time should not depend on the value of `subject`.
"""

def select(subject, result_if_one, result_if_zero):
    mask = -subject  
    return (result_if_one & mask) | (result_if_zero & ~mask)