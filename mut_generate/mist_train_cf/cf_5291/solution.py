"""
QUESTION:
Generate a function `generate_random_numbers` that takes three parameters: a lower bound (`lower`), an upper bound (`upper`), and a count of numbers to generate (`count`). The function should return a list of `count` unique random numbers between `lower` and `upper` (inclusive) without using any built-in random number generator functions or libraries.
"""

def generate_random_numbers(lower, upper, count):
    numbers = list(range(lower, upper + 1))
    result = []

    for i in range(count):
        # Generate a random index within the remaining unshuffled part of the list
        rand_index = i + int((len(numbers) - i) * seed_random())

        # Swap the current element with the randomly selected element
        numbers[i], numbers[rand_index] = numbers[rand_index], numbers[i]

        # Append the current element to the result
        result.append(numbers[i])

    return result

def seed_random():
    seed = 1
    a = 1664525
    c = 1013904223
    m = 2**32
    seed = (a * seed + c) % m
    return seed / m