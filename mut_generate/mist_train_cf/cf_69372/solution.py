"""
QUESTION:
Create a function `factorial(num, recursive=True, memo={})` that calculates the factorial of a given number. The function should be able to use both iterative and recursive approaches, with the recursive approach utilizing memoization to optimize its performance. The `recursive` argument is a Boolean value that determines whether the function uses the recursive or iterative approach. If `recursive` is `True`, the function should use the recursive approach; otherwise, it should use the iterative approach.
"""

def entance(num, recursive=True, memo={}):
    if num == 0 or num == 1:
        return 1
    
    # Memoization for the recursive solution
    if recursive and num in memo:
        return memo[num]

    if recursive:
        memo[num] = num * entance(num - 1, recursive=True, memo=memo)
        return memo[num]
    else:
        fact = 1
        for i in range(1, num + 1):
            fact *= i
        return fact