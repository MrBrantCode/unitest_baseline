"""
QUESTION:
Write a function `print_combinations(arr)` that prints all possible combinations of unique integer elements from an array in a non-repetitive manner, including the empty combination and individual elements, and handles arrays of any length.
"""

def print_combinations(arr):
    # Create an empty list to store the combinations
    combinations = []

    # Define a helper function that takes the current combination, remaining elements, and the index
    def generate_combinations(current, remaining, index):
        # If all elements have been used, add the current combination to the list
        if index == len(arr):
            combinations.append(current)
            return

        # Generate combinations by including the current element and recursively calling the function
        generate_combinations(current + [remaining[index]], remaining, index + 1)

        # Generate combinations by excluding the current element and recursively calling the function
        generate_combinations(current, remaining, index + 1)

    # Call the helper function with an empty current combination, the array, and the starting index
    generate_combinations([], arr, 0)

    # Print all the combinations
    for combination in combinations:
        print(combination)