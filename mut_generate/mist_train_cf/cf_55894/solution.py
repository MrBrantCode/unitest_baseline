"""
QUESTION:
Develop a function `check_arrays` that takes in a list of numerical arrays and returns a dictionary where each key is the array index and the value is its progression difference if the array elements are in a strict ascending arithmetic progression. If an array does not meet this condition, its index should not be included in the dictionary. The function should utilize multi-threading to evaluate the arrays concurrently. The input list of arrays can contain any number of arrays, and each array can contain any number of elements.
"""

from concurrent.futures import ThreadPoolExecutor

def check_arrays(arrays):
    def progression_difference(array):
        if len(array) < 2:
            return None
        diff = array[1] - array[0]
        for i in range(2, len(array)):
            if array[i] - array[i-1] != diff:
                return None
        return diff

    with ThreadPoolExecutor(max_workers=len(arrays)) as executor:
        results = executor.map(progression_difference, arrays)
    return {i: res for i, res in enumerate(results) if res is not None}