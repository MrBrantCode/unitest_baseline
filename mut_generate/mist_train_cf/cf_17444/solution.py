"""
QUESTION:
Write a function `find_common_elements(arr1, arr2)` that compares two given arrays and returns a list of common elements present in both, while maintaining the relative order of the elements and removing duplicates. The function should have a time complexity of O(n), where n is the length of the longer array, and a space complexity of O(m), where m is the number of unique common elements between the two arrays. The solution should handle large arrays with up to 10^6 elements efficiently, be case-sensitive when comparing elements, and output a sorted list in ascending order.
"""

def find_common_elements(arr1, arr2):
    # Create a set to store unique common elements
    common_elements = set()
    
    # Create a dictionary to store the count of each element in arr2
    count_dict = {}
    for num in arr2:
        count_dict[num] = count_dict.get(num, 0) + 1
    
    # Iterate over arr1 and check if each element is present in arr2
    for num in arr1:
        # If the element is present in arr2 and has a count > 0, add it to the set
        if num in count_dict and count_dict[num] > 0:
            common_elements.add(num)
            count_dict[num] -= 1
    
    # Convert the set to a list and sort it in ascending order
    common_elements = sorted(list(common_elements))
    
    return common_elements