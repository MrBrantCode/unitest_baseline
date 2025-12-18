"""
QUESTION:
Write a function called `fibonacci` that generates the Fibonacci sequence up to the nth number. The function should be called within a loop that runs n times, where n is a positive integer provided by the user. The program should validate the user's input to ensure it is a positive integer and handle any exceptions or errors that may occur. The loop should print the loop index and the corresponding Fibonacci number each time it runs.
"""

def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        sequence = [0, 1]
        while len(sequence) < n:
            sequence.append(sequence[-1] + sequence[-2])
        return sequence