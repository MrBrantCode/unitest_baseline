"""
QUESTION:
Write a function named `remove_duplicates` that takes a list of strings as input. The function should return a list with duplicate strings removed while maintaining the original order of occurrence. Additionally, it should print the strings that were removed along with their counts.
"""

def remove_duplicates(input_list):
    result = []
    count = {}
    duplicates = {}

    for string in input_list:
        if string not in count:
            count[string] = 1
            result.append(string)
        else:
            count[string] += 1
            if count[string] == 2:
                duplicates[string] = 1
            else:
                duplicates[string] += 1

    print("Duplicates and their count:")
    for key, value in duplicates.items():
        print(f"String: {key}, Count: {value}")
    
    return result