"""
QUESTION:
Create a function named `most_common_elements` that takes a list of elements as input and returns a list of the top 10 most common elements. If there are ties, all tied elements should be included. The function should handle any type of elements and any length of input list. The output list should be ordered by the frequency of elements in descending order.
"""

def most_common_elements(lst):
    # Create a dictionary to store the count of each element
    count_dict = {}
    
    # Count the occurrences of each element in the list
    for num in lst:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    
    # Sort the dictionary by the count of each element in descending order
    sorted_dict = sorted(count_dict.items(), key=lambda x: x[1], reverse=True)
    
    # Initialize a list to store the most common elements
    most_common = []
    
    # Add the most common elements to the list
    for item in sorted_dict:
        most_common.append(item[0])
    
    return most_common[:10]