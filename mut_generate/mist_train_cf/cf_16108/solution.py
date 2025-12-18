"""
QUESTION:
Write a function named "print_numbers" that prints numbers from two input integers 'a' and 'b' in ascending order, but only if they are divisible by 2 and not by 3. The function should stop printing numbers once the sum of the printed numbers exceeds 100.
"""

def print_numbers(a, b):
    """
    Prints numbers from two input integers 'a' and 'b' in ascending order, 
    but only if they are divisible by 2 and not by 3. The function stops 
    printing numbers once the sum of the printed numbers exceeds 100.
    
    Args:
        a (int): The first integer.
        b (int): The second integer.
    """
    total = 0
    smaller = min(a, b)
    larger = max(a, b)

    while total <= 100:
        for num in range(smaller, larger + 1):
            if num % 3 != 0 and num % 2 == 0:
                print(num)
                total += num
                if total > 100:
                    return
        smaller += 1
        larger += 1