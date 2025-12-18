"""
QUESTION:
Create a function named `find_duplicates` that takes an array of integers and floating-point numbers as input and returns a list of tuples, where each tuple contains a duplicate element and its frequency in the array. The array can contain a maximum of 10^6 elements and may include negative numbers. The function should use a hash table to efficiently detect duplicates.
"""

def find_duplicates(arr):
    freq_table = {}  # Hash table to store frequencies

    # Iterate through each element in the array
    for element in arr:
        # Convert the element to a string to handle floating-point numbers
        key = str(element)

        # If the key is already present in the hash table, increment its frequency
        if key in freq_table:
            freq_table[key] += 1
        else:
            # If the key is not present, add it to the hash table with a frequency of 1
            freq_table[key] = 1

    duplicates = []
    # Iterate through the hash table to find duplicate elements
    for key, frequency in freq_table.items():
        # If the frequency is greater than 1, it is a duplicate element
        if frequency > 1:
            duplicates.append((float(key) if '.' in key else int(key), frequency))

    return duplicates