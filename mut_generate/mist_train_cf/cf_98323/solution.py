"""
QUESTION:
Write a function `find_least_common_values` that takes a list of integers as input, filters out values outside the range [7, 12], and returns a table with the three least common values in the range and their corresponding frequencies in ascending order of value and descending order of frequency. If there are less than three unique values in the range, return all of them.
"""

def find_least_common_values(lst):
    # Filter the list to only include values between 7 and 12
    filtered_lst = [x for x in lst if x >= 7 and x <= 12]
    
    # Count the frequency of each value in the filtered list
    freq_dict = {}
    for x in filtered_lst:
        if x in freq_dict:
            freq_dict[x] += 1
        else:
            freq_dict[x] = 1
    
    # Sort the values in ascending order by frequency
    sorted_freq = sorted(freq_dict.items(), key=lambda x: (x[0], x[1]))
    
    # Extract the three least common values (if possible)
    least_common_values = sorted_freq[:min(3, len(sorted_freq))]
    
    # Create a table with the values and their frequencies
    table = [['Value', 'Frequency']]
    for x, freq in least_common_values:
        table.append([x, freq])
    
    return table