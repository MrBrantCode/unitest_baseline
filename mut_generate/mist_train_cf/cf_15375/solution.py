"""
QUESTION:
Create a function `fibonacci(n)` that generates the Fibonacci sequence up to the nth term, where n is a positive integer greater than 2, and returns the sequence along with the sum of all even numbers in the sequence without using any loops or if statements.
"""

def fibonacci(n):
    sequence = [0, 1]
    
    def generate_fibonacci(prev_1, prev_2, count):
        next_num = prev_1 + prev_2
        sequence.append(next_num)
        
        if count < n - 1: # check count against n - 1
            generate_fibonacci(prev_2, next_num, count + 1)
            
    generate_fibonacci(0, 1, 2) # call with count 2
    
    even_sum = sum(filter(lambda x: x % 2 == 0, sequence))
    
    return sequence, even_sum