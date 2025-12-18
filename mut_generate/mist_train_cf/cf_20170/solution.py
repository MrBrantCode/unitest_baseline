"""
QUESTION:
Create a function called `fibonacci_sum_greater_than` that takes one parameter, `limit`, representing the target sum. The function should generate a Fibonacci sequence starting with 0 and 2, adding the last two numbers to get the next number, but only including even numbers in the sequence. It should continue generating numbers until the sum of the sequence exceeds the given `limit`. The function should return the generated Fibonacci sequence and the average of the even numbers in the sequence.
"""

def fibonacci_sum_greater_than(limit):
    sequence = [0, 2]  # Starting Fibonacci sequence with first two even numbers
    sum_sequence = 2  # Initial sum

    while sum_sequence <= limit:
        # Calculate next Fibonacci number by adding the last two numbers in the sequence
        next_number = sequence[-1] + sequence[-2]
        
        # Check if the next number is even
        if next_number % 2 == 0:
            sequence.append(next_number)
            sum_sequence += next_number

    # Compute the average of the even numbers in the sequence
    even_numbers = [number for number in sequence if number % 2 == 0]
    average = sum(even_numbers) / len(even_numbers)
    
    return sequence, average