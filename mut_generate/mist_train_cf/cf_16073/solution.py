"""
QUESTION:
Write a function called `find_numbers` that takes two parameters: a list of numbers and a target sum. The function should find three distinct numbers in the list that add up to the target sum and return them as a list. If no such triplet exists, the function should return an empty list. The function should have a time complexity of O(n^2) and a space complexity of O(n).
"""

def find_numbers(numbers, target_sum):
    # Create a set to store the complement of each pair of numbers
    complements = set()
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            # Calculate the complement of the current pair of numbers
            complement = target_sum - (numbers[i] + numbers[j])
            # Check if the complement is in the complements set
            if complement in complements:
                # Return the three numbers that add up to the target sum
                return [complement, numbers[i], numbers[j]]
            # Add the complement of the current pair of numbers to the complements set
            complements.add(numbers[i])
            complements.add(numbers[j])
    # If no three numbers add up to the target sum, return an empty list
    return []