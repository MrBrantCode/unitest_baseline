"""
QUESTION:
Create a function called `singular_occurrences` that takes a 3D matrix as input and returns a dictionary where the keys are the coordinates (i, j, k) of elements in the matrix and the values are the elements themselves. The function should only include elements that appear exactly once in the matrix.
"""

def singular_occurrences(matrix):
    # Initialize an empty dictionary
    output_dict = {}

    # Go through each element, capture its value and its location
    for i in range(len(matrix)):  # i represents the depth
        for j in range(len(matrix[i])):  # j represents the row
            for k in range(len(matrix[i][j])):  # k represents the column
                element = matrix[i][j][k]
                
                if element not in output_dict.values():
                    # If an element is not already in dictionary values,
                    # add its location and value to the dictionary
                    location = (i, j, k)
                    output_dict[location] = element
                else:
                    # If there's a recurring element, 
                    # find its key and remove it from the dictionary
                    for key, value in output_dict.items():
                        if value == element:
                            del output_dict[key]
                            break
                    
    return output_dict