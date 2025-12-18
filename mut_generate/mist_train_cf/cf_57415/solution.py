"""
QUESTION:
Generate a function `fibonacci_sequence_up_to` that takes a positive integer `n` and returns a tuple containing the Fibonacci sequence up to `n` and the sum of the generated sequence. Implement another function `process_input_list` that takes a list of positive integers, calculates the Fibonacci sequence and sum for each integer, and returns a list of tuples, where each tuple contains the generated sequence and the corresponding sum. The `process_input_list` function should optimize the computation by storing previously computed sequences and recalling them when needed.
"""

def fibonacci_sequence_up_to(n):
    if n < 0:
        return "Error: Input should be a positive integer."
    if n == 0:
        return ([0], 0)
    if n == 1:
        return ([0, 1], 1)
    sequence = [0, 1]
    while sequence[-1] + sequence[-2] <= n:
        sequence.append(sequence[-1] + sequence[-2])
    return (sequence, sum(sequence))

def process_input_list(input_list):
    results = []
    previous_results = {}
    for number in input_list:
        if number not in previous_results:
            sequence, sequence_sum = fibonacci_sequence_up_to(number)
            results.append((sequence, sequence_sum))
            previous_results[number] = (sequence, sequence_sum)
        else:
            results.append(previous_results[number])
    return results