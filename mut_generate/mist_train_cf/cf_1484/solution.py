"""
QUESTION:
Create a function named `find_strings_with_target` that takes in a list of strings (`lst`) and a target string (`target`). The function should print and count the strings in the list that contain the target string as a substring, ignoring case sensitivity. If a string contains multiple occurrences of the target string, count each occurrence separately. Return the total count of occurrences.
"""

def find_strings_with_target(lst, target):
    count = 0
    for string in lst:
        if target.lower() in string.lower():
            print(string)
            count += string.lower().count(target.lower())
    print("Count:", count)
    return count