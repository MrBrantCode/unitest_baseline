"""
QUESTION:
Create a function called `fibonacci` that takes a positive integer `n` greater than 2 as input and returns a tuple containing the Fibonacci sequence up to the nth term and the sum of all the even numbers in the sequence, without using any loops or if statements in the main function.
"""

def fibonacci(n):
    if n <= 0:
        return "Invalid input. n should be a positive integer greater than 2."
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    sequence = [0, 1]
    
    def generate_fibonacci(prev_1, prev_2, count):
        next_num = prev_1 + prev_2
        sequence.append(next_num)
        
        if count < n:
            generate_fibonacci(prev_2, next_num, count + 1)
            
    generate_fibonacci(0, 1, 3)
    
    even_sum = sum(filter(lambda x: x % 2 == 0, sequence))
    
    return sequence, even_sum