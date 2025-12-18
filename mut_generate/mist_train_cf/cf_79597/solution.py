"""
QUESTION:
Write a function `fun` that takes a boolean template parameter `B` and returns an integer value based on the value of `B` at compile time using `if constexpr`. The function should return 1 if `B` is true and 0 if `B` is false. Discuss the performance implications of using `if constexpr` in this context and its potential benefits and limitations.
"""

def fun(b):
    if b:
        return 1
    return 0