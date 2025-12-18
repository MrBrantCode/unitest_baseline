"""
QUESTION:
Create a function named `categorize_list` that takes a list of numbers and an optional sorting order parameter as input. The function should categorize the numbers into odd and even, count the occurrences of each, sort the numbers in the specified order (default is descending), and print the categorized numbers along with their counts. The function should also handle empty input lists and lists containing non-numeric elements by printing an error message. The sorting order parameter should be either 'ascending' or 'descending'.
"""

def categorize_list(lst, sort_order='descending'):
    # Initialize counters for odd and even numbers
    odd_count = 0
    even_count = 0
    
    # Initialize empty lists for odd and even numbers
    odd_list = []
    even_list = []
    
    # Check if the list is empty
    if len(lst) == 0:
        print("The input list is empty.")
        return
    
    # Iterate over each element in the list
    for elem in lst:
        # Check if the element is numeric
        if not isinstance(elem, (int, float)):
            print("The input list contains non-numeric elements.")
            return
        
        # Categorize the element as odd or even
        if elem % 2 == 0:
            even_count += 1
            even_list.append(elem)
        else:
            odd_count += 1
            odd_list.append(elem)
    
    # Sort the odd and even lists in descending order
    if sort_order == 'descending':
        odd_list.sort(reverse=True)
        even_list.sort(reverse=True)
    elif sort_order == 'ascending':
        odd_list.sort()
        even_list.sort()
    else:
        print("Invalid sorting order. Please enter 'ascending' or 'descending'.")
        return
    
    # Print the odd and even lists with their counts
    print("Odd numbers ({0}): {1}".format(odd_count, odd_list))
    print("Even numbers ({0}): {1}".format(even_count, even_list))
    
    # Create a table to show the counts of odd and even numbers
    print("\nCount Table:")
    print("------------")
    print("| {0:^9} | {1:^9} |".format("Odd", "Even"))
    print("|{0:-^11}|{1:-^11}|".format("", ""))
    print("| {0:^9} | {1:^9} |".format(odd_count, even_count))