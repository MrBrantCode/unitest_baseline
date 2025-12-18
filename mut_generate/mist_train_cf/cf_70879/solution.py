"""
QUESTION:
Write a function `number_of_microscopes` that takes the number of microscopes at Springfield Elementary School as input. The function should calculate the number of microscopes at Shelbyville Elementary School, which is always 4/5 of the number of microscopes at Springfield. Ensure that the calculated number of microscopes at Shelbyville is a whole number. Implement error handling to return an error message if the input is not a non-negative integer or if the calculated number of microscopes at Shelbyville is not a whole number.
"""

def number_of_microscopes(springfield_microscopes):
    # Error handling for non-integer input
    if not isinstance(springfield_microscopes, int):
        return 'Error: Number of microscopes must be an integer.'
    
    # Error handling for negative input
    if springfield_microscopes < 0:
        return 'Error: Number of microscopes cannot be negative.'
    
    # calculate number of microscopes at Shelbyville
    shelbyville_microscopes = springfield_microscopes / 1.25

    # Error handling for non-integer outcome
    if not shelbyville_microscopes.is_integer():
        return 'Error: Number of microscopes at Shelbyville would not be a whole number.'
        
    return int(shelbyville_microscopes) # Return as integer