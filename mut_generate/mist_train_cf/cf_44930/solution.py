"""
QUESTION:
Implement the `array_rotate` function to perform in-place array rotation without using any extra space or built-in rotate method. The rotation step can be both positive (right rotation) and negative (left rotation). Also, implement the `recovery` function to get the original array back. The function should handle possible edge cases, such as an empty array or a rotation step size larger than the length of the array. The input parameters are the array to be rotated and the rotation step. The function should modify the input array in-place. The recovery function should restore the original state of the array regardless of the previous rotation.
"""

def array_rotate(arr, rotation):
    """
    Rotate the input array in-place by the specified rotation step.

    Args:
        arr (list): The input array to be rotated.
        rotation (int): The rotation step. Positive for right rotation, negative for left rotation.

    Returns:
        list: The rotated array.
    """
    if not arr or rotation == 0:
        return arr

    rotation = rotation % len(arr)

    if rotation < 0:
        rotation += len(arr)

    arr[:rotation], arr[rotation:] = arr[-rotation:], arr[:-rotation]

    return arr

def recovery(arr, rotation):
    """
    Recover the original array by inversely rotating the given array.

    Args:
        arr (list): The rotated array to be recovered.
        rotation (int): The previous rotation step.

    Returns:
        list: The recovered array.
    """
    if rotation == 0:
        return arr
    rotation = -rotation % len(arr)
    return array_rotate(arr, rotation)