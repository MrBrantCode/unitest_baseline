"""
QUESTION:
Create a function called `find_pattern` that identifies and returns the starting index of the first repeated sequence in a given list of numbers. The function should be able to detect patterns of any length and should not be limited to a specific sequence. The input is a list of integers, and the output should be the starting index of the pattern if found, or -1 if no pattern is found.
"""

def find_pattern(numbers):
    """
    Finds the starting index of the first repeated sequence in a given list of numbers.

    Args:
        numbers (list): A list of integers.

    Returns:
        int: The starting index of the pattern if found, or -1 if no pattern is found.
    """
    
    # Initialize the minimum pattern length to 1
    min_pattern_length = 1
    
    # Iterate over possible pattern lengths
    for pattern_length in range(min_pattern_length, len(numbers) // 2 + 1):
        
        # Check if the list length is divisible by the pattern length
        if len(numbers) % pattern_length == 0:
            
            # Initialize a flag to True, assuming the pattern is found
            pattern_found = True
            
            # Iterate over the list in chunks of pattern length
            for i in range(0, len(numbers), pattern_length):
                
                # If the chunk is not equal to the first chunk, the pattern is not found
                if numbers[i:i+pattern_length] != numbers[:pattern_length]:
                    pattern_found = False
                    break
            
            # If the pattern is found, return the starting index
            if pattern_found:
                return 0
    
    # If no pattern is found, return -1
    return -1