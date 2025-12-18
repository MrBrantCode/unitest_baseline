"""
QUESTION:
Create a function `find_instances` that takes a numerical array and a target integer as parameters. The function should return a list of tuples containing the target integer, its position in the array, and the distance from the previous instance of the target integer. If the target integer is the first instance, the distance should be represented by a dash (-). If the target integer does not exist in the array, the function should return a message indicating so.
"""

def find_instances(array, target):
    """
    This function takes a numerical array and a target integer as parameters.
    It returns a list of tuples containing the target integer, its position in the array, 
    and the distance from the previous instance of the target integer.
    
    If the target integer is the first instance, the distance is represented by a dash (-).
    If the target integer does not exist in the array, the function returns a message indicating so.

    Parameters:
    array (list): A list of integers.
    target (int): The target integer to be searched in the array.

    Returns:
    list or str: A list of tuples or a message if the target is not found.
    """
    prev_pos = None
    result = []
    for i, val in enumerate(array):
        if val == target:
            if prev_pos is None:
                result.append((target, i, "-"))
            else:
                result.append((target, i, i - prev_pos))
            prev_pos = i
    if not result:
        return f"Integer {target} not in array"
    else:
        return result