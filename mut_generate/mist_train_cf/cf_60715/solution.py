"""
QUESTION:
Write a function named `operation_on_array` that takes in a 1D array of integers `arr`, an integer `target`, and a list of operations `operations`. The function should search for the `target` in `arr`, and if found, perform the operations in the order specified in `operations`. The allowed operations are 'swap' (swap the target with the first element of the array) and 'last' (move the target to the last position of the array). If the target is not found or an invalid operation is provided, handle the error accordingly. Return the modified array and the new index of the target if it exists, or -1 if the target is not found.
"""

def operation_on_array(arr, target, operations):
    # Check whether target exists in array
    if target not in arr:
        print(f'Target: {target} is not present in the array')
        return arr, -1

    target_index = arr.index(target)
    for operation in operations:
        if operation == 'swap':
            # Swap first element with target
            arr[0], arr[target_index] = arr[target_index], arr[0]
            # Update target_index after the swap
            target_index = arr.index(target)
        elif operation == 'last':
            arr.pop(target_index)
            arr.append(target)
            # Update target_index after the move
            target_index = len(arr) - 1
        else:
            print(f'Invalid operation: {operation}')
    return arr, target_index