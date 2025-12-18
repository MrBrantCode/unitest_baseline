"""
QUESTION:
Write a function `names_with_lowest_frequency` that takes a dictionary where keys are personal names and values are their occurrence frequencies. Return a list of names with the lowest frequency in lexicographical order. The function should handle multiple names with the same lowest frequency and implement its own sorting algorithm without using built-in `sort()` or `sorted()` methods. The input dictionary is guaranteed to have at least one key-value pair.
"""

def names_with_lowest_frequency(dictionary):
    # Find the lowest frequency
    lowest_frequency = min(dictionary.values())
    
    # Create a list of names with the lowest frequency
    names = [name for name, frequency in dictionary.items() if frequency == lowest_frequency]
    
    # Implement bubble sort for lexicographic ordering
    for i in range(len(names)):
        for j in range(len(names) - i - 1):
            if names[j] > names[j + 1]:
                names[j], names[j + 1] = names[j + 1], names[j]
    
    return names