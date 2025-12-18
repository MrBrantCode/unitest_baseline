"""
QUESTION:
Create a function `filter_func` that takes a multi-dimensional array `inputArray` and a number `filterNumber` as input, and returns the modified array with all instances of `filterNumber` removed. The function should be able to handle arrays of varying depths and formats, and it should not include any empty arrays in the output.
"""

def filter_func(inputArray, filterNumber):
    outputArray = []
    for element in inputArray:
        if isinstance(element, list):
            filteredElement = filter_func(element, filterNumber)
            if filteredElement:  # if the filteredElement list is not empty
                outputArray.append(filteredElement)
        elif element != filterNumber:
            outputArray.append(element)
    return outputArray