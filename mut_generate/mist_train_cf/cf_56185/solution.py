"""
QUESTION:
Design a function called `stats_calculator` that takes a list of real numbers as input and returns the mean, median, and mode of the list. The function should handle input errors and invalid data, including non-numeric values and non-list inputs. The function should also handle cases where the list length is even for median calculation.
"""

def stats_calculator(numbers):
    # Check if input is a list
    if type(numbers) == list:
        # Remove anything that's not a number
        numbers = [i for i in numbers if type(i) in [int, float]]
        if not numbers:
            return 'Error: The list is empty or contains no real numbers.'
        
        mean = sum(numbers)/len(numbers)
        
        numbers.sort()
        if len(numbers) % 2 == 0:
            median = (numbers[len(numbers)//2-1] + numbers[len(numbers)//2])/2
        else:
            median = numbers[len(numbers)//2]
            
        mode = max(set(numbers), key = numbers.count)
        return mean, median, mode
    else:
        return 'Error: Input is not a list.'