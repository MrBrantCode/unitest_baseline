"""
QUESTION:
Write a function named `is_descending_3d` that checks if all elements in a given 3D array are in descending order in terms of depth, row, and column. The function should return `True` if the array is in descending order, `False` otherwise. If the input is not a 3D list or the elements in the list are not well-structured, the function should return an error message. If any other error occurs, the function should return a generic error message.
"""

def is_descending_3d(arr):
    try: 
        # Loop over the depth
        for z in range(len(arr)-1, -1, -1):
            # Loop over rows
            for y in range(len(arr[z])-1, -1, -1):
                # Loop over columns
                for x in range(len(arr[z][y])-1, -1, -1):
                    # If there is depth for comparison
                    if z > 0:
                        if arr[z][y][x] > arr[z-1][y][x]:
                            return False
                    # If there is row for comparison
                    if y > 0:
                        if arr[z][y][x] > arr[z][y-1][x]:
                            return False
                    # If there is column for comparison
                    if x > 0:
                        if arr[z][y][x] > arr[z][y][x-1]:
                            return False
        return True
    except TypeError:
        return 'Error: The input should be a 3D list'
    except IndexError:
        return 'Error: The elements in the list are not well-structured'
    except:
        return 'Error: Something went wrong'