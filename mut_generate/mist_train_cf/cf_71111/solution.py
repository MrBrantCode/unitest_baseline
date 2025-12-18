"""
QUESTION:
Create a function `find_third_smallest` that takes a list of mixed data types and a range defined by `lowerBound` and `upperBound` as input. The function should efficiently find the third smallest unique numeric value within the specified range, handling errors and large datasets gracefully. The input list may contain integers, fractions, and numbers in string format, as well as non-numeric data. If there are fewer than three unique numbers in the range, the function should return a corresponding message.
"""

def find_third_smallest(inputList, lowerBound, upperBound):
    uniqueNumbers = set()
    for item in inputList:
        try:
            number = float(item)
            if lowerBound <= number <= upperBound:
                uniqueNumbers.add(number)
        except ValueError:
            continue
    
    sortedNumbers = sorted(uniqueNumbers)
    if len(sortedNumbers) < 3:
        return "There are fewer than 3 unique values within the specified range"
    else:
        return sortedNumbers[2]