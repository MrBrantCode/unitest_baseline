"""
QUESTION:
Write a function named `find_least_common_values` that takes a list of integers as input. The function should filter out integers not within the range 7 to 12 (inclusive), count the frequency of each integer, and then find the three least common integers in the filtered list. The function should return a table (as a list of lists) with the three least common integers in ascending order and their frequencies in descending order. If there are less than three unique integers in the filtered list, the function should return all of them.
"""

def entrance(lst):
    filtered_lst = [x for x in lst if 7 <= x <= 12]
    
    freq_dict = {}
    for x in filtered_lst:
        if x in freq_dict:
            freq_dict[x] += 1
        else:
            freq_dict[x] = 1
    
    sorted_freq = sorted(freq_dict.items(), key=lambda x: (x[1], x[0]))
    
    least_common_values = sorted_freq[:min(3, len(sorted_freq))]
    
    table = [['Value', 'Frequency']]
    for x, freq in least_common_values:
        table.append([x, freq])
    
    return table