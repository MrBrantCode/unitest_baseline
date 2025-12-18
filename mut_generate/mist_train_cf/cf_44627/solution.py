"""
QUESTION:
Write a function named `nested_list` that takes a 3D array as input and returns a new nested list where each nested list contains the first and last elements of each valid inner list in the input array. A valid inner list must be non-empty and have integer values at its beginning and end. If an invalid inner list or subarray is encountered, the function should print a meaningful error message.
"""

def nested_list(array):
    new_list = []
    for subarray in array:
        if isinstance(subarray, list):
            for inner_list in subarray:
                if isinstance(inner_list, list) and len(inner_list) > 0:
                    try:
                        # check for integer values and non-empty lists
                        if isinstance(inner_list[0], int) and isinstance(inner_list[-1], int):
                            new_list.append([inner_list[0], inner_list[-1]])
                        else:
                            print("Error: Non-integer value encountered.")
                    except IndexError:
                        print("Error: Empty inner list.")
                else:
                    print("Error: Invalid inner list.")
        else:
            print("Error: Invalid subarray.")
    return new_list