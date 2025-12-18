"""
QUESTION:
Write a function named `findTriplet` that takes two parameters: a multidimensional array of numeric entities and a target sum. The function should return `True` if there exists a triplet in the array with distinct elements that sum up to the target sum, and `False` otherwise. The function should handle nested arrays and ignore any non-numeric entities. The time complexity of the function should be reasonable for handling large arrays.
"""

def findTriplet(arr, sum):
    def flattenArray(array):
        result = []
        for i in array:
            if isinstance(i, list):
                result.extend(flattenArray(i))
            elif isinstance(i, (int, float)):  # Only consider numeric entities
                result.append(i)
        return result

    flattenedArray = flattenArray(arr)
    for i in range(len(flattenedArray)):
        for j in range(i + 1, len(flattenedArray)):
            for k in range(j + 1, len(flattenedArray)):
                if flattenedArray[i] + flattenedArray[j] + flattenedArray[k] == sum:
                    return True
    return False