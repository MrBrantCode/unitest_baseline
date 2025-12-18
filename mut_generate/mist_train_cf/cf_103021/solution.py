"""
QUESTION:
Create a function named `sort_and_filter_dictionary` that takes a dictionary as input and returns a new dictionary with keys that start with a vowel, sorted in descending order. The function should also print the total number of vowels in the dictionary. The input dictionary may contain keys with both lowercase and uppercase letters, but for the purpose of this problem, 'a', 'e', 'i', 'o', and 'u' (both lowercase and uppercase) are considered vowels.
"""

def sort_and_filter_dictionary(dictionary):
    vowels = ['a', 'e', 'i', 'o', 'u']
    filtered_dict = {}
    vowel_count = 0
    
    for key in sorted(dictionary, reverse=True):
        if key.lower() in vowels:
            filtered_dict[key] = dictionary[key]
            vowel_count += 1
    
    print(f"Total number of vowels: {vowel_count}")
    return filtered_dict