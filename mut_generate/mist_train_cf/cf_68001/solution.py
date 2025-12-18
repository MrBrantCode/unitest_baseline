"""
QUESTION:
Find a pair of numbers in a collection that, when one is divided by the other, equals a certain value. The function `find_pair` should take a list of numbers and a quotient as input, and return the pair of numbers if found, or a message if no pair is found. The division operation should be exact, i.e., the result should be an integer.
"""

def find_pair(numbers, quotient):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] % numbers[j] == 0 and numbers[i] // numbers[j] == quotient:
                return (numbers[i], numbers[j])
            if numbers[j] % numbers[i] == 0 and numbers[j] // numbers[i] == quotient:
                return (numbers[j], numbers[i])
    return "No pair found."