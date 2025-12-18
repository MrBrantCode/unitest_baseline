"""
QUESTION:
Write a function `calculate_remainders` that takes in a list of pairs of integers and returns a list of remainders for each pair. The remainder should be calculated as the first number in the pair divided by the second number. If the second number in a pair is 0, the function should return 'Error: Division by 0' for that pair. The function should handle any errors that may occur during the division process.
"""

def calculate_remainders(pairs):
    # initialize the list to store results
    results = []
    for pair in pairs:
        try:
            # if the second number in a pair is 0, a ZeroDivisionError will be raised
            result = pair[0] % pair[1]
            results.append(result)
        except ZeroDivisionError:
            results.append('Error: Division by 0')
        except Exception as e:
            results.append('Error: ' + str(e))
    return results