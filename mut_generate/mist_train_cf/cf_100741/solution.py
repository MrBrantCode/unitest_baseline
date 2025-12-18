"""
QUESTION:
Create a function called `split_fruits` that takes in a list of elements as input. The function should split the list into two different lists: one containing elements that have a vowel in their name and another containing elements that have a consonant in their name. The function should handle cases where the input list contains duplicates or non-string elements, skipping these elements in the process. The output should be two separate lists of string elements, with each list containing the corresponding elements based on the above conditions.
"""

def split_fruits(fruits):
    vowels = ['A', 'E', 'I', 'O', 'U']
    list1 = []
    list2 = []
    for fruit in fruits:
        if not isinstance(fruit, str) or not fruit.isalpha():
            continue
        if any(v in fruit.upper() for v in vowels):
            list1.append(fruit)
        else:
            list2.append(fruit)
    return list1, list2