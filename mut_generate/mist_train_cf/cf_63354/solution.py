"""
QUESTION:
Create a function named `sort_integers` that takes a list of mixed data types as input, filters out non-integer entries, and categorizes the remaining integers into four lists: positive even numbers, positive odd numbers, negative even numbers, and negative odd numbers. The function should then print out the integers in each category in sorted order, and also print out the excluded non-integer entries.
"""

def sort_integers(user_input):
    if not isinstance(user_input, list):
        print("Invalid input. Please enter a list of integers.")
        return 

    positive_even = []
    positive_odd = []
    negative_even = []
    negative_odd = []
    excluded_entries = []

    for item in user_input:
        if not isinstance(item, int):
            excluded_entries.append(item)
            continue
        
        if item > 0:
            if item % 2 == 0:
                positive_even.append(item)
            else:
                positive_odd.append(item)

        if item < 0:
            if item % 2 == 0:
                negative_even.append(item)
            else:
                negative_odd.append(item)

    print("Positive Even: " + ','.join(map(str, sorted(positive_even))))
    print("Positive Odd: " + ','.join(map(str, sorted(positive_odd))))
    print("Negative Even: " + ','.join(map(str, sorted(negative_even))))
    print("Negative Odd: " + ','.join(map(str, sorted(negative_odd))))

    if excluded_entries:
        print("Excluded Entries: " + ','.join(map(str, excluded_entries)))