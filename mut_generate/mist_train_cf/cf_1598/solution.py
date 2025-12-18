"""
QUESTION:
Create a function called `most_common_elements` that takes a list as input and returns a list of the five most common elements. If there are ties for the most common elements or less than five unique elements, the function should return all unique elements in descending order of their occurrence.
"""

def most_common_elements(lst):
    freq_dict = {}
    for num in lst:
        freq_dict[num] = freq_dict.get(num, 0) + 1

    sorted_dict = sorted(freq_dict.items(), key=lambda x: x[1], reverse=True)

    result = []
    for num, count in sorted_dict:
        result.append(num)

    if len(result) <= 5:
        return result
    else:
        return result[:5]