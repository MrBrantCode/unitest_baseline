"""
QUESTION:
Implement the function `find_three_sum(array, target)` to find all sets of three distinct numbers in an array that add up to a given target number. The array contains positive integers only and may have duplicate values. The function should return the sets in ascending order without any duplicates, with a time complexity of O(n^2) or less.
"""

def find_three_sum(array, target):
    array.sort()  # Sort the array in ascending order
    result = []

    for i in range(len(array) - 2):
        if i > 0 and array[i] == array[i-1]:  # Skip duplicate elements
            continue
        
        left = i + 1
        right = len(array) - 1

        while left < right:
            current_sum = array[i] + array[left] + array[right]

            if current_sum == target:
                result.append([array[i], array[left], array[right]])

                # Skip duplicate elements
                while left < right and array[left] == array[left+1]:
                    left += 1
                while left < right and array[right] == array[right-1]:
                    right -= 1

                left += 1
                right -= 1
            elif current_sum < target:
                left += 1
            else:
                right -= 1

    return result